import json
import re

import pytest  # type: ignore
from bs4 import BeautifulSoup as Soup

from api.custom_types.alternative_string_types import Yomi
from api.custom_types.exception_types import APIErrorDict
from api.modules import wadoku
from api.utils import convert_list_of_str_to_kaki
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(name="test_dict", params=TEST_DICTS, ids=lambda d: d.test_name)
def fixture_test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text, status_code=200, error=""):
        self.text = text
        self.status_code = status_code


#####################
## TESTS  ###########
#####################


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the wadoku info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    html = test_dict.wadoku.html
    expected_output = test_dict.wadoku.expected_output

    monkeypatch.setattr("requests.post", lambda x, timeout: FakeResponse(html))
    assert wadoku.main(word_list) == expected_output


def test_main_recursion(monkeypatch):
    """
    GIVEN a wordlist with an invalid first word
    WHEN an accent dict is generated
    THEN the function runs again, excluding the first word
    """
    word_list = convert_list_of_str_to_kaki(["BADINPUT", "食べる", "学生"])

    def html_response(url, timeout):
        if "BADINPUT" in url:
            resp_path = "testing/html_files/wadoku_badinput_taberu_gakusei.html"
        else:
            resp_path = "testing/html_files/wadoku_taberu_gakusei.html"

        with open(resp_path, encoding="utf8") as f:
            mock_response = FakeResponse(re.sub(r">\s*<", "><", f.read()))
        return mock_response

    monkeypatch.setattr("requests.post", html_response)

    assert wadoku.main(word_list) == {
        "BADINPUT": {
            "success": True,
            "error": None,
            "main_data": {
                "accent": [],
            },
        },
        "食べる": {
            "success": True,
            "error": None,
            "main_data": {
                "accent": [Yomi("たべ' る")],
            },
        },
        "学生": {
            "success": True,
            "error": None,
            "main_data": {
                "accent": [Yomi("がくせい")],
            },
        },
    }


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert wadoku.main([]) == {}


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
            "error": APIErrorDict(
                error_msg=json.dumps({"error": "api_error"}),
                status_code=400,
                url=test_dict.wadoku.url,
            ),
            "main_data": {
                "accent": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.post", lambda x, timeout: FakeResponse(response, status_code=400)
    )
    assert wadoku.main(word_list) == expected_output


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    expected_url = test_dict.wadoku.url

    assert wadoku.get_url(word_list) == expected_url


def test_get_html(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTML page is fetched
    - THEN check it is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    html = test_dict.wadoku.html

    monkeypatch.setattr("requests.post", lambda url, timeout: FakeResponse(html))

    assert wadoku.get_html(word_list) == Soup(html, "html.parser")


def test_get_html_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr(
        "requests.post", lambda x, timeout: FakeResponse(response, status_code=400)
    )

    with pytest.raises(wadoku.WadokuAPIError) as api_error:
        wadoku.get_html(word_list)
    assert api_error.value.error_msg == json.dumps({"error": "could not connect"})
    assert api_error.value.status_code == 400


def test_get_sections(test_dict: FullTestDict):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct
    """
    html = test_dict.wadoku.html
    expected_sections = test_dict.wadoku.expected_sections

    assert wadoku.get_sections(Soup(html, "html.parser")) == [
        (section["writing_section"], section["reading_sections"])
        for section in expected_sections
    ]


def test_extract_writings(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict.wadoku.expected_sections:
        assert (
            wadoku.extract_writings(section["writing_section"]) == section["writings"]
        )


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ["no punct", "no punct"],
        ["remove･dot", "removedot"],
        ["remove\nnewline", "removenewline"],
        ["remove￨pipe", "removepipe"],
        ["remove~tilda", "removetilda"],
        ["remove~~tildas", "removetildas"],
        ["remove\n￨･~all", "removeall"],
    ],
)
def test_remove_punct(input_string, expected_output):
    """
    - GIVEN a string, potentially with invalid punctuation
    - WHEN the punctation is removed
    - THEN check all the unwanted punctuation has be successfully removed
    """
    assert wadoku.remove_punct(input_string) == expected_output


def test_extract_readings(test_dict: FullTestDict):
    """
    - GIVEN an html sections
    - WHEN the writing is extracted
    - THEN check all the correct writings are extracted
    """
    for section in test_dict.wadoku.expected_sections:
        for html_section, reading in zip(
            section["reading_sections"], section["readings"]
        ):
            assert wadoku.extract_reading(html_section) == reading


def test_build_accent_dict(test_dict: FullTestDict):
    """
    - GIVEN html sections
    - WHEN the accent dict is constructed
    - THEN check all the values are as expected
    """
    word_sections = [
        (section["writing_section"], section["reading_sections"])
        for section in test_dict.wadoku.expected_sections
    ]

    assert wadoku.build_accent_dict(word_sections) == test_dict.wadoku.full_accent_dict
