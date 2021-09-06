# pylint: disable=line-too-long

from collections import defaultdict
from bs4 import BeautifulSoup as Soup
import pytest

from modules import wadoku
from testing.dicts import (
    MEGANE,
    COMEBACK,
    TABERU_GAKUSEI,
    KOTOBA,
)


class FakeResponse:
    def __init__(self, text):
        self.text = text


@pytest.mark.parametrize(
    "test_dict",
    [
        MEGANE,
        COMEBACK,
        TABERU_GAKUSEI,
        KOTOBA,
    ]
)
def test_get_url(test_dict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = test_dict['input']
    expected_url = test_dict['wadoku']['url']

    assert wadoku.get_url(word_list) == expected_url


@pytest.mark.parametrize(
    "test_dict",
    [
        MEGANE,
        COMEBACK,
        TABERU_GAKUSEI,
        KOTOBA,
    ]
)
def test_get_sections(test_dict):
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


@pytest.mark.parametrize(
    "test_dict",
    [
        MEGANE,
        COMEBACK,
        TABERU_GAKUSEI,
        KOTOBA,
    ]
)
def test_extract_writings(test_dict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['wadoku']['expected_sections']:
        assert wadoku.extract_writings(section['writing_section']) == section['writings']


@pytest.mark.parametrize(
    "test_dict",
    [
        MEGANE,
        COMEBACK,
        TABERU_GAKUSEI,
        KOTOBA,
    ]
)
def test_extract_readings(test_dict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['wadoku']['expected_sections']:
        for html_section, reading in zip(section['reading_sections'], section['readings']):
            assert wadoku.extract_reading(html_section) == reading


@pytest.mark.parametrize(
    "test_dict",
    [
        MEGANE,
        COMEBACK,
        TABERU_GAKUSEI,
        KOTOBA,
    ]
)
def test_build_accent_dict(test_dict):
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


@pytest.mark.parametrize("test_dict", [
    MEGANE,
    COMEBACK,
    TABERU_GAKUSEI,
    KOTOBA,
])
def test_get_accent_dict(monkeypatch, test_dict):
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
