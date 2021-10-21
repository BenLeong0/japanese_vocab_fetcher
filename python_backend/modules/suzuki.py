from ast import literal_eval
import json
import re
from typing import Dict, List, Tuple, Union

from bs4 import BeautifulSoup as Soup
import requests

from custom_types.alternative_string_types import HTMLString, Kaki, URL, Yomi
from custom_types.exception_types import APIError, api_error_response_factory, FailedResponseItem
from custom_types.response_types import ResponseItemSuzuki
from utils import make_single_line


NAME = "suzuki"
SuzukiModuleReturnTypes = Union[ResponseItemSuzuki, FailedResponseItem]


def response_factory(accent_list: List[Yomi] = None) -> ResponseItemSuzuki:
    if accent_list is None:
        accent_list = []
    return {
        "success": True,
        "main_data": {
            "accent": accent_list,
        },
    }


class SuzukiAPIError(APIError):
    pass


def main(word_list: List[Kaki]) -> Dict[Kaki, SuzukiModuleReturnTypes]:
    if not word_list:
        return {}

    try:
        html = get_html(word_list)
    except SuzukiAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word : api_error_response_factory(api_error) for word in word_list}

    word_sections = get_sections(html)
    accent_dict = build_accent_dict(word_sections)

    return {word : response_factory(accent_list=accent_dict[word]) for word in word_list}


# Get HTML

def get_formdata(word_list: List[Kaki]) -> Dict[str, str]:
    words_with_particles = [word + 'は' for word in word_list]
    formdata = {
        "data[Phrasing][curve]": "advanced",
        "data[Phrasing][accent]": "advanced",
        "data[Phrasing][accent_mark]": "all",
        "data[Phrasing][estimation]": "crf",
        "data[Phrasing][analyze]": "true",
        "data[Phrasing][phrase_component]": "invisible",
        "data[Phrasing][param]": "invisible",
        "data[Phrasing][subscript]": "visible",
    }
    formdata["data[Phrasing][text]"] = "\n".join(words_with_particles)
    return formdata


def get_html(word_list: List[Kaki]) -> Soup:
    url = URL('http://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index')
    formdata = get_formdata(word_list)
    response = requests.post(url, formdata, timeout=20)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = json.loads(response.text)["error"]
        raise SuzukiAPIError(error_msg, status_code, url)

    html = HTMLString(response.text)
    return Soup(html, 'html.parser')


# Extract sections

def get_sections(html: Soup) -> List[Tuple[Soup, Soup, Soup]]:
    """Return list of tuples of form `(writing_section, reading_section, accent_section)`"""
    rows: List[Soup] = list(html.find_all('div', class_='phrasing_phrase_wrapper'))
    return [
        (
            Soup(str(row.find('div', class_='phrasing_subscript')), "html.parser"),
            Soup(str(row.find('div', class_='phrasing_text')), "html.parser"),
            Soup(make_single_line(str(row.find('script'))), "html.parser")
        ) for row in rows if row.find('div', class_='phrasing_subscript') is not None
    ]


def extract_writing(writing_html: Soup) -> Kaki:
    full_writing: str = re.sub(r'\s', '', writing_html.text)
    writing_without_final_ha = full_writing[:-1]
    return Kaki(writing_without_final_ha)


def extract_characters(reading_html: Soup) -> str:
    full_reading: str = re.sub(r'\s', '', reading_html.text)
    reading_without_final_ha = full_reading[:-1]
    return reading_without_final_ha


def extract_accent_pattern(accent_html: Soup) -> List[int]:
    accent_array_regex = r'\[.*?\]'
    accent_match = re.search(accent_array_regex, str(accent_html))

    if accent_match is None:
        raise Exception("Accent not found")

    heights: List[int] = literal_eval(accent_match.group())
    return heights


def contruct_reading(chars: str, accent_pattern: List[int]) -> Yomi:
    if not chars:
        return Yomi("")
    mini_chars = 'ゃょゅぁぃぅぇぉゎャュョァィゥェォヮ'
    accented_word = ''
    curr_height = accent_pattern[0]
    for (i, height) in enumerate(accent_pattern[1:]):
        accented_word += chars[i]
        if (
            curr_height == 0 and
            height == 1 and
            i != 0 and
            (i != 1 or chars[i] not in mini_chars)
        ):
            # If valid pitch accent rise, not after first mora
            accented_word += "* "
        elif curr_height == 1 and height == 0:
            accented_word += "' "
        curr_height = height

    if accented_word[-1] == ' ':
        accented_word = accented_word[:-1]
    return Yomi(accented_word)


def extract_reading(reading_html: Soup, accent_html: Soup) -> Yomi:
    chars = extract_characters(reading_html)
    accent_pattern = extract_accent_pattern(accent_html)
    return contruct_reading(chars, accent_pattern)


def build_accent_dict(word_sections: List[Tuple[Soup, Soup, Soup]]) -> Dict[Kaki, List[Yomi]]:
    accent_dict: Dict[Kaki, List[Yomi]] = {}

    for writing_html, reading_html, accent_html in word_sections:
        writing = extract_writing(writing_html)
        reading = extract_reading(reading_html, accent_html)
        accent_dict[writing] = [reading] if reading else []

    return accent_dict
