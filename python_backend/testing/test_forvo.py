# pylint: disable=redefined-outer-name

import json
import re

import pytest   # type: ignore

from custom_types import Kaki, URL
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
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['forvo']['expected_sections']
    expected_output = test_dict['forvo']['expected_output']

    def get_word_from_forvo_url(url: URL) -> Kaki:
        match = re.search(r"word/(.+?)/", url)
        assert match is not None
        return Kaki(match.group(1))

    def get_api_response(url: URL) -> str:
        word = get_word_from_forvo_url(url)
        return sections[word]["api_response"]

    monkeypatch.setattr("requests.get", lambda url: FakeResponse(get_api_response(url)))
    assert forvo.main(word_list) == expected_output


def test_get_api_urls(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN API urls are generated
    - THEN check the urls are encoded and correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['forvo']['expected_sections']

    for word in word_list:
        assert forvo.get_api_url(word) == sections[word]["url"]


def test_call_api(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API is called
    - THEN check the response is returned correctly
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['forvo']['expected_sections']

    for word in word_list:
        section = sections[word]

        fake_response = section['api_response']
        monkeypatch.setattr("requests.get", lambda url: FakeResponse(fake_response))

        resp = forvo.call_api(word)

        assert "attributes" in resp
        assert "items" in resp
        assert resp['attributes']['total'] == section['total_items']
        assert len(resp['items']) == section['total_items']


def test_get_audio_url_list(test_dict: FullTestDict):
    """
    - GIVEN a response from the API
    - WHEN the audio urls are extracted
    - THEN check the returned list is correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['forvo']['expected_sections']
    expected_output = test_dict['forvo']["expected_output"]

    for word in word_list:
        api_response = json.loads(sections[word]['api_response'])
        assert forvo.extract_audio_url_list(api_response, word) == expected_output[word]


def test_extract_audio_url():
    """
    - GIVEN a response from the API
    - WHEN the response's url is extracted
    - THEN check the url is correct
    """
    test_item = {
        "pathmp3": "http://www.test.com/audio.mp3"
    }
    assert forvo.extract_audio_url(test_item) == "http://www.test.com/audio.mp3"


@pytest.mark.parametrize(
    "item, word, expected_result",
    [
        ({"word": "静か"}, "静か", True),
        ({"word": "\\u9759\\u304b"}, "静か", True),
        ({"word": ""}, "", True),
        ({"word": "not 静か"}, "静か", False),
        ({"word": "静か"}, "not 静か", False),
        ({"word": ""}, None, False),
    ]
)
def test_correct_word(item, word, expected_result):
    """
    - GIVEN a response from the API
    - WHEN the response's word is checked
    - THEN check `correct_word` returns the correct boolean
    """
    assert forvo.correct_word(item, word) == expected_result
