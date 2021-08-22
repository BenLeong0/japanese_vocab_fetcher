from collections import defaultdict
from typing import Dict, List

import requests

from bs4 import BeautifulSoup
from bs4.element import ResultSet

from utils import remove_punct


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    html_sections = get_html_sections(word_list)
    accent_dict = build_accent_dict(html_sections)
    print(accent_dict)
    return accent_dict


# Get HTML Sections

def get_url(word_list: List[str]) -> str:
    search_param = '%20'.join(word_list)
    return f"https://www.wadoku.de/search/{search_param}"


def get_html_sections(word_list) -> BeautifulSoup:
    url = get_url(word_list)
    html = requests.post(url, timeout=20).text
    soup = BeautifulSoup(html, 'html.parser')
    return extract_sections(soup)


def extract_sections(soup: BeautifulSoup) -> List[BeautifulSoup]:
    table_rows: ResultSet = soup.findAll('tr')
    sections: list[BeautifulSoup] = ['']
    print(table_rows[0])
    for row in table_rows:
        if not row.has_attr('class'):
            sections.append(str(row))
        else:
            sections[-1] += str(row)

    return [BeautifulSoup(section, 'html.parser') for section in sections]


# Build accent dict

def build_accent_dict(html_sections: List[BeautifulSoup]) -> Dict[str, List[str]]:
    accent_dict = defaultdict(list)
    for section in html_sections:
        writing = extract_kakikata(section)
        accents = extract_yomikata(section)
        accent_dict[writing] = accents
    return accent_dict


def extract_kakikata(section: BeautifulSoup) -> str:
    midashi_section: BeautifulSoup = section.find('th', class_='focalPhrase')
    if midashi_section is None:
        return ''
    return midashi_section.text.strip()


def extract_yomikata(section: BeautifulSoup) -> List[str]:
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
