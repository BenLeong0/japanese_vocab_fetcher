"""
Jim Breen's JMdict/EDICT, via the WWWJDIC server (edrdg.org).

The `1ZUJ` "backdoor" entry point returns the raw EDICT2 lines for every entry
whose writing or reading starts with the search term, e.g.

whose writing or reading starts with the search term, e.g.
"""

import re
from threading import Thread

import requests

from api.custom_types.alternative_string_types import URL, HTMLString, Kaki, Yomi
from api.custom_types.exception_types import APIError
from api.custom_types.response_types import (
    JDictEntry,
    JDictExtraItem,
    JDictMainData,
    JDictSense,
    ResponseItemJDict,
)
from api.utils import remove_end_brackets

NAME = "jdict"


class JDictAPIError(APIError):
    pass


class JDictParsingError(APIError):
    pass


def response_factory(data: JDictMainData | None = None) -> ResponseItemJDict:
    return {
        "success": True,
        "error": None,
        "main_data": {"results": [], "extra": []} if data is None else data,
    }


def error_response_factory(
    error: JDictAPIError | JDictParsingError,
) -> ResponseItemJDict:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "results": [],
            "extra": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemJDict]:
    results_dict: dict[Kaki, ResponseItemJDict] = {}

    def call_script(word: Kaki) -> None:
        results_dict[word] = get_jdict_data(word)

    threads: list[Thread] = [
        Thread(target=call_script, args=[word]) for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return results_dict


def get_jdict_data(word: Kaki) -> ResponseItemJDict:
    try:
        html = get_html_string(word)
    except JDictAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return error_response_factory(api_error)

    try:
        entries = extract_entries(html)
    except JDictParsingError as parsing_error:
        print("An error occurred:", parsing_error.error_msg)
        return error_response_factory(parsing_error)

    data = segregate_entries(entries, word)
    return response_factory(data)


# Get HTML


def get_url(word: Kaki) -> URL:
    url = f"https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ{word}"
    return URL(url)


def get_html_string(word: Kaki) -> HTMLString:
    url = get_url(word)
    try:
        response = requests.get(url, timeout=5)
    except Exception:
        raise JDictAPIError("request failed", 500, url) from None
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = response.text
        raise JDictAPIError(error_msg, status_code, url)

    html = HTMLString(response.text)
    return html


# Extract entries


NO_MATCHES_TEXT = "No matches were found for this key!"


def extract_rows(html: HTMLString) -> list[str]:
    if NO_MATCHES_TEXT in html:
        return []

    cleaning_pattern = r"<pre>(?P<results>.*)</pre>"
    result_search = re.search(cleaning_pattern, html, flags=re.DOTALL)

    if result_search is None:
        raise JDictParsingError(
            status_code=400, error_msg="could not extract results from html"
        )

    full_result: str = result_search["results"]
    return [row for row in full_result.split("\n") if row.strip()]


ROW_PATTERN = r"^(?P<writings>\S+) (\[(?P<readings>\S+)\] )?/(?P<glosses>.*)/$"
MARKER_PATTERN = r"^\((?P<marker>[^()]*)\) "
SENSE_NUMBER_PATTERN = r"^\d+$"
# Bracketed text at the start of a gloss is only a tag if it looks like one
# (`(uk)`, `(exp,v5u)`, `(See 言語)`, `(めがね, メガネ only)`, `(as ...からなる)`),
# otherwise it is part of the definition (`(one's) whereabouts`)
TAG_PATTERN = (
    r"^(\d+|[a-z0-9-]+(,[a-z0-9-]+)*|See .*|.* only"
    r"|(as|after|esp\.|usu\.|oft\.|often|usually|also|orig\.|lit\.|from)\b.*)$"
)


def split_forms(forms: str) -> list[str]:
    """`籠(P);篭(P)` -> `["籠", "篭"]`"""
    return [remove_end_brackets(form) for form in forms.split(";")]


def parse_gloss(gloss: str) -> tuple[list[str], str]:
    """
    Split the leading bracketed markers off a gloss:
    `(n) (1) (uk) glasses` -> `(["n", "1", "uk"], "glasses")`
    """
    markers: list[str] = []
    while (match := re.search(MARKER_PATTERN, gloss)) is not None and re.match(
        TAG_PATTERN, match["marker"]
    ):
        markers.append(match["marker"])
        gloss = gloss[match.end() :]
    return markers, gloss


def build_senses(glosses: list[str]) -> list[JDictSense]:
    """
    Group the glosses of an entry into senses. A sense starts with its parts of
    speech, then (for multi-sense entries) its number, then any other tags:
    `/(n) (1) (uk) glasses/eyeglasses/(n) (2) insight/`
    """
    senses: list[JDictSense] = []

    for gloss in glosses:
        markers, definition = parse_gloss(gloss)
        is_new_sense = not senses or any(
            re.match(SENSE_NUMBER_PATTERN, marker) for marker in markers
        )

        if is_new_sense:
            parts_of_speech: list[str] = []
            tags: list[str] = []
            seen_number = False
            for marker in markers:
                if re.match(SENSE_NUMBER_PATTERN, marker):
                    seen_number = True
                elif seen_number or parts_of_speech:
                    tags.append(marker)
                else:
                    parts_of_speech = marker.split(",")
            senses.append(
                {"parts_of_speech": parts_of_speech, "tags": tags, "definitions": []}
            )
        else:
            senses[-1]["tags"] += [m for m in markers if m not in senses[-1]["tags"]]

        if definition:
            senses[-1]["definitions"].append(definition)

    return senses


def format_row(row: str) -> JDictEntry:
    match = re.search(ROW_PATTERN, row)

    if match is None:
        raise JDictParsingError(
            status_code=400, error_msg="could not extract results from row"
        )

    writings_match: str = match["writings"]
    readings_match: str | None = match["readings"]
    glosses: list[str] = match["glosses"].split("/")

    # Trailing `(P)` marks a common entry, `EntL...` is the entry id
    is_common = "(P)" in writings_match or "(P)" in (readings_match or "")
    glosses = [
        gloss
        for gloss in glosses
        if gloss not in ("", "(P)") and not gloss.startswith("EntL")
    ]

    if readings_match is None:
        # Kana-only entries have no separate reading
        writings: list[Kaki] = []
        readings = [Yomi(x) for x in split_forms(writings_match)]
    else:
        writings = [Kaki(x) for x in split_forms(writings_match)]
        readings = [Yomi(x) for x in split_forms(readings_match)]

    return {
        "writings": writings,
        "readings": readings,
        "is_common": is_common,
        "senses": build_senses(glosses),
    }


def extract_entries(html: HTMLString) -> list[JDictEntry]:
    rows = extract_rows(html)
    return list(map(format_row, rows))


# Build result


def convert_to_extra_item(entry: JDictEntry) -> JDictExtraItem:
    return {"writings": entry["writings"], "readings": entry["readings"]}


def entry_is_matching(entry: JDictEntry, word: Kaki) -> bool:
    return word in entry["writings"] or word in entry["readings"]


def segregate_entries(entries: list[JDictEntry], word: Kaki) -> JDictMainData:
    """Split the (prefix-matched) entries into exact matches and the rest"""
    results: list[JDictEntry] = []
    extra: list[JDictExtraItem] = []

    for entry in entries:
        if entry_is_matching(entry, word):
            results.append(entry)
        else:
            extra.append(convert_to_extra_item(entry))

    return {"results": results, "extra": extra}
