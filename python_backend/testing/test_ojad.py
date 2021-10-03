from functools import partial
import re
from typing import List

from bs4 import BeautifulSoup as Soup
import pytest   # type: ignore

from modules import ojad
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the wadoku info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    htmls = test_dict['ojad']['htmls']
    expected_output = test_dict['ojad']['expected_output']

    monkeypatch.setattr("requests.post", partial(_get_ojad_html_string, htmls=htmls))
    assert ojad.main(word_list) == expected_output


def _get_ojad_html_string(url: str, htmls: List[Soup], timeout: int = 20) -> FakeResponse:
    """Given a url return the corresponding (test) html, or a blank page if out of range"""
    page_number_match = re.search(r"page:\d+", url)

    if not page_number_match:
        raise Exception("Page number not found")

    page_number = int(page_number_match.group()[5:])
    if page_number > len(htmls):
        with open("testing/html_files/ojad_BLANK.html", encoding="utf8") as file:
            return FakeResponse(str(file))
    return FakeResponse(htmls[page_number - 1])


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns an empty dict
    """
    assert ojad.main([]) == {}


@pytest.mark.parametrize("page_number", [1,2,3,10,100])
def test_get_url(test_dict: FullTestDict, page_number: int):
    """
    - GIVEN a list of words and a page number
    - WHEN the url is generated
    - THEN test it is returns the expected url
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_url = test_dict['ojad']['url'] % page_number

    assert ojad.get_url(word_list, page_number) == expected_url


def test_has_words_true(test_dict: FullTestDict):
    """
    - GIVEN an html file
    - WHEN it is tested whether it contains words
    - THEN return true when it should
    """
    htmls = test_dict['ojad']['htmls']
    for html in htmls:
        parsed_html = Soup(html, "html.parser")
        assert ojad.has_words(parsed_html) == True


def test_has_words_false():
    """
    - GIVEN an empty html file
    - WHEN it is tested whether it contains words
    - THEN return false when it should
    """
    with open("testing/html_files/ojad_BLANK.html", encoding="utf8") as file:
        html = Soup(file, 'html.parser')

    assert ojad.has_words(html) == False


def test_get_htmls(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the respective pages are collected
    - THEN check they are all collected, and that the loop terminates
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    htmls = test_dict['ojad']['htmls']
    monkeypatch.setattr("requests.post", partial(_get_ojad_html_string, htmls=htmls))

    assert ojad.get_htmls(word_list) == [Soup(html, "html.parser") for html in htmls]


def test_get_sections(test_dict: FullTestDict):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct
    """
    htmls = test_dict['ojad']['htmls']
    parsed_htmls = [Soup(html, "html.parser") for html in htmls]
    expected_sections = test_dict['ojad']['expected_sections']

    assert ojad.get_sections(parsed_htmls) == [
        (section['writing_section'], section['reading_sections'])
        for section in expected_sections
    ]


def test_extract_writings(test_dict: FullTestDict):
    """
    - GIVEN writing sections
    - WHEN the writings are extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['ojad']['expected_sections']:
        assert ojad.extract_writings(section['writing_section']) == section['writings']


def test_extract_reading(test_dict: FullTestDict):
    """
    - GIVEN reading sections
    - WHEN the readings are extracted
    - THEN check all the correct readings are extracted
    """
    for section in test_dict['ojad']['expected_sections']:
        for html_section, reading in zip(section['reading_sections'], section['readings']):
            na_adj = "na_adj" in section and section["na_adj"] is True
            assert ojad.extract_reading(html_section, na_adj) == reading


def test_build_accent_dict(test_dict: FullTestDict):
    """
    - GIVEN html sections
    - WHEN the accent dict is constructed
    - THEN check all the values are as expected
    """
    word_sections = [
        (section['writing_section'], section['reading_sections'])
        for section in test_dict['ojad']['expected_sections']
    ]

    assert ojad.build_accent_dict(word_sections) == test_dict['ojad']['full_accent_dict']
