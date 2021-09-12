from bs4 import BeautifulSoup as Soup
import pytest
import re

from modules import wadoku
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert wadoku.get_accent_dict([]) == {}


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = test_dict['input']
    expected_url = test_dict['wadoku']['url']

    assert wadoku.get_url(word_list) == expected_url


def test_get_sections(test_dict: FullTestDict):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct
    """
    html = test_dict['wadoku']['html']
    expected_sections = test_dict['wadoku']['expected_sections']

    assert wadoku.get_sections(Soup(html, "html.parser")) == [
        (section['writing_section'], section['reading_sections'])
        for section in expected_sections
    ]


def test_extract_writings(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['wadoku']['expected_sections']:
        assert wadoku.extract_writings(section['writing_section']) == section['writings']


def test_extract_readings(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['wadoku']['expected_sections']:
        for html_section, reading in zip(section['reading_sections'], section['readings']):
            assert wadoku.extract_reading(html_section) == reading


def test_build_accent_dict(test_dict: FullTestDict):
    """
    - GIVEN html sections
    - WHEN the accent dict is constructed
    - THEN check all the values are as expected
    """
    word_sections = [
        (section['writing_section'], section['reading_sections'])
        for section in test_dict['wadoku']['expected_sections']
    ]

    assert wadoku.build_accent_dict(word_sections) == test_dict['wadoku']['full_accent_dict']


def test_get_accent_dict(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the wadoku info is correct and complete
    """
    word_list = test_dict['input']
    html = test_dict['wadoku']['html']
    expected_output = test_dict['wadoku']['expected_output']

    monkeypatch.setattr("requests.post", lambda x, timeout: FakeResponse(html))
    assert wadoku.get_accent_dict(word_list) == expected_output


def test_recursion(monkeypatch):
    """
    GIVEN a wordlist with an invalid first word
    WHEN an accent dict is generated
    THEN the function runs again, excluding the first word
    """
    word_list = ["BADINPUT", "食べる", "学生"]

    def html_response(url, timeout):
        if "BADINPUT" in url:
            f = open("testing/html_files/wadoku_badinput_taberu_gakusei.html", encoding="utf8")
        else:
            f = open("testing/html_files/wadoku_taberu_gakusei.html", encoding="utf8")
        mock_response = FakeResponse(re.sub(r'>\s*<', '><', f.read()))
        f.close()
        return mock_response

    monkeypatch.setattr("requests.post", html_response)

    assert wadoku.get_accent_dict(word_list) == {
        'BADINPUT': [],
        '食べる': ["たべ' る"],
        '学生': ["がくせい"],
    }
