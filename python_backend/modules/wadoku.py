from collections import defaultdict
from typing import DefaultDict, Dict, List, Set, Tuple

import requests

from bs4 import BeautifulSoup as Soup
from bs4.element import PageElement

from utils import remove_punct


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    if not word_list:
        return {}

    html = get_html(word_list)
    word_sections = get_sections(html, word_list)
    # accent_dict = build_accent_dict(html_sections, single=single)
    # return accent_dict
    # return {key:accent_dict[key] for key in word_list}


# Get HTML

def get_url(word_list: List[str]) -> str:
    search_param = '%20'.join(word_list)
    return f"https://www.wadoku.de/search/{search_param}"


def get_html(word_list: List[str]) -> Soup:
    url = get_url(word_list)
    html = requests.post(url, timeout=20).text
    return Soup(html, 'html.parser')


# Extract sections

def get_sections(html: Soup) -> List[Tuple[Soup, Soup]]:
    rows = [Soup(row) for row in html.findAll('tr')]
    return [
        (Soup(row.find('div', class_='japanese')), Soup(row.find('div', class_='accent')))
        for row in rows
    ]


def extract_sections(soup: Soup, single: bool = False) -> List[PageElement]:
    table_rows = [Soup(str(x), 'html.parser') for x in soup.findAll('tr')]
    if single:
        return table_rows

    sections: List[PageElement] = []
    for row in table_rows:
        if not row.has_attr('class'):
            sections.append(row)
        else:
            sections[-1].append(row)

    return [Soup(str(x)) for x in sections]


# Build accent dict mult

def build_accent_dict(
    html_sections: List[Soup],
    single: bool = False,
) -> DefaultDict[str, List[str]]:
    if single:
        extract_subsections = extract_subsections_single
        extract_kakikata = extract_kakikata_single
        extract_yomikata = extract_yomikata_single
    else:
        extract_subsections = extract_subsections_mult
        extract_kakikata = extract_kakikata_multiple
        extract_yomikata = extract_yomikata_multiple

    accent_dict = defaultdict(list)
    for section in html_sections:
        writing_sections, reading_sections = extract_subsections(section)
        writing = extract_kakikata(writing_sections)
        accents = extract_yomikata(reading_sections)
        accent_dict[writing] = accents

    return accent_dict


def extract_kakikata_single(section: Soup) -> str:
    midashi_section: Soup = section.find('th', class_='focalPhrase')
    if midashi_section is None:
        return ''
    return midashi_section.text.strip()


def extract_kakikata_multiple(section: Soup) -> str:
    midashi_section: Soup = section.find('th', class_='focalPhrase')
    if midashi_section is None:
        return ''
    return midashi_section.text.strip()


def extract_yomikata_single(section: List[Soup]) -> List[str]:
    print([reading.text.strip() for reading in section])
    return [reading.text.strip() for reading in section]


def extract_yomikata_multiple(section: Soup) -> List[str]:
    # TODO: Check if NO ACCENT!
    accent_sections: List[Soup] = section.find_all('span', class_='accent')

    accents: Set[str] = set()
    for accent in accent_sections:
        spans: List[Soup] = [span for span in accent.children if span != '…']

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


def extract_subsections_single(section: Soup) -> Tuple[Soup, List[Soup]]:
    """Returns a tuple (writing_section, reading_sections)"""
    writing_sections = section.find('div', class_='japanese')
    reading_sections = section.findAll('span', class_='accent')
    return writing_sections, reading_sections

def extract_subsections_mult(section: Soup) -> Tuple[Soup, List[Soup]]:
    """Returns a tuple (writing_section, reading_sections)"""
    writing_sections = section.find('span', class_='accent')
    return writing_sections, writing_sections
