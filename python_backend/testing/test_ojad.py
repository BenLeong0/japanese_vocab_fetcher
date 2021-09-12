from bs4 import BeautifulSoup as Soup
import pytest

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


def test_get_formdata(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = test_dict['input']
    expected_formdata = test_dict['ojad']['formdata']

    assert ojad.get_formdata(word_list) == expected_formdata


def test_get_sections(test_dict: FullTestDict):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct
    """
    html = test_dict['ojad']['html']
    expected_sections = test_dict['ojad']['expected_sections']

    assert ojad.get_sections(Soup(html, "html.parser")) == [
        (section['writing_section'], section['reading_section'], section['accent_section'])
        for section in expected_sections
    ]


def test_extract_writing(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['ojad']['expected_sections']:
        assert ojad.extract_writing(section['writing_section']) == section['writing']


def test_extract_reading(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['ojad']['expected_sections']:
        assert ojad.extract_reading(section['reading_section'], section['accent_section']) == section['reading']


def test_build_accent_dict(test_dict: FullTestDict):
    """
    - GIVEN html sections
    - WHEN the accent dict is constructed
    - THEN check all the values are as expected
    """
    word_sections = [
        (section['writing_section'], section['reading_section'], section['accent_section'])
        for section in test_dict['ojad']['expected_sections']
    ]

    assert ojad.build_accent_dict(word_sections) == test_dict['ojad']['expected_output']


def test_get_accent_dict(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the ojad info is correct and complete
    """
    word_list = test_dict['input']
    html = test_dict['ojad']['html']
    expected_output = test_dict['ojad']['expected_output']

    monkeypatch.setattr("requests.post", lambda url, formdata, timeout: FakeResponse(html))
    assert ojad.get_accent_dict(word_list) == expected_output
