import json
import re

import pytest  # type: ignore

from api.custom_types.alternative_string_types import URL, Kaki
from api.modules import forvo
from api.utils import convert_list_of_str_to_kaki
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(name="test_dict", params=TEST_DICTS, ids=lambda d: d.test_name)
def fixture_test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


#####################
## TESTS  ###########
#####################


def test_api_key_import():
    """Check the API_KEY is successfully imported"""
    api_key_format_re = r"^[0-9a-f]{32}$"
    assert re.match(api_key_format_re, forvo.API_KEY) is not None


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the forvo info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.forvo.expected_sections
    expected_output = test_dict.forvo.expected_output

    def get_word_from_forvo_url(url: URL) -> Kaki:
        match = re.search(r"word/(.+?)/", url)
        assert match is not None
        return Kaki(match.group(1))

    def get_api_response(url: URL) -> str:
        word = get_word_from_forvo_url(url)
        return sections[word]["api_response"]

    monkeypatch.setattr(
        "requests.get", lambda url, **_: FakeResponse(get_api_response(url))
    )
    assert forvo.main(word_list) == expected_output


def test_main_api_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "api_error"})
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": json.dumps({"error": "api_error"}),
                "status_code": 400,
                "url": test_dict.forvo.expected_sections[word]["url"],
            },
            "main_data": {
                "audio": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda url, **__: FakeResponse(response, status_code=400)
    )
    assert forvo.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an audio dictionary is generated
    - THEN check it returns and empty dict
    """
    assert forvo.main([]) == {}


def test_get_api_urls(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN API urls are generated
    - THEN check the urls are encoded and correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.forvo.expected_sections

    for word in word_list:
        assert forvo.get_api_url(word) == sections[word]["url"]


def test_get_audio_urls(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the audio url lists are generated for each word
    - THEN check the lists are as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.forvo.expected_sections
    expected_output = test_dict.forvo.expected_output

    for word in word_list:
        section = sections[word]

        fake_response = section["api_response"]
        monkeypatch.setattr(
            "requests.get", lambda url, **_: FakeResponse(fake_response)
        )

        assert forvo.get_audio_urls(word) == expected_output[word]


def test_call_api(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API is called for each word
    - THEN check each response is returned correctly
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.forvo.expected_sections

    for word in word_list:
        section = sections[word]

        fake_response = section["api_response"]
        monkeypatch.setattr(
            "requests.get", lambda url, **_: FakeResponse(fake_response)
        )

        resp = forvo.call_api(word)

        assert "attributes" in resp
        assert "items" in resp
        assert resp["attributes"]["total"] == section["total_items"]
        assert len(resp["items"]) == section["total_items"]


def test_call_api_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr(
        "requests.get", lambda url, **_: FakeResponse(response, status_code=400)
    )

    for word in word_list:
        with pytest.raises(forvo.ForvoAPIError) as api_error:
            forvo.call_api(word)
        assert api_error.value.error_msg == json.dumps({"error": "could not connect"})
        assert api_error.value.status_code == 400


def test_extract_audio_list(test_dict: FullTestDict):
    """
    - GIVEN a series of responses from the API
    - WHEN the audio urls are extracted
    - THEN check the returned lists are correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.forvo.expected_sections
    expected_output = test_dict.forvo.expected_output

    for word in word_list:
        api_response = json.loads(sections[word]["api_response"])
        assert (
            forvo.extract_audio_list(api_response, word)
            == expected_output[word]["main_data"]["audio"]
        )


def test_extract_data():
    """
    - GIVEN a response from the API
    - WHEN the response's url is extracted
    - THEN check the url is correct
    """
    test_item = {
        "pathmp3": "http://www.test.com/audio.mp3",
        "username": "test_username",
    }
    assert forvo.extract_data(test_item) == {
        "url": "http://www.test.com/audio.mp3",
        "username": "test_username",
    }


@pytest.mark.parametrize(
    "item, word, expected_result",
    [
        ({"word": "静か"}, "静か", True),
        ({"word": "\\u9759\\u304b"}, "静か", True),
        ({"word": ""}, "", True),
        ({"word": "not 静か"}, "静か", False),
        ({"word": "静か"}, "not 静か", False),
        ({"word": ""}, None, False),
    ],
)
def test_correct_word(item, word, expected_result):
    """
    - GIVEN a response from the API
    - WHEN the response's word is checked
    - THEN check `correct_word` returns the correct boolean
    """
    assert forvo.correct_word(item, word) == expected_result
