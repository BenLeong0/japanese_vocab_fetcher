from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple
import urllib

import requests

from bs4 import BeautifulSoup as Soup

from utils import remove_punct


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    if not word_list:
        return {}

    html = get_html(word_list)
    word_sections = get_sections(html)
    accent_dict = build_accent_dict(word_sections)

    return {word:accent_dict[word] for word in word_list}


# Get HTML

def get_url(word_list: List[str]) -> str:
    encoded_word_list = [urllib.parse.quote(word) for word in word_list]
    search_param = '%20'.join(encoded_word_list)
    return f"https://www.wadoku.de/search/{search_param}"


def get_html(word_list: List[str]) -> Soup:
    url = get_url(word_list)
    html = requests.post(url, timeout=20).text
    return Soup(html, 'html.parser')


# Extract sections

def get_sections(html: Soup) -> List[Tuple[Soup, List[Soup]]]:
    rows = [row for row in html.findAll('tr')]
    return [
        (
            Soup(str(row.find('div', class_='japanese')), "html.parser"),
            [Soup(str(span), "html.parser") for span in row.findAll('span', class_='accent')]
        ) for row in rows if row.find('div', class_='japanese') is not None
    ]


def extract_writings(writing_html: Soup) -> List[str]:
    writings = writing_html.text.split('；')
    return [remove_punct(writing) for writing in writings]


def extract_reading(reading_html: Soup) -> str:
    spans: List[Soup] = [
        span for span in reading_html.findChild().findChildren()
        if remove_punct(span.text) != ''
    ]

    if not spans:
        return ''

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

    return curr


def build_accent_dict(word_sections: List[Tuple[Soup, List[Soup]]]) -> DefaultDict:
    accent_dict = defaultdict(list)

    for writing_html, reading_htmls in word_sections:
        writings = extract_writings(writing_html)
        readings = [extract_reading(reading_html) for reading_html in reading_htmls]
        for writing in writings:
            accent_dict[writing] += readings

    return accent_dict
