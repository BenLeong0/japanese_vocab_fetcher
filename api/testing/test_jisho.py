import json
import re

import pytest  # type: ignore

from api.custom_types.alternative_string_types import Kaki, URL
from api.modules import jisho
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from api.utils import convert_list_of_str_to_kaki


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


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the jisho info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jisho.expected_sections
    expected_output = test_dict.jisho.expected_output

    def get_word_from_jisho_url(url: URL) -> Kaki:
        match = re.search(r"words\?keyword=(.+)", url)
        assert match is not None
        return Kaki(match.group(1))

    def get_api_response(url: URL) -> str:
        word = get_word_from_jisho_url(url)
        return json.dumps(sections[word]["api_response"])

    monkeypatch.setattr("requests.get", lambda url: FakeResponse(get_api_response(url)))
    assert jisho.main(word_list) == expected_output


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
                "url": test_dict.jisho.expected_sections[word]["url"],
            },
            "main_data": {
                "results": [],
                "extra": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda x: FakeResponse(response, status_code=400)
    )
    assert jisho.main(word_list) == expected_output


def test_main_meta_data_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"meta": {"status": 400, "error_msg": "api_error"}})
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": "An error occurred. Meta data: "
                + json.dumps({"status": 400, "error_msg": "api_error"}),
                "status_code": 400,
                "url": test_dict.jisho.expected_sections[word]["url"],
            },
            "main_data": {
                "results": [],
                "extra": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda x: FakeResponse(response, status_code=200)
    )
    assert jisho.main(word_list) == expected_output


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
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jisho.expected_sections

    for word in word_list:
        assert jisho.get_api_url(word) == sections[word]["url"]


def test_call_api(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN an API URL
    - WHEN the API is called
    - THEN check the response is handled correctly
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)

    for word in word_list:
        api_response = test_dict.jisho.expected_sections[word]["api_response"]
        monkeypatch.setattr(
            "requests.get", lambda url: FakeResponse(json.dumps(api_response))
        )

        assert jisho.call_api(word) == api_response


def test_call_api_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr(
        "requests.get", lambda url: FakeResponse(response, status_code=400)
    )

    for word in word_list:
        try:
            jisho.call_api(word)
            assert False
        except jisho.JishoAPIError as api_error:
            assert api_error.error_msg == json.dumps({"error": "could not connect"})
            assert api_error.status_code == 400


def test_call_api_meta_data_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a failed response is received
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"meta": {"status": 400, "error_msg": "api_error"}})
    monkeypatch.setattr(
        "requests.get", lambda url: FakeResponse(response, status_code=200)
    )

    for word in word_list:
        try:
            jisho.call_api(word)
            assert False
        except jisho.JishoAPIError as api_error:
            assert api_error.error_msg == "An error occurred. Meta data: " + json.dumps(
                {"status": 400, "error_msg": "api_error"}
            )
            assert api_error.status_code == 400


def test_segregate_items(test_dict: FullTestDict):
    """
    - GIVEN a list of items from a Jisho API response
    - WHEN they is checked whether they correspond to the correct word
    - THEN check the returned list is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)

    for word in word_list:
        api_response = test_dict.jisho.expected_sections[word]["api_response"]
        items = api_response["data"]
        expected_filtered_items = test_dict.jisho.expected_sections[word][
            "filtered_items"
        ]
        expected_extra_items = test_dict.jisho.expected_sections[word]["extra_items"]

        assert jisho.segregate_items(items, word) == (
            expected_filtered_items,
            expected_extra_items,
        )


def test_extract_jisho_data(test_dict: FullTestDict):
    """
    - GIVEN an API response
    - WHEN the data is extracted
    - THEN check the returned result is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)

    for word in word_list:
        api_response = test_dict.jisho.expected_sections[word]["api_response"]
        expected_output = {
            "results": test_dict.jisho.expected_sections[word]["filtered_items"],
            "extra": test_dict.jisho.expected_sections[word]["extra_items"],
        }

        assert jisho.extract_jisho_data(api_response, word) == expected_output
