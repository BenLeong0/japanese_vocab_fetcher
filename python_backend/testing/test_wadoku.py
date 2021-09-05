# pylint: disable=line-too-long

from bs4 import BeautifulSoup as Soup
import pytest

from modules import wadoku
from testing.dicts import (
    MEGANE,
    COMEBACK,
    TABERU_GAKUSEI
)

@pytest.mark.parametrize(
    "word_list, expected_url",
    [
        [MEGANE['input'], MEGANE['wadoku']['url']],
        [COMEBACK['input'], COMEBACK['wadoku']['url']],
        [TABERU_GAKUSEI['input'], TABERU_GAKUSEI['wadoku']['url']],
    ]
)
def test_get_url(word_list, expected_url):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    assert wadoku.get_url(word_list) == expected_url


@pytest.mark.parametrize(
    "html, expected_sections",
    [
        [MEGANE['wadoku']['html'], MEGANE['wadoku']['expected_sections']],
        [COMEBACK['wadoku']['html'], COMEBACK['wadoku']['expected_sections']],
        [TABERU_GAKUSEI['wadoku']['html'], TABERU_GAKUSEI['wadoku']['expected_sections']],
    ]
)
def test_get_sections(html, expected_sections):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct
    """
    assert wadoku.get_sections(Soup(html, "html.parser")) == [
        (section['writing_section'], section['reading_sections'])
        for section in expected_sections
    ]
