#!/usr/bin/env python3
"""
Fetch information for a list of Japanese words from the Japanese Vocab Fetcher API.

Usage:
    fetch_vocab.py 食べる 猫 静か
    fetch_vocab.py --file words.txt --sources jisho,ojad
    echo "食べる" | fetch_vocab.py --format json
    fetch_vocab.py --raw 食べる

Only uses the standard library, so it can run with any python3.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_API_URL = "https://api.benleong.uk/jp"
ALL_SOURCES = (
    "forvo",
    "japanesepod",
    "jdict",
    "jisho",
    "ojad",
    "suzuki",
    "tatoeba",
    "wadoku",
    "wanikani",
)
DEFAULT_SOURCES = (
    "jisho",
    "jdict",
    "ojad",
    "suzuki",
    "wadoku",
    "japanesepod",
    "tatoeba",
    "wanikani",
)
ACCENT_SOURCES = ("ojad", "wadoku", "suzuki")
BATCH_SIZE = 20
TIMEOUT = 60


def read_words(args: argparse.Namespace) -> list[str]:
    lines: list[str] = list(args.words)
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            lines.extend(f.read().splitlines())
    if not lines and not sys.stdin.isatty():
        lines.extend(sys.stdin.read().splitlines())

    # Allow comma/、 separated words too, and drop duplicates while keeping order
    words: list[str] = []
    for line in lines:
        for word in line.replace("、", ",").split(","):
            word = word.strip()
            if word and word not in words:
                words.append(word)
    return words


def request(req: urllib.request.Request) -> list[dict]:
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode())


def fetch_batch(api_url: str, words: list[str], sources: list[str]) -> list[dict]:
    """Call POST /words, falling back to the older GET /words if POST isn't deployed"""
    body = json.dumps({"words": words, "sources": sources}).encode()
    post = urllib.request.Request(
        f"{api_url}/words",
        data=body,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        return request(post)
    except urllib.error.HTTPError as e:
        if e.code not in (403, 404, 405):
            raise

    query = urllib.parse.urlencode({"words": json.dumps(words)})
    results = request(urllib.request.Request(f"{api_url}/words?{query}"))
    return [
        {k: v for k, v in item.items() if k == "word" or k in sources}
        for item in results
    ]


def fetch(api_url: str, words: list[str], sources: list[str]) -> list[dict]:
    results: list[dict] = []
    for i in range(0, len(words), BATCH_SIZE):
        results.extend(fetch_batch(api_url, words[i : i + BATCH_SIZE], sources))
    return results


def main_data(item: dict, source: str) -> dict:
    return (item.get(source) or {}).get("main_data") or {}


def summarise(item: dict, max_senses: int) -> dict:
    """Condense the full API response for a word into the most useful fields"""
    summary: dict = {"word": item["word"], "jisho_requested": "jisho" in item}

    jisho_results = main_data(item, "jisho").get("results") or []
    if jisho_results:
        top = jisho_results[0]
        readings = []
        for jp in top.get("japanese", []):
            reading = jp.get("reading") or jp.get("word")
            if reading and reading not in readings:
                readings.append(reading)
        summary["jisho_match"] = top.get("slug")
        summary["readings"] = readings
        summary["common"] = top.get("is_common", False)
        summary["jlpt"] = [j.replace("jlpt-", "").upper() for j in top.get("jlpt", [])]
        summary["meanings"] = [
            {
                "pos": sense.get("parts_of_speech", []),
                "en": sense.get("english_definitions", []),
            }
            for sense in top.get("senses", [])[:max_senses]
        ]

    jdict_results = main_data(item, "jdict").get("results") or []
    if jdict_results and not jisho_results:
        # Fall back to JMdict (via WWWJDIC) when jisho has no exact match
        top = jdict_results[0]
        summary["readings"] = top.get("readings", [])
        summary["common"] = top.get("is_common", False)
        summary["meanings"] = [
            {"pos": sense.get("parts_of_speech", []), "en": sense.get("definitions", [])}
            for sense in top.get("senses", [])[:max_senses]
        ]
    if jdict_results:
        summary["jdict"] = [
            {
                "writings": entry.get("writings", []),
                "readings": entry.get("readings", []),
                "meanings": [
                    {"pos": sense.get("parts_of_speech", []), "en": sense.get("definitions", [])}
                    for sense in entry.get("senses", [])[:max_senses]
                ],
            }
            for entry in jdict_results
        ]

    accents = {
        source: main_data(item, source).get("accent")
        for source in ACCENT_SOURCES
        if main_data(item, source).get("accent")
    }
    if accents:
        summary["accent"] = accents

    audio = []
    for source in ("japanesepod", "forvo", "wanikani"):
        for clip in main_data(item, source).get("audio") or []:
            url = clip.get("url")
            if url:
                audio.append(url)
    if audio:
        summary["audio"] = audio[:3]

    sentences = []
    for source in ("wanikani", "tatoeba"):
        sentences.extend(main_data(item, source).get("sentences") or [])
    if sentences:
        summary["sentences"] = sentences[:2]

    errors = {
        source: (value.get("error") or {}).get("error_msg", "failed")
        for source, value in item.items()
        if isinstance(value, dict) and not value.get("success", True)
    }
    if errors:
        summary["errors"] = errors

    return summary


def as_markdown(summaries: list[dict]) -> str:
    lines = []
    for s in summaries:
        lines.append(f"## {s['word']}")
        if "readings" in s:
            extra = []
            if s["jisho_match"] != s["word"]:
                extra.append(f"jisho match: {s['jisho_match']}")
            if s["jlpt"]:
                extra.append("/".join(s["jlpt"]))
            if s["common"]:
                extra.append("common")
            suffix = f" ({', '.join(extra)})" if extra else ""
            lines.append(f"- Reading: {', '.join(s['readings'])}{suffix}")
            for i, m in enumerate(s["meanings"], 1):
                pos = f"[{', '.join(m['pos'])}] " if m["pos"] else ""
                lines.append(f"- {i}. {pos}{'; '.join(m['en'])}")
        elif s["jisho_requested"]:
            lines.append("- No dictionary entry found")
        for entry in s.get("jdict", []):
            forms = "、".join(entry["writings"] or entry["readings"])
            readings = f" [{'、'.join(entry['readings'])}]" if entry["writings"] else ""
            meanings = " / ".join(
                f"[{', '.join(m['pos'])}] " * bool(m["pos"]) + "; ".join(m["en"])
                for m in entry["meanings"]
            )
            lines.append(f"- JMdict: {forms}{readings} — {meanings}")
        for source, accent in s.get("accent", {}).items():
            lines.append(f"- Accent ({source}): {' / '.join(accent)}")
        for sentence in s.get("sentences", []):
            lines.append(f"- Example: {sentence['ja']} — {sentence['en']}")
        for url in s.get("audio", []):
            lines.append(f"- Audio: {url}")
        for source, msg in s.get("errors", {}).items():
            lines.append(f"- ⚠ {source} failed: {msg}")
        lines.append("")
    return "\n".join(lines)


def parse_sources(value: str) -> list[str]:
    if value == "all":
        return list(ALL_SOURCES)
    sources = [s.strip() for s in value.split(",") if s.strip()]
    unknown = set(sources) - set(ALL_SOURCES)
    if unknown:
        raise argparse.ArgumentTypeError(
            f"unknown sources {sorted(unknown)}; choose from {', '.join(ALL_SOURCES)}"
        )
    return sources


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[1])
    parser.add_argument("words", nargs="*", help="words to look up")
    parser.add_argument("--file", help="file with one word per line")
    parser.add_argument(
        "--sources",
        type=parse_sources,
        default=list(DEFAULT_SOURCES),
        help=f"comma separated, or 'all' (default: {','.join(DEFAULT_SOURCES)})",
    )
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--raw", action="store_true", help="print full API response")
    parser.add_argument("--max-senses", type=int, default=3)
    parser.add_argument(
        "--api-url",
        default=os.environ.get("VOCAB_API_URL", DEFAULT_API_URL),
        help="API base URL (or set VOCAB_API_URL), e.g. http://localhost:9090",
    )
    args = parser.parse_args()

    words = read_words(args)
    if not words:
        parser.error("no words given")

    try:
        results = fetch(args.api_url.rstrip("/"), words, args.sources)
    except urllib.error.HTTPError as e:
        print(f"API error {e.code}: {e.read().decode()[:500]}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Could not reach {args.api_url}: {e.reason}", file=sys.stderr)
        return 1

    if args.raw:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    summaries = [summarise(item, args.max_senses) for item in results]
    if args.format == "json":
        print(json.dumps(summaries, ensure_ascii=False, indent=2))
    else:
        print(as_markdown(summaries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
