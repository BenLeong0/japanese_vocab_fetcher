from collections import defaultdict
from typing import Dict, List, Tuple

import requests

from bs4 import BeautifulSoup
from bs4.element import PageElement

from utils import remove_punct


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    if not word_list:
        return defaultdict(list)

    single = len(word_list) == 1
    html_sections = get_html_sections(word_list, single=single)
    accent_dict = build_accent_dict(html_sections, single=single)
    return accent_dict


# Get HTML Sections

def get_url(word_list: List[str]) -> str:
    search_param = '%20'.join(word_list)
    return f"https://www.wadoku.de/search/{search_param}"


def get_html_sections(word_list: List[str], single_word: bool = False) -> List[BeautifulSoup]:
    url = get_url(word_list)
    html = requests.post(url, timeout=20).text
    soup = BeautifulSoup(html, 'html.parser')
    return extract_sections(soup, single=single_word)


def extract_sections(soup: BeautifulSoup, single: bool = False) -> List[PageElement]:
    table_rows = [BeautifulSoup(str(x)) for x in soup.findAll('tr')]
    if single:
        return table_rows

    sections: list[PageElement] = []
    for row in table_rows:
        if not row.has_attr('class'):
            sections.append(row)
        else:
            sections[-1].append(row)

    return [BeautifulSoup(str(x)) for x in sections]


# Build accent dict mult

def build_accent_dict(
    html_sections: List[BeautifulSoup],
    single: bool = False,
) -> Dict[str, List[str]]:
    if single:
        extract_subsections = extract_subsections_single
        extract_kakikata = extract_kakikata_single
        extract_yomikata = extract_yomikata_single
    else:
        extract_subsections = extract_subsections_multiple
        extract_kakikata = extract_kakikata_multiple
        extract_yomikata = extract_yomikata_multiple

    accent_dict = defaultdict(list)
    for section in html_sections:
        writing_sections, reading_sections = extract_subsections(html_sections)
        writing = extract_kakikata(section)
        accents = extract_yomikata(section)
        accent_dict[writing] = accents

    return accent_dict


def extract_kakikata_single(section: BeautifulSoup) -> str:
    midashi_section: BeautifulSoup = section.find('th', class_='focalPhrase')
    if midashi_section is None:
        return ''
    return midashi_section.text.strip()


def extract_kakikata_multiple(section: BeautifulSoup) -> str:
    midashi_section: BeautifulSoup = section.find('th', class_='focalPhrase')
    if midashi_section is None:
        return ''
    return midashi_section.text.strip()


def extract_yomikata_single(section: BeautifulSoup) -> List[str]:
    return [str(section)]


def extract_yomikata_multiple(section: BeautifulSoup) -> List[str]:
    accent_sections: list[BeautifulSoup] = section.find_all('span', class_='accent')

    accents: set[str] = set()
    for accent in accent_sections:
        spans: list[BeautifulSoup] = [span for span in accent.children if span != '…']

        # Initialise with first char
        curr = remove_punct(spans[0].text)
        if 't' in spans[0]['class']:
            if 'r' in spans[0]:
                curr += "' "
                H = 0
            H = 1
        else: H = 0

        # Iterate over alternating heights
        for (i, span) in enumerate(spans[1:], start=1):
            if 't' in span['class'] and H == 0:
                if i != 1: curr += "* "
                H = 1
            elif 'b' in span['class'] and H == 1:
                curr += "' "
                H = 0

            curr += remove_punct(span.text)

        # Final drop if 尾高
        if 'r' in spans[-1]['class'] and H == 1:
            curr += "'"

        accents.add(curr)

    return list(accents)


# Build accent dict single


def extract_subsections_single(section: BeautifulSoup) -> Tuple(BeautifulSoup, BeautifulSoup):
    writing_sections = section.find('span', class_='accent')

def extract_subsections_multiple(section: BeautifulSoup) -> Tuple(BeautifulSoup, BeautifulSoup):
    writing_sections = section.find('span', class_='accent')
