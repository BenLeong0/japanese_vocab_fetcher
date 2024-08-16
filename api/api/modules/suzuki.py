import re
from ast import literal_eval
from typing import Optional

import requests
from bs4 import BeautifulSoup as Soup

from api.custom_types.alternative_string_types import URL, HTMLString, Kaki, Yomi
from api.custom_types.exception_types import APIError
from api.custom_types.response_types import ResponseItemSuzuki
from api.utils import make_single_line

NAME = "suzuki"


class SuzukiAPIError(APIError):
    pass


def response_factory(accent_list: Optional[list[Yomi]] = None) -> ResponseItemSuzuki:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "accent": [] if accent_list is None else accent_list,
        },
    }


def error_response_factory(error: SuzukiAPIError) -> ResponseItemSuzuki:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "accent": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemSuzuki]:
    if not word_list:
        return {}

    try:
        html = get_html(word_list)
    except SuzukiAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word: error_response_factory(api_error) for word in word_list}

    word_sections = get_sections(html)
    accent_dict = build_accent_dict(word_sections)

    return {word: response_factory(accent_list=accent_dict[word]) for word in word_list}


# Get HTML


def get_formdata(word_list: list[Kaki]) -> dict[str, str]:
    words_with_particles = [word + "は" for word in word_list]
    text = "\n".join(words_with_particles)
    formdata = {
        "_method": "POST",
        "data[Phrasing][text]": text,
        "data[Phrasing][curve]": "advanced",
        "data[Phrasing][accent]": "advanced",
        "data[Phrasing][accent_mark]": "all",
        "data[Phrasing][estimation]": "crf",
        "data[Phrasing][analyze]": "true",
        "data[Phrasing][phrase_component]": "invisible",
        "data[Phrasing][param]": "invisible",
        "data[Phrasing][subscript]": "visible",
        "data[Phrasing][jeita]": "invisible",
    }
    return formdata


def get_html(word_list: list[Kaki]) -> Soup:
    url = URL("https://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index")
    formdata = get_formdata(word_list)
    try:
        response = requests.post(url, formdata, timeout=20)
    except Exception:
        raise SuzukiAPIError("request failed", 500, url) from None
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = response.text
        raise SuzukiAPIError(error_msg, status_code, url)

    html = HTMLString(response.text)
    return Soup(html, "html.parser")


# Extract sections


def get_sections(html: Soup) -> list[tuple[Soup, Soup, Soup]]:
    """
    Return list of tuples of form `(writing_section, reading_section, accent_section)`
    """
    rows: list[Soup] = list(html.find_all("div", class_="phrasing_phrase_wrapper"))
    return [
        (
            Soup(str(row.find("div", class_="phrasing_subscript")), "html.parser"),
            Soup(str(row.find("div", class_="phrasing_text")), "html.parser"),
            Soup(make_single_line(str(row.find("script"))), "html.parser"),
        )
        for row in rows
        if row.find("div", class_="phrasing_subscript") is not None
    ]


def extract_writing(writing_html: Soup) -> Kaki:
    full_writing: str = re.sub(r"\s", "", writing_html.text)
    writing_without_final_ha = full_writing[:-1]
    return Kaki(writing_without_final_ha)


def extract_characters(reading_html: Soup) -> str:
    full_reading: str = re.sub(r"\s", "", reading_html.text)
    reading_without_final_ha = full_reading[:-1]
    return reading_without_final_ha


def extract_accent_pattern(accent_html: Soup) -> list[int]:
    accent_array_regex = r"\[.*?\]"
    accent_match = re.search(accent_array_regex, str(accent_html))

    if accent_match is None:
        raise Exception("Accent not found")

    heights: list[int] = literal_eval(accent_match.group())
    return heights


def contruct_reading(chars: str, accent_pattern: list[int]) -> Yomi:
    if not chars:
        return Yomi("")
    mini_chars = "ゃょゅぁぃぅぇぉゎャュョァィゥェォヮ"
    accented_word = ""
    curr_height = accent_pattern[0]
    for i, height in enumerate(accent_pattern[1:]):
        accented_word += chars[i]
        if (
            curr_height == 0
            and height == 1
            and i != 0
            and (i != 1 or chars[i] not in mini_chars)
        ):
            # If valid pitch accent rise, not after first mora
            accented_word += "* "
        elif curr_height == 1 and height == 0:
            accented_word += "' "
        curr_height = height

    if accented_word[-1] == " ":
        accented_word = accented_word[:-1]
    return Yomi(accented_word)


def extract_reading(reading_html: Soup, accent_html: Soup) -> Yomi:
    chars = extract_characters(reading_html)
    accent_pattern = extract_accent_pattern(accent_html)
    return contruct_reading(chars, accent_pattern)


def build_accent_dict(
    word_sections: list[tuple[Soup, Soup, Soup]],
) -> dict[Kaki, list[Yomi]]:
    accent_dict: dict[Kaki, list[Yomi]] = {}

    for writing_html, reading_html, accent_html in word_sections:
        writing = extract_writing(writing_html)
        reading = extract_reading(reading_html, accent_html)
        accent_dict[writing] = [reading] if reading else []

    return accent_dict
