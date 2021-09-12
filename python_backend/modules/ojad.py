import re
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup as Soup
from bs4.element import PageElement
import requests


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


def get_rows(html_page: Soup) -> List[PageElement]:
    return html_page.find_all("tr", id=re.compile(r"word_\d+"))


def has_words(html_page: Soup) -> bool:
    return len(get_rows(html_page)) > 0


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


# Extract sections

def get_sections(htmls: List[Soup]) -> List[Tuple[Soup, List[Soup]]]:
    rows = sum(map(get_rows, htmls), [])
    return [
        (
            Soup(str(row.find('td', class_='midashi')), "html.parser"),
            [
                Soup(str(proc), "html.parser") for proc in
                row.find('td', class_='katsuyo_jisho_js').findAll('div', class_="katsuyo_proc")
            ]
        ) for row in rows
    ]


def extract_writings(writing_html: Soup) -> List[str]:
    midashi: str = writing_html.find('p', class_='midashi_word').text
    writings = midashi.split('・')
    # eg 綺麗[な] -> 綺麗
    filtered_writings = [re.search(r'[^\[]*', writing).group() for writing in writings]
    return filtered_writings


def extract_reading(reading_html: Soup) -> str:
    # 拗音 get their own span already!
    contents: Soup = reading_html.find("span", class_="accented_word")
    chars: List[str] = [span.text for span in contents]
    classes: List[List[str]] = [span['class'] for span in contents]

    reading = ''
    for (char, class_list) in zip(chars, classes):
        reading += char
        if 'accent_top' in class_list:
            reading += "' "

    if reading[-1] == " ":
        reading = reading[:-1]
    return reading

