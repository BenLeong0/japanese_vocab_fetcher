from functools import partial
import pytest
import re
from typing import List

from bs4 import BeautifulSoup as Soup

from modules import ojad
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


def _get_ojad_html_string(url: str, htmls: List[Soup], timeout: int = 20) -> str:
    page_number = int(re.search(r"page:\d+", url).group()[5:])
    if page_number > len(htmls):
        with open("testing/html_files/ojad_BLANK.html") as file:
            return FakeResponse(str(file))
    return FakeResponse(htmls[page_number - 1])


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert ojad.get_accent_dict([]) == {}


@pytest.mark.parametrize("page_number", [1,2,3,10,100])
def test_get_url(test_dict: FullTestDict, page_number: int):
    """
    - GIVEN a list of words and a page number
    - WHEN the url is generated
    - THEN test it is as expected
    """
    word_list = test_dict['input']
    expected_url = test_dict['ojad']['url'] % page_number

    assert ojad.get_url(word_list, page_number) == expected_url


def test_has_words_true(test_dict: FullTestDict):
    """
    - GIVEN an html file
    - WHEN it is tested whether it contains words
    - THEN return true when it does
    """
    htmls = test_dict['ojad']['htmls']
    for html in htmls:
        parsed_html = Soup(html, "html.parser")
        assert ojad.has_words(parsed_html) == True


def test_has_words_false():
    """
    - GIVEN an empty html file
    - WHEN it is tested whether it contains words
    - THEN return false, as it doesn't
    """
    with open("testing/html_files/ojad_BLANK.html") as file:
        html = Soup(file, 'html.parser')

    assert ojad.has_words(html) == False


def test_get_htmls(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the respective pages are collected
    - THEN check they are all collected, and the loop terminates
    """
    word_list = test_dict['input']
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


# def test_extract_writing(test_dict: FullTestDict):
#     """
#     - GIVEN an html sections
#     - WHEN the writing is extracted
#     - THEN check all the correct writings are extracted
#     """
#     for section in test_dict['ojad']['expected_sections']:
#         assert ojad.extract_writing(section['writing_section']) == section['writing']


# def test_extract_reading(test_dict: FullTestDict):
#     """
#     - GIVEN an html sections
#     - WHEN the writing is extracted
#     - THEN check all the correct writings are extracted
#     """
#     for section in test_dict['ojad']['expected_sections']:
#         assert ojad.extract_reading(section['reading_section'], section['accent_section']) == section['reading']


# def test_build_accent_dict(test_dict: FullTestDict):
#     """
#     - GIVEN html sections
#     - WHEN the accent dict is constructed
#     - THEN check all the values are as expected
#     """
#     word_sections = [
#         (section['writing_section'], section['reading_section'], section['accent_section'])
#         for section in test_dict['ojad']['expected_sections']
#     ]

#     assert ojad.build_accent_dict(word_sections) == test_dict['ojad']['expected_output']


# def test_get_accent_dict(monkeypatch, test_dict: FullTestDict):
#     """
#     - GIVEN a list of words
#     - WHEN the accent dict is generated
#     - THEN check all the ojad info is correct and complete
#     """
#     word_list = test_dict['input']
#     html = test_dict['ojad']['html']
#     expected_output = test_dict['ojad']['expected_output']

#     monkeypatch.setattr("requests.post", lambda url, formdata, timeout: FakeResponse(html))
#     assert ojad.get_accent_dict(word_list) == expected_output
