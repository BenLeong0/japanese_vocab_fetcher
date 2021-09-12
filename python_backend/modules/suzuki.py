import re
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup as Soup
import requests

from utils import make_single_line


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    if not word_list:
        return {}

    html = get_html(word_list)
    word_sections = get_sections(html)
    # accent_dict = build_accent_dict(word_sections)

    return {word:[] for word in word_list}


# Get HTML

def get_formdata(word_list: List[str]) -> Dict[str, str]:
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


def get_html(word_list: List[str]) -> Soup:
    url = 'http://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing/index'
    formdata = get_formdata(word_list)
    html = requests.post(url, formdata, timeout=20).text
    return Soup(html, 'html.parser')


# Extract sections

def get_sections(html: Soup) -> List[Tuple[Soup, List[Soup]]]:
    rows = [row for row in html.findAll('div', class_='phrasing_phrase_wrapper')]
    return [
        (
            Soup(str(row.find('div', class_='phrasing_subscript')), "html.parser"),
            Soup(str(row.find('div', class_='phrasing_text')), "html.parser"),
            Soup(make_single_line(str(row.find('script'))), "html.parser")
        ) for row in rows if row.find('div', class_='phrasing_subscript') is not None
    ]


def extract_writing(writing_html: Soup) -> str:
    full_writing = re.sub('\s', '', writing_html.text)
    writing_without_final_ha = full_writing[:-1]
    return writing_without_final_ha


def extract_characters(reading_html: Soup) -> str:
    full_reading = re.sub('\s', '', reading_html.text)
    reading_without_final_ha = full_reading[:-1]
    return reading_without_final_ha


def extract_accent_pattern(accent_html: Soup) -> List[int]:
    accent_array_regex = r'\[.*?\]'
    accent_pattern = eval(re.search(accent_array_regex, str(accent_html)).group())
    return accent_pattern


def contruct_reading(chars: str, accent_pattern: List[int]) -> str:
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
    return accented_word


def extract_reading(reading_html: Soup, accent_html: Soup) -> str:
    chars = extract_characters(reading_html)
    accent_pattern = extract_accent_pattern(accent_html)
    return contruct_reading(chars, accent_pattern)


def build_accent_dict(word_sections: List[Tuple[Soup, List[Soup]]]) -> Dict:
    accent_dict = {}

    for writing_html, reading_html, accent_html in word_sections:
        writing = extract_writing(writing_html)
        reading = extract_reading(reading_html, accent_html)
        accent_dict[writing] = [reading]

    return accent_dict
