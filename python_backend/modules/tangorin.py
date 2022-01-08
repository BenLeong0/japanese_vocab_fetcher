import json
import re
from threading import Thread
from typing import Optional

from bs4 import BeautifulSoup as Soup
from bs4.element import Tag
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

    sentences = extract_sentences(html)
    response_factory(sentences)
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

def clean_html(html: Soup) -> None:
    """Remove furigana, and insert whitespace"""
    for furigana in html.find_all("rt"):
        furigana.decompose()
    for space in html.find_all("mark"):
        if (
            isinstance(space.nextSibling, Tag) and
            space.nextSibling.name == "mark"
        ):
            space.insert_after(" ")


def extract_sentences(html: Soup) -> list[ContextSentence]:
    """Returns list of ContextSentences"""
    clean_html(html)
    rows: list[Soup] = list(html.find_all("div", class_="sentences"))
    return [
        {
            "ja": re.sub(r'\s+', ' ', row.find('dt', class_='s-jp').text).strip(),
            "en": re.sub(r'\s+', ' ', row.find('dd', class_='s-en').text).strip()
        } for row in rows
    ]
