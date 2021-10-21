from collections import defaultdict
import json
import re
from typing import DefaultDict, Dict, List, Tuple, Union

from bs4 import BeautifulSoup as Soup
import requests

from custom_types.alternative_string_types import HTMLString, Kaki, URL, Yomi
from custom_types.exception_types import APIError, api_error_response_factory, FailedResponseItem
from custom_types.response_types import ResponseItemOJAD


NAME = "ojad"
OJADModuleReturnTypes = Union[ResponseItemOJAD, FailedResponseItem]


def response_factory(accent_list: List[Yomi] = None, success: bool = True) -> ResponseItemOJAD:
    if accent_list is None:
        accent_list = []
    return {
        "success": success,
        "main_data": {
            "accent": accent_list,
        },
    }


class OJADAPIError(APIError):
    pass


OJADWordSectionsType = List[Tuple[Soup, List[Soup]]]


def main(word_list: List[Kaki]) -> Dict[Kaki, OJADModuleReturnTypes]:
    if not word_list:
        return {}

    try:
        htmls = get_htmls(word_list)
    except OJADAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word : api_error_response_factory(api_error) for word in word_list}

    word_sections = get_sections(htmls)
    accent_dict = build_accent_dict(word_sections)

    return {word : response_factory(accent_dict[word]) for word in word_list}


# Get HTML

def get_url(word_list: List[Kaki], page_number: int) -> URL:
    search_parameters = '%20'.join(word_list)
    url = "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:{}/page:{}".format(
        search_parameters,
        page_number,
    )
    return URL(url)


def get_rows(html_page: Soup) -> List[Soup]:
    return list(html_page.find_all("tr", id=re.compile(r"word_\d+")))


def has_words(html_page: Soup) -> bool:
    return len(get_rows(html_page)) > 0


def get_html(word_list: List[Kaki], page_number: int) -> Soup:
    url = get_url(word_list, page_number)
    response = requests.post(url, timeout=20)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = json.loads(response.text)["error"]
        raise OJADAPIError(error_msg, status_code, url)

    html_string = HTMLString(response.text)
    html = Soup(html_string, 'html.parser')
    return html


def get_htmls(word_list: List[Kaki]) -> List[Soup]:
    pages: List[Soup] = []
    curr_page_number = 1
    html = get_html(word_list, curr_page_number)
    while has_words(html):
        pages.append(html)
        curr_page_number += 1
        html = get_html(word_list, curr_page_number)
    return pages


# Extract sections

def get_sections(htmls: List[Soup]) -> OJADWordSectionsType:
    """Return list of tuples of form `(writing_section, reading_section)`"""
    rows: List[Soup] = sum(map(get_rows, htmls), [])
    return [
        (
            Soup(str(row.find('td', class_='midashi')), "html.parser"),
            [
                Soup(str(proc), "html.parser") for proc in
                row.find('td', class_='katsuyo_jisho_js').find_all('div', class_="katsuyo_proc")
            ]
        ) for row in rows
    ]


def extract_writings(writing_html: Soup) -> List[Kaki]:
    midashi: str = writing_html.find('p', class_='midashi_word').text
    writings = midashi.split('・')
    # eg 綺麗[な] -> 綺麗
    filtered_writings = [writing.replace('[な]', '') for writing in writings]
    return list(map(Kaki, filtered_writings))


def extract_reading(reading_html: Soup, na_adj: bool) -> Yomi:
    # 拗音 get their own span already!
    contents: Soup = reading_html.find("span", class_="accented_word")
    chars: List[str] = [span.text for span in contents]
    classes: List[List[str]] = [span['class'] for span in contents]

    reading = ''
    for (char, class_list) in zip(chars, classes):
        reading += char
        if 'accent_top' in class_list:
            reading += "' "

    if na_adj and reading[-1] == "な":
        reading = reading[:-1]
    if reading[-1] == " ":
        reading = reading[:-1]
    return Yomi(reading)


def build_accent_dict(word_sections: OJADWordSectionsType) -> DefaultDict[Kaki, List[Yomi]]:
    accent_dict: DefaultDict[Kaki, List[Yomi]] = defaultdict(list)

    for writing_html, reading_htmls in word_sections:
        writings = extract_writings(writing_html)
        na_adj = '[な]' in writing_html.text
        readings = [extract_reading(reading_html, na_adj=na_adj) for reading_html in reading_htmls]
        for writing in writings:
            accent_dict[writing] += readings

    return accent_dict
