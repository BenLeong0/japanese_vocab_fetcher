from bs4 import BeautifulSoup as Soup
import pytest   # type: ignore

from modules import suzuki
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=lambda d:d['id'])
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


#####################
## TESTS  ###########
#####################

def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the suzuki info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    html = test_dict['suzuki']['html']
    expected_output = test_dict['suzuki']['expected_output']

    monkeypatch.setattr("requests.post", lambda url, formdata, timeout: FakeResponse(html))
    assert suzuki.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert suzuki.main([]) == {}


def test_get_formdata(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_formdata = test_dict['suzuki']['formdata']

    assert suzuki.get_formdata(word_list) == expected_formdata


def test_get_sections(test_dict: FullTestDict):
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


def test_extract_writing(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['suzuki']['expected_sections']:
        assert suzuki.extract_writing(section['writing_section']) == section['writing']


def test_extract_reading(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict['suzuki']['expected_sections']:
        assert suzuki.extract_reading(section['reading_section'], section['accent_section']) == section['reading']


def test_build_accent_dict(test_dict: FullTestDict):
    """
    - GIVEN html sections
    - WHEN the accent dict is constructed
    - THEN check all the values are as expected
    """
    word_sections = [
        (section['writing_section'], section['reading_section'], section['accent_section'])
        for section in test_dict['suzuki']['expected_sections']
    ]

    expected_accent_dict = {
        word:test_dict['suzuki']['expected_output'][word]['main_data']['accent']
        for word in test_dict['suzuki']['expected_output']
    }

    assert suzuki.build_accent_dict(word_sections) == expected_accent_dict
