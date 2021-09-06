import json

import pytest
import requests

API_URL = "http://127.0.0.1:5000/words"

@pytest.mark.parametrize(
    "word_list",
    [
        ['行く'],
        ['行く', '眼鏡'],
        [],
    ]
)
def test_words_endpoint(word_list):
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
