from itertools import product
import re
from threading import Thread
from typing import Optional

import requests

from custom_types.alternative_string_types import HTMLString, Kaki, URL, Yomi
from custom_types.exception_types import APIError
from custom_types.response_types import JapanesePodAudio, ResponseItemJapanesePod
from utils import remove_end_brackets


NAME = "japanesepod"


class JapanesePodAPIError(APIError):
    pass

class JapanesePodParsingError(APIError):
    pass


def response_factory(
    audio_list: Optional[list[JapanesePodAudio]] = None,
) -> ResponseItemJapanesePod:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "audio": [] if audio_list is None else audio_list,
        },
    }


def error_response_factory(
    error: JapanesePodAPIError | JapanesePodParsingError,
) -> ResponseItemJapanesePod:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "audio": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemJapanesePod]:
    audio_dict: dict[Kaki, ResponseItemJapanesePod] = {}

    def call_script(word: Kaki) -> None:
        audio_dict[word] = get_audio_urls(word)

    threads: list[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return audio_dict


def get_audio_urls(word: Kaki) -> ResponseItemJapanesePod:
    try:
        html = get_html_string(word)
    except JapanesePodAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return error_response_factory(api_error)

    try:
        results = extract_results(html)
    except JapanesePodParsingError as parsing_error:
        print("An error occurred:", parsing_error.error_msg)
        return error_response_factory(parsing_error)

    filtered_results = filter_results(results, word)
    potential_urls = generate_audio_urls(filtered_results)
    print(potential_urls)

    return response_factory()


# Get HTML

def get_url(word: Kaki) -> URL:
    url = f"https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ{word}"
    return URL(url)


def get_html_string(word: Kaki) -> HTMLString:
    url = get_url(word)
    response = requests.get(url, timeout=20)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = response.text
        raise JapanesePodAPIError(error_msg, status_code, url)

    html = HTMLString(response.text)
    return html


# Extract results

def extract_rows(html: HTMLString) -> list[str]:
    cleaning_pattern = r"<pre>(?P<results>.*)</pre>"
    result_search = re.search(cleaning_pattern, html, flags=re.DOTALL)

    if result_search is None:
        raise JapanesePodParsingError(
            status_code=400,
            error_msg="could not extract results from html"
        )

    full_result: str = result_search['results']
    return [x for x in full_result.split("\n") if x]    # Filter out "empty" rows (first and last)


def extract_matches_from_row_string(row: str) -> tuple[str, Optional[str]]:
    """Takes in a row string, return a tuple of the form `writings, readings`"""
    pattern = r"^(?P<writings>[^\s]+) (\[(?P<readings>[^\s]+)\] )?"
    match = re.search(pattern, row)

    if match is None:
        raise JapanesePodParsingError(
            status_code=400,
            error_msg="could not extract results from row"
        )

    writings_match: str = match['writings']
    readings_match: Optional[str] = match['readings']

    return (writings_match, readings_match)


def build_row_result_from_matches(
    writings_match: str,
    readings_match: Optional[str]
) -> tuple[list[Kaki], list[Yomi]]:
    readings_match = writings_match if readings_match is None else readings_match

    writings = [Kaki(remove_end_brackets(x)) for x in writings_match.split(";")]
    readings = [Yomi(remove_end_brackets(x)) for x in readings_match.split(";")]

    return (writings, readings)


def format_row(row: str) -> tuple[list[Kaki], list[Yomi]]:
    writings_match, readings_match = extract_matches_from_row_string(row)
    writings, readings = build_row_result_from_matches(writings_match, readings_match)
    return (writings, readings)


def extract_results(html: HTMLString) -> list[tuple[list[Kaki], list[Yomi]]]:
    rows = extract_rows(html)
    formatted_rows = list(map(format_row, rows))
    return formatted_rows


# Audio urls

def filter_results(
    results: list[tuple[list[Kaki], list[Yomi]]],
    word: Kaki,
) -> list[tuple[list[Kaki], list[Yomi]]]:
    return list(filter(lambda result: word in result[0], results))


def generate_audio_urls(
    results: list[tuple[list[Kaki], list[Yomi]]]
) -> list[tuple[Kaki, Yomi, URL]]:
    base_url = "https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kanji={}&kana={}"
    return sum([
        [(k, y, URL(base_url.format(k, y))) for k, y in product(*res)]
        for res in results
    ], [])
