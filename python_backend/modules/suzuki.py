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
