"""
Tests that can be manually run against a live server
ie `coverage run -m pytest testing/_test_server.py -vv`
"""

import json

import pytest   # type: ignore
import requests

from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS


API_URL = "http://127.0.0.1:5000/words"


@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


def test_words_endpoint(test_dict: FullTestDict):
    word_list = test_dict['input']
    payload = {'words': word_list}
    result = requests.get(API_URL, data=json.dumps(payload))

    assert result.status_code == 200
    assert result.text == json.dumps(test_dict['expected_result'])
