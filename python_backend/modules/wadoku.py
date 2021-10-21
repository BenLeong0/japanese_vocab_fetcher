from collections import defaultdict
import re
from typing import DefaultDict, Dict, List, Tuple

from bs4 import BeautifulSoup as Soup
import requests

from custom_types.alternative_string_types import HTMLString, Kaki, URL, Yomi
from custom_types.exception_types import APIError
from custom_types.response_types import ResponseItemWadoku


NAME = "wadoku"


def response_factory(accent_list: List[Yomi] = None, success: bool = True) -> ResponseItemWadoku:
    if accent_list is None:
        accent_list = []
    return {
        "success": success,
        "main_data": {
            "accent": accent_list,
        },
    }


class WadokuAPIError(APIError):
    pass


WadokuWordSectionsType = List[Tuple[Soup, List[Soup]]]

def main(word_list: List[Kaki]) -> Dict[Kaki, ResponseItemWadoku]:
    if not word_list:
        return {}

    html = get_html(word_list)

    try:
        word_sections = get_sections(html)
    except WadokuAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word: response_factory(success=False) for word in word_list}

    # If first word is invalid, the whole search fails, so try removing first word
    if not word_sections:
        sub_accent_dict = main(word_list[1:])
        sub_accent_dict[word_list[0]] = response_factory()
        return sub_accent_dict

    accent_dict = build_accent_dict(word_sections)

    return {word:response_factory(accent_list=accent_dict[word]) for word in word_list}


# Get HTML

def get_url(word_list: List[Kaki]) -> URL:
    search_param = '%20'.join(word_list)
    url = f"https://www.wadoku.de/search/{search_param}"
    return URL(url)


def get_html(word_list: List[Kaki]) -> Soup:
    url = get_url(word_list)
    html = HTMLString(requests.post(url, timeout=20).text)
    return Soup(html, 'html.parser')


# Extract sections

def get_sections(html: Soup) -> WadokuWordSectionsType:
    """Return list of tuples of form `(writing_section, List[reading_section])`"""
    rows: List[Soup] = list(html.find_all('tr'))
    return [
        (
            Soup(str(row.find('div', class_='japanese')), "html.parser"),
            [Soup(str(span), "html.parser") for span in row.find_all('span', class_='accent')]
        ) for row in rows if row.find('div', class_='japanese') is not None
    ]


def extract_writings(writing_html: Soup) -> List[Kaki]:
    writings = writing_html.text.split('；')
    no_punct_writings = [remove_punct(writing) for writing in writings]
    return list(map(Kaki, no_punct_writings))


def remove_punct(input_string: str) -> str:
    return re.sub(r'[\n￨･~]', '', input_string)


def extract_reading(reading_html: Soup) -> Yomi:
    spans: List[Soup] = [
        span for span in reading_html.findChild().findChildren()
        if remove_punct(span.text) not in ['', '…']
    ]

    if not spans:
        return Yomi("")

    # Initialise with first char
    curr = remove_punct(spans[0].text)
    height = 1 if 't' in spans[0]['class'] else 0

    # Iterate over alternating heights
    for (i, span) in enumerate(spans[1:], start=1):
        if 't' in span['class'] and height == 0:
            if i != 1:
                curr += "* "
            height = 1
        elif 'b' in span['class'] and height == 1:
            curr += "' "
            height = 0

        curr += remove_punct(span.text)

    # Final drop if 尾高
    if 'r' in spans[-1]['class'] and height == 1:
        curr += "'"

    return Yomi(curr)


def build_accent_dict(word_sections: WadokuWordSectionsType) -> DefaultDict[Kaki, List[Yomi]]:
    accent_dict: DefaultDict[Kaki, List[Yomi]] = defaultdict(list)

    for writing_html, reading_htmls in word_sections:
        writings = extract_writings(writing_html)
        readings = [extract_reading(reading_html) for reading_html in reading_htmls]
        for writing in writings:
            accent_dict[writing] += readings

    return accent_dict
