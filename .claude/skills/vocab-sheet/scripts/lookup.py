#!/usr/bin/env python3
"""
Look up Japanese words for the vocab spreadsheet.

Queries the Japanese Vocab Fetcher API one word and one source at a time
(the deployed API returns 500 when several words share a request) and prints
a compact JSON summary per word: reading(s), parts of speech, meanings, OJAD
pitch accent and Tatoeba example sentences.

Usage:
    lookup.py 蝉 蜻蛉
    lookup.py --file words.txt
    echo "蝉、蜻蛉" | lookup.py
    lookup.py --sources jisho,ojad,wadoku,tatoeba 蝉

Standard library only.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_API_URL = "https://api.benleong.uk/jp"
DEFAULT_SOURCES = ("jisho", "ojad", "tatoeba")
ALL_SOURCES = ("jisho", "ojad", "wadoku", "suzuki", "tatoeba", "wanikani", "japanesepod", "forvo")
TIMEOUT = 60
RETRIES = 2


def read_words(args: argparse.Namespace) -> list[str]:
    lines = list(args.words)
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            lines.extend(f.read().splitlines())
    if not lines and not sys.stdin.isatty():
        lines.extend(sys.stdin.read().splitlines())
    words: list[str] = []
    for line in lines:
        for word in line.replace("、", ",").replace("\t", ",").split(","):
            word = word.strip()
            if word and word not in words:
                words.append(word)
    return words


USE_GET = False  # flipped on when the deployed API turns out not to support POST


def _request(req: urllib.request.Request) -> dict:
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode())[0]


def fetch_word(api_url: str, word: str, sources: list[str]) -> dict[str, dict]:
    """Return {source: item} for one word.

    POST /words lets us pick sources, one request per source (the API 500s
    when several words or sources share a request). If POST isn't deployed
    (404/405), fall back to GET /words, which queries every source in one go.
    """
    global USE_GET
    items: dict[str, dict] = {}
    if not USE_GET:
        for source in sources:
            body = json.dumps({"words": [word], "sources": [source]}).encode()
            req = urllib.request.Request(
                f"{api_url}/words", data=body, method="POST",
                headers={"Content-Type": "application/json"},
            )
            last_error = None
            for attempt in range(RETRIES + 1):
                try:
                    items[source] = _request(req)
                    break
                except urllib.error.HTTPError as e:
                    if e.code in (403, 404, 405):
                        USE_GET = True
                        break
                    last_error = e
                    time.sleep(2 * (attempt + 1))
                except (urllib.error.URLError, TimeoutError) as e:
                    last_error = e
                    time.sleep(2 * (attempt + 1))
            if USE_GET:
                break
            if source not in items:
                items[source] = {"word": word, source: {"success": False, "error": {"error_msg": str(last_error)}}}
        if not USE_GET:
            return items

    query = urllib.parse.urlencode({"words": json.dumps([word])})
    req = urllib.request.Request(f"{api_url}/words?{query}")
    last_error = None
    for attempt in range(RETRIES + 1):
        try:
            item = _request(req)
            return {source: item for source in sources}
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            last_error = e
            time.sleep(2 * (attempt + 1))
    return {
        source: {"word": word, source: {"success": False, "error": {"error_msg": str(last_error)}}}
        for source in sources
    }


def main_data(item: dict, source: str) -> dict:
    return (item.get(source) or {}).get("main_data") or {}


def summarise(word: str, items: dict[str, dict]) -> dict:
    out: dict = {"word": word}
    jisho = items.get("jisho")
    results = main_data(jisho, "jisho").get("results") if jisho else None
    if results:
        top = results[0]
        readings = []
        for jp in top.get("japanese", []):
            r = jp.get("reading") or jp.get("word")
            if r and r not in readings:
                readings.append(r)
        out["jisho_match"] = top.get("slug")
        out["readings"] = readings
        out["common"] = top.get("is_common", False)
        out["jlpt"] = [j.replace("jlpt-", "").upper() for j in top.get("jlpt", [])]
        out["senses"] = [
            {"pos": s.get("parts_of_speech", []), "en": s.get("english_definitions", []),
             "tags": s.get("tags", []), "info": s.get("info", [])}
            for s in top.get("senses", [])[:5]
        ]
        out["suru_verb"] = any("Suru verb" in p for s in out["senses"] for p in s["pos"])
        out["usually_kana"] = any("Usually written using kana alone" in t for s in out["senses"] for t in s["tags"])
    elif jisho is not None:
        out["jisho_match"] = None

    accents = {}
    for src in ("ojad", "wadoku", "suzuki"):
        acc = main_data(items.get(src, {}), src).get("accent")
        if acc:
            accents[src] = acc
    if accents:
        out["accent"] = accents

    sentences = []
    for src in ("tatoeba", "wanikani"):
        sentences.extend(main_data(items.get(src, {}), src).get("sentences") or [])
    if sentences:
        out["sentences"] = sentences[:5]

    errors = {
        src: (v.get("error") or {}).get("error_msg", "failed")
        for src, v in items.items()
        if isinstance(v.get(src), dict) and not v[src].get("success", True)
    }
    if errors:
        out["errors"] = errors
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[1])
    parser.add_argument("words", nargs="*")
    parser.add_argument("--file")
    parser.add_argument("--sources", default=",".join(DEFAULT_SOURCES))
    parser.add_argument("--api-url", default=os.environ.get("VOCAB_API_URL", DEFAULT_API_URL))
    args = parser.parse_args()

    sources = [s.strip() for s in args.sources.split(",") if s.strip()]
    unknown = set(sources) - set(ALL_SOURCES)
    if unknown:
        parser.error(f"unknown sources {sorted(unknown)}; choose from {', '.join(ALL_SOURCES)}")
    words = read_words(args)
    if not words:
        parser.error("no words given")

    api_url = args.api_url.rstrip("/")
    summaries = []
    for word in words:
        summaries.append(summarise(word, fetch_word(api_url, word, sources)))
        print(f"looked up {word}", file=sys.stderr)
    print(json.dumps(summaries, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
