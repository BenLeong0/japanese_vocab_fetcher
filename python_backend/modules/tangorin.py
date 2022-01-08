import json
from threading import Thread
from typing import Optional

from bs4 import BeautifulSoup as Soup
import requests

from custom_types.alternative_string_types import HTMLString, Kaki, URL
from custom_types.exception_types import APIError
from custom_types.response_types import ContextSentence, ResponseItemTangorin


NAME = "tangorin"


class TangorinAPIError(APIError):
    pass


def response_factory(sentence_list: Optional[list[ContextSentence]] = None) -> ResponseItemTangorin:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "sentences": [] if sentence_list is None else sentence_list,
        },
    }


def error_response_factory(error: TangorinAPIError) -> ResponseItemTangorin:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "sentences": [],
        },
    }

TangorinSentenceSection = list[tuple[Soup, Soup]]


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemTangorin]:
    sentences_dict: dict[Kaki, ResponseItemTangorin] = {}

    def call_script(word: Kaki) -> None:
        sentences_dict[word] = get_sentences(word)

    threads: list[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return sentences_dict


def get_sentences(word: Kaki) -> ResponseItemTangorin:
    try:
        html = get_html(word)
    except TangorinAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return error_response_factory(api_error)

    _sentence_sections = get_sections(html)

    return response_factory(None)


# Get HTML

def get_url(word: Kaki) -> URL:
    url = f"https://tangorin.com/sentences?search={word}"
    return URL(url)


def get_html(word: Kaki) -> Soup:
    url = get_url(word)
    response = requests.get(url, timeout=20)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = json.loads(response.text)["error"]
        raise TangorinAPIError(error_msg, status_code, url)

    html = HTMLString(response.text)
    return Soup(html, 'html.parser')


# Extract sections

def get_sections(html: Soup) -> list[TangorinSentenceSection]:
    """Return list of tuples of form `(sentence_ja, sentence_en])`"""
    rows: list[Soup] = list(html.find_all("div", class_="sentences"))
    return [
        (
            Soup(str(row.find('dt', class_='s-jp')), "html.parser"),
            Soup(str(row.find('dd', class_='s-en')), "html.parser")
        ) for row in rows
    ]
