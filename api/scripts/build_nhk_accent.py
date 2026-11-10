"""
Build `api/data/nhk_accent.tsv.gz` from the NHK accent dictionary CSV
(ACCDB_unicode.csv) distributed with https://github.com/javdejong/nhk-pronunciation.

Usage (from the `api` directory):
    uv run python scripts/build_nhk_accent.py [path/to/ACCDB_unicode.csv]

If no path is given, the CSV is downloaded from the pinned commit below.

Each output line is `word<TAB>accent`, where `word` is a lookup key (the NHK headword
or its kanji spelling) and `accent` is a hiragana reading with `' ` after the mora where
the pitch drops (the same format as the other accent modules, e.g. `め' がね`,
`がくせい`, `ことば'`).
Accent phrases in compounds are separated by `・`.
"""

import gzip
import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import NamedTuple

import requests

COMMIT = "09232150343f5bc912d3daa417de7843fa90276b"
REPO_URL = "https://raw.githubusercontent.com/javdejong/nhk-pronunciation"
CSV_URL = f"{REPO_URL}/{COMMIT}/ACCDB_unicode.csv"
CSV_SHA256 = "0b450bce4520c7121eddaa445607e4e7a650d96a9bbdf3fdea59f3db06330ed4"

OUTPUT_PATH = (
    Path(__file__).resolve().parent.parent / "api" / "data" / "nhk_accent.tsv.gz"
)

FIELDS = [
    "NID", "ID", "WAVname", "K_FLD", "ACT", "midashigo", "nhk", "kanjiexpr", "NHKexpr",
    "numberchars", "nopronouncepos", "nasalsoundpos", "majiri", "kaisi", "KWAV",
    "midashigo1", "akusentosuu", "bunshou", "ac",
]  # fmt: skip


class Entry(NamedTuple):
    id: str
    midashigo: str  # Standard katakana spelling, e.g. ガッコウ
    nhk: str  # NHK headword, e.g. ことば
    kanjiexpr: str  # Kanji spelling, e.g. 言葉
    nasalsoundpos: str
    midashigo1: str  # Pronunciation spelling the accent is aligned to, e.g. ガッコー
    ac: str  # Per-character pitch: 0 low, 1 high, 2 high then drop


def load_csv_text(path: str | None) -> str:
    if path is not None:
        data = Path(path).read_bytes()
    else:
        response = requests.get(CSV_URL, timeout=60)
        response.raise_for_status()
        data = response.content
        digest = hashlib.sha256(data).hexdigest()
        if digest != CSV_SHA256:
            raise ValueError(f"Unexpected checksum for downloaded CSV: {digest}")
    return data.decode("utf-8")


def parse_line(line: str) -> Entry | None:
    # Commas inside {...} and (...) in NHKexpr are not field separators
    line = re.sub(
        r"[{(][^{}()]*?,[^{}()]*?[})]", lambda m: m[0].replace(",", ";"), line
    )
    fields = line.split(",")
    if len(fields) != len(FIELDS):
        return None
    row = dict(zip(FIELDS, fields, strict=True))
    return Entry(
        id=row["ID"],
        midashigo=row["midashigo"],
        nhk=row["nhk"],
        kanjiexpr=row["kanjiexpr"],
        nasalsoundpos=row["nasalsoundpos"],
        midashigo1=row["midashigo1"],
        ac=row["ac"],
    )


def katakana_to_hiragana(text: str) -> str:
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in text)


def parse_positions(positions: str) -> list[int]:
    """Positions are 1-indexed and separated by 0s, eg "205" -> [2, 5], "20" -> [20]"""
    result: list[int] = []
    for part in positions.split("0"):
        if part:
            result.append(int(part))
        elif result:
            result[-1] *= 10
    return result


def restore_nasals(text: str, nasalsoundpos: str) -> str:
    """midashigo1 writes nasal ガ行 as カ行 (plus a nasal marker): restore dakuten"""
    chars = list(text)
    for pos in parse_positions(nasalsoundpos):
        if 0 < pos <= len(chars) and chars[pos - 1] in "カキクケコ":
            chars[pos - 1] = chr(ord(chars[pos - 1]) + 1)
    return "".join(chars)


def get_display_chars(entry: Entry) -> str | None:
    """
    Return a spelling aligned character-by-character with `entry.ac`, preferring the
    standard spelling (midashigo, eg ガッコウ) over the pronunciation spelling
    (midashigo1, eg ガッコー)
    """
    pron = entry.midashigo1
    if len(entry.midashigo) == len(pron):
        return entry.midashigo
    # midashigo1 separates accent phrases with ・, eg アイ・イレナイ
    if len(entry.midashigo) == len(pron.replace("・", "")):
        standard = iter(entry.midashigo)
        return "".join(c if c == "・" else next(standard) for c in pron)
    return restore_nasals(pron, entry.nasalsoundpos)


def format_accent(entry: Entry) -> str | None:
    chars = get_display_chars(entry)
    if chars is None or not chars or len(entry.ac) > len(chars):
        return None
    if not re.fullmatch(r"[012]+", entry.ac):
        return None
    pitches = entry.ac.zfill(len(chars))

    reading = ""
    for char, pitch in zip(chars, pitches, strict=True):
        reading += katakana_to_hiragana(char)
        if pitch == "2":
            reading += "' "
    return reading.rstrip(" ").replace(" ・", "・")


def build(csv_text: str) -> dict[str, list[str]]:
    entries = [e for e in map(parse_line, csv_text.splitlines()) if e is not None]

    # The same word/accent may be listed with several spellings
    # (eg ガッコウ and ガッコー): keep the one with the fewest long vowel marks
    best: dict[tuple[str, str, str, str], Entry] = {}
    for entry in entries:
        key = (entry.id, entry.nhk, entry.kanjiexpr, entry.ac)
        if key not in best or entry.midashigo.count("ー") < best[key].midashigo.count(
            "ー"
        ):
            best[key] = entry

    accent_dict: defaultdict[str, list[str]] = defaultdict(list)
    for entry in entries:
        if best[(entry.id, entry.nhk, entry.kanjiexpr, entry.ac)] is not entry:
            continue
        accent = format_accent(entry)
        if accent is None:
            continue
        for word in dict.fromkeys([entry.nhk, entry.kanjiexpr]):
            if word and accent not in accent_dict[word]:
                accent_dict[word].append(accent)
    return accent_dict


def main() -> None:
    csv_text = load_csv_text(sys.argv[1] if len(sys.argv) > 1 else None)
    accent_dict = build(csv_text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"{word}\t{accent}\n"
        for word, accents in accent_dict.items()
        for accent in accents
    ]
    # mtime=0 keeps the output byte-for-byte reproducible
    with (
        open(OUTPUT_PATH, "wb") as raw,
        gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as f,
    ):
        f.write("".join(lines).encode("utf-8"))
    print(f"Wrote {len(lines)} entries for {len(accent_dict)} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
