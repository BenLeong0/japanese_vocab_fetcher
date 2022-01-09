import json
import re

import pytest   # type: ignore

# from custom_types.alternative_string_types import Kaki, URL
from modules import wanikani
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_dict_str_keys_to_kaki, convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=lambda d:d['id'])
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


API_KEY_REGEX = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"


#####################
## TESTS  ###########
#####################

def test_api_key_import():
    """Check the API_KEY is successfully imported"""
    assert re.match(API_KEY_REGEX, wanikani.API_KEY) is not None


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the wanikani info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_output = test_dict['wanikani']['expected_output']
    api_response = test_dict['wanikani']['api_response']

    monkeypatch.setattr("requests.get", lambda url, headers: FakeResponse(json.dumps(api_response)))

    assert wanikani.main(word_list) == expected_output


def test_main_api_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    response = json.dumps({"error": "api_error"})
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": json.dumps({"error": "api_error"}),
                "status_code": 400,
                "url": test_dict["wanikani"]["url"]
            },
            "main_data": {
                "audio": [],
                "sentences": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr("requests.get", lambda url, headers: FakeResponse(response, status_code=400))

    assert wanikani.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an audio dictionary is generated
    - THEN check it returns and empty dict
    """
    assert wanikani.main([]) == {}


def test_get_api_response(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API response is returned
    - THEN check the result is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    api_response = test_dict['wanikani']['api_response']

    def check_get_request(url, headers):
        auth_regex = r"Bearer " + API_KEY_REGEX
        assert "api.wanikani.com" in url
        assert "Authorization" in headers
        assert re.match(auth_regex, headers["Authorization"])
        return FakeResponse(json.dumps(api_response))

    monkeypatch.setattr("requests.get", check_get_request)

    assert wanikani.get_api_response(word_list) == api_response


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API URL is generated
    - THEN check the URL is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_url = test_dict['wanikani']['url']

    assert wanikani.get_url(word_list) == expected_url


def test_call_api(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN an API URL
    - WHEN the API is called
    - THEN check the response is handled correctly
    """
    url = test_dict['wanikani']['url']
    api_response = test_dict['wanikani']['api_response']

    def validate_get_request(url, headers):
        auth_regex = r"Bearer " + API_KEY_REGEX
        assert "api.wanikani.com" in url
        assert "Authorization" in headers
        assert re.match(auth_regex, headers["Authorization"])

    def mock_get_request(url, headers):
        validate_get_request(url, headers)
        return FakeResponse(json.dumps(api_response))

    monkeypatch.setattr("requests.get", mock_get_request)

    assert wanikani.call_api(url) == api_response


def test_call_api_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    url = test_dict['wanikani']['url']
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr("requests.get", lambda url, headers: FakeResponse(response, status_code=400))

    try:
        wanikani.call_api(url)
        assert False            # Test fails if call_api() doesn't raise an error
    except wanikani.WanikaniAPIError as api_error:
        assert api_error.error_msg == json.dumps({"error": "could not connect"})
        assert api_error.status_code == 400
        assert api_error.url == url


def test_call_api_unsuccessful(monkeypatch):
    """
    - GIVEN an API call
    - WHEN an unsuccessful response is returned
    - THEN check the response is handled as expected
    """
    unsuccessful_response = FakeResponse('{"error": "call_api failed"}', 400)
    monkeypatch.setattr("requests.get", lambda url, headers: unsuccessful_response)

    try:
        wanikani.call_api("www.testurl.com")
        assert False            # Test fails if call_api() doesn't raise an error
    except wanikani.WanikaniAPIError as api_error:
        assert api_error.error_msg == '{"error": "call_api failed"}'
        assert api_error.status_code == 400
        assert api_error.url == "www.testurl.com"


def test_build_result_dict(test_dict: FullTestDict):
    """
    - GIVEN an API response
    - WHEN the result dict is built
    - THEN check the result is as expected
    """
    api_response = test_dict["wanikani"]["api_response"]
    expected_result = convert_dict_str_keys_to_kaki(test_dict["wanikani"]["result_dict"])

    assert dict(wanikani.build_result_dict(api_response)) == expected_result
