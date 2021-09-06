from bs4 import BeautifulSoup as Soup
import pytest

from modules import suzuki
from testing.dict_typing import TestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


def test_get_formdata(test_dict: TestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = test_dict['input']
    expected_formdata = test_dict['suzuki']['request']['formdata']

    assert suzuki.get_formdata(word_list) == expected_formdata


def test_get_sections(test_dict: TestDict):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct
    """
    html = test_dict['suzuki']['html']
    expected_sections = test_dict['suzuki']['expected_sections']

    assert suzuki.get_sections(Soup(html, "html.parser")) == [
        (section['writing_section'], section['reading_section'], section['accent_section'])
        for section in expected_sections
    ]
