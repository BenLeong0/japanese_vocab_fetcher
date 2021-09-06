import json

import pytest
import requests

from testing.dicts import TEST_DICTS, TEST_DICT_IDS


@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param

API_URL = "http://127.0.0.1:5000/words"


def test_words_endpoint(test_dict):
    word_list = test_dict['input']
    encoded_word_list = json.dumps(word_list)
    payload = {'words': encoded_word_list}
    result = requests.get(API_URL, params=payload)
    assert result.status_code == 200
    assert result.text == json.dumps([
        {
            'word': word,
            'accent': {
                'ojad': [],
                'suzuki': [],
                'wadoku': [],
            },
        } for word in word_list
    ])
