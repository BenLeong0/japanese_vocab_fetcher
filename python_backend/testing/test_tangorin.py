import json
import re

from bs4 import BeautifulSoup as Soup
import pytest   # type: ignore

from custom_types.alternative_string_types import Yomi
from modules import tangorin
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=lambda d:d['id'])
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text, status_code=200, error=""):
        self.text = text
        self.status_code = status_code


#####################
## TESTS  ###########
#####################

# def test_main(monkeypatch, test_dict: FullTestDict):
#     """
#     - GIVEN a list of words
#     - WHEN the accent dict is generated
#     - THEN check all the tangorin info is correct and complete
#     """
#     word_list = convert_list_of_str_to_kaki(test_dict['input'])
#     html = test_dict['tangorin']['html']
#     expected_output = test_dict['tangorin']['expected_output']

#     monkeypatch.setattr("requests.post", lambda x, timeout: FakeResponse(html))
#     assert tangorin.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert tangorin.main([]) == {}
