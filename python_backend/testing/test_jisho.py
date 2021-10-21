import json
import re

import pytest   # type: ignore

from custom_types.alternative_string_types import Kaki, URL
from modules import jisho
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=lambda d:d['id'])
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


#####################
## TESTS  ###########
#####################


# def test_main(monkeypatch, test_dict: FullTestDict):
#     """
#     - GIVEN a list of words
#     - WHEN the accent dict is generated
#     - THEN check all the jisho info is correct and complete
#     """
#     word_list = convert_list_of_str_to_kaki(test_dict['input'])
#     sections = test_dict['jisho']['expected_sections']
#     expected_output = test_dict['jisho']['expected_output']

#     def get_word_from_jisho_url(url: URL) -> Kaki:
#         match = re.search(r"word/(.+?)/", url)
#         assert match is not None
#         return Kaki(match.group(1))

#     def get_api_response(url: URL) -> str:
#         word = get_word_from_jisho_url(url)
#         return sections[word]["api_response"]

#     monkeypatch.setattr("requests.get", lambda url: FakeResponse(get_api_response(url)))
#     assert jisho.main(word_list) == expected_output


# def test_main_api_error(monkeypatch, test_dict: FullTestDict):
#     """
#     - GIVEN a list of words
#     - WHEN the API returns an unsuccessful status code
#     - THEN check the failed dict is returned as expected
#     """
#     word_list = convert_list_of_str_to_kaki(test_dict['input'])
#     response = json.dumps({"error": "api_error"})
#     expected_output = {
#         word: {
#             "success": False,
#             "error": {
#                 "error_msg": "api_error",
#                 "status_code": 400,
#                 "url": test_dict["jisho"]["expected_sections"][word]["url"]
#             },
#         }
#         for word in word_list
#     }

#     monkeypatch.setattr("requests.get", lambda x: FakeResponse(response, status_code=400))
#     assert jisho.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN a results dictionary is generated
    - THEN check it returns and empty dict
    """
    assert jisho.main([]) == {}


def test_get_api_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN API urls are generated
    - THEN check the urls are encoded and correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['jisho']['expected_sections']

    for word in word_list:
        assert jisho.get_api_url(word) == sections[word]["url"]
