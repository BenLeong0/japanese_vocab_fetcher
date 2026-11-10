"""Pitch accent lookup using the Kanjium accent data.

Kanjium (https://github.com/mifunetoshiro/kanjium) publishes a tab-separated file
of `writing<TAB>reading<TAB>accent` rows. The reading is empty when the word is
written in kana, and the accent field is a comma-separated list of downstep
positions (the mora after which the pitch drops, 0 = heiban), optionally prefixed
by a part of speech, e.g. `(副)0,(名)3`.

The file is downloaded on first use and cached in memory for the life of the process.
"""

import re
import threading
import unicodedata
from collections import defaultdict

import requests

from api.custom_types.alternative_string_types import URL, Kaki, Yomi
from api.custom_types.exception_types import APIError
from api.custom_types.response_types import ResponseItemKanjium

NAME = "kanjium"

ACCENTS_URL = URL(
    "https://raw.githubusercontent.com/mifunetoshiro/kanjium/master"
    "/data/source_files/raw/accents.txt"
)

# Small kana that combine with the preceding kana into a single mora
SMALL_KANA = set("ゃゅょぁぃぅぇぉゎャュョァィゥェォヮ")

AccentDict = dict[str, list[Yomi]]

_accent_dict: AccentDict | None = None
_accent_dict_lock = threading.Lock()


class KanjiumAPIError(APIError):
    pass


def response_factory(accent_list: list[Yomi] | None = None) -> ResponseItemKanjium:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "accent": [] if accent_list is None else accent_list,
        },
    }


def error_response_factory(error: KanjiumAPIError) -> ResponseItemKanjium:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "accent": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemKanjium]:
    if not word_list:
        return {}

    try:
        accent_dict = get_accent_dict()
    except KanjiumAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word: error_response_factory(api_error) for word in word_list}

    return {
        word: response_factory(accent_list=accent_dict.get(normalise(word), []))
        for word in word_list
    }


# Fetch data


def get_accent_dict() -> AccentDict:
    """Return the (cached) mapping of writing -> formatted accents"""
    global _accent_dict  # pylint: disable=global-statement
    if _accent_dict is None:
        with _accent_dict_lock:
            if _accent_dict is None:
                _accent_dict = build_accent_dict(get_accents_text())
    return _accent_dict


def get_accents_text() -> str:
    try:
        response = requests.get(ACCENTS_URL, timeout=10)
    except Exception:
        raise KanjiumAPIError("request failed", 500, ACCENTS_URL) from None

    if response.status_code != 200:
        raise KanjiumAPIError(response.text, response.status_code, ACCENTS_URL)

    response.encoding = "utf-8"
    return response.text


# Parse data


def normalise(word: str) -> str:
    """Normalise full-width digits/letters so that e.g. `10月` matches `１０月`"""
    return unicodedata.normalize("NFKC", word).strip()


def build_accent_dict(text: str) -> AccentDict:
    accent_dict: defaultdict[str, list[Yomi]] = defaultdict(list)

    for line in text.splitlines():
        fields = line.split("\t")
        if len(fields) != 3:
            continue
        writing, reading, accent_field = fields
        reading = reading or writing
        key = normalise(writing)

        for position in parse_accent_field(accent_field):
            accent = format_accent(reading, position)
            if accent is not None and accent not in accent_dict[key]:
                accent_dict[key].append(accent)

    return dict(accent_dict)


def parse_accent_field(accent_field: str) -> list[int]:
    """`(副)0,(名)3,1` -> [0, 3, 1] (part of speech labels are dropped)"""
    positions: list[int] = []
    for part in accent_field.split(","):
        number = re.sub(r"^\([^)]*\)", "", part.strip())
        if number.isdigit() and int(number) not in positions:
            positions.append(int(number))
    return positions


def split_moras(reading: str) -> list[str]:
    moras: list[str] = []
    for char in reading:
        if char in SMALL_KANA and moras:
            moras[-1] += char
        else:
            moras.append(char)
    return moras


def format_accent(reading: str, position: int) -> Yomi | None:
    """Mark the downstep with `'`, like the other modules (`め' がね`, `がんきょう`)"""
    moras = split_moras(reading)
    if position > len(moras):
        return None
    if position == 0:
        return Yomi(reading)
    head, tail = "".join(moras[:position]), "".join(moras[position:])
    return Yomi(f"{head}' {tail}" if tail else f"{head}'")
