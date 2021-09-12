import re
import requests
from typing import Dict, List

from bs4 import BeautifulSoup as Soup


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    if not word_list:
        return {}

    return {key:[] for key in word_list}


# Get HTML

def get_url(word_list: List[str], page_number: int) -> str:
    search_parameters = '%20'.join(word_list)
    return "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:{}/page:{}".format(
        search_parameters,
        page_number,
    )


def has_words(html_page: Soup) -> bool:
    return len(html_page.find_all("tr", id=re.compile(r"word_\d+"))) > 0


def get_html(word_list: List[str], page_number: int) -> Soup:
    url = get_url(word_list, page_number)
    html_string = requests.post(url, timeout=20).text
    html = Soup(html_string, 'html.parser')
    return html


def get_htmls(word_list: List[str]) -> List[Soup]:
    pages = []
    curr_page_number = 1
    html = get_html(word_list, curr_page_number)
    while has_words(html):
        pages.append(html)
        curr_page_number += 1
        html = get_html(word_list, curr_page_number)
    return pages
