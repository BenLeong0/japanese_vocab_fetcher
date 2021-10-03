import pytest   # type: ignore

from modules import forvo
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


#####################
## TESTS  ###########
#####################

def test_api_key_import():
    """Check the API_KEY is successfully imported"""
    assert len(forvo.API_KEY) == 32


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the forvo info is correct and complete
    """
#     word_list = convert_list_of_str_to_kaki(test_dict['input'])
#     html = test_dict['forvo']['html']
#     expected_output = test_dict['forvo']['expected_output']

#     monkeypatch.setattr("requests.post", lambda url, formdata, timeout: FakeResponse(html))
#     assert forvo.main(word_list) == expected_output


def test_get_api_urls(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN API urls are generated
    - THEN check the urls are encoded and correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_urls = [section['url'] for section in test_dict['forvo']['expected_sections']]

    for word, expected_url in zip(word_list, expected_urls):
        assert forvo.get_api_url(word) == expected_url
