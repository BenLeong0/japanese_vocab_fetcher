import json
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
        assert "Authorization" in headers
        assert re.match(auth_regex, headers["Authorization"])
        return FakeResponse(json.dumps(api_response))

    monkeypatch.setattr("requests.get", check_get_request)

    assert wanikani.get_api_response(word_list) == api_response


def test_gen_url(test_dict: FullTestDict):
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
        assert "Authorization" in headers
        assert re.match(auth_regex, headers["Authorization"])

    def mock_get_request(url, headers):
        validate_get_request(url, headers)
        return FakeResponse(json.dumps(api_response))

    monkeypatch.setattr("requests.get", mock_get_request)

    assert wanikani.call_api(url) == api_response


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
        assert False
    except wanikani.WanikaniAPIError as e:
        assert e.error_msg == "call_api failed"
        assert e.status_code == 400
        assert e.url == "www.testurl.com"
