import pytest   # type: ignore
import re

# from custom_types import Kaki, URL
from modules import wanikani
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
    api_key_format_re = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    assert re.match(api_key_format_re, wanikani.API_KEY) is not None


# def test_main(monkeypatch, test_dict: FullTestDict):
#     """
#     - GIVEN a list of words
#     - WHEN the accent dict is generated
#     - THEN check all the wanikani info is correct and complete
#     """
#     word_list = convert_list_of_str_to_kaki(test_dict['input'])
#     sections = test_dict['wanikani']['expected_sections']
#     expected_output = test_dict['wanikani']['expected_output']
#     api_response = test_dict['wanikani']['api_response']

#     monkeypatch.setattr("requests.get", lambda url: FakeResponse(lambda url: api_response))
#     assert wanikani.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an audio dictionary is generated
    - THEN check it returns and empty dict
    """
    assert wanikani.main([]) == {}


def test_gen_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API URL is generated
    - THEN check the URL is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_url = test_dict['wanikani']['url']

    assert wanikani.get_url(word_list) == expected_url
