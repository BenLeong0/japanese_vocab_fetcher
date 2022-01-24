import json
from typing import cast

import pytest   # type: ignore

from custom_types.alternative_string_types import URL, HTMLString, Kaki, Yomi   # type: ignore

from modules import japanesepod
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

def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the audio dict is generated
    - THEN check all the japanesepod info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['japanesepod']['expected_sections']
    expected_output = test_dict['japanesepod']['expected_output']

    def get_word_from_wwwjdic_url(url: URL) -> Kaki:
        return Kaki(url[50:])

    def get_html_response(url: URL) -> str:
        if "wwwjdic" in url:
            word = get_word_from_wwwjdic_url(url)
            return sections[word]["html"]
        raise Exception("invalid url")

    monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(get_html_response(url)))

    assert japanesepod.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an audio dictionary is generated
    - THEN check it returns and empty dict
    """
    assert japanesepod.main([]) == {}


def test_main_api_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    response = json.dumps({"error": "api_error"})
    sections = test_dict["japanesepod"]["expected_sections"]
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": json.dumps({"error": "api_error"}),
                "status_code": 400,
                "url": sections[word]["url"]
            },
            "main_data": {
                "audio": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr("requests.get", lambda x, timeout: FakeResponse(response, status_code=400))
    assert japanesepod.main(word_list) == expected_output


def test_main_parsing_html_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTML cannot be parsed
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": "could not extract results from html",
                "status_code": 400,
                "url": URL("")
            },
            "main_data": {
                "audio": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse("invalid html"))
    assert japanesepod.main(word_list) == expected_output


def test_main_parsing_row_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a row cannot be parsed
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": "could not extract results from row",
                "status_code": 400,
                "url": URL("")
            },
            "main_data": {
                "audio": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse("<pre> invalid row</pre>"))
    assert japanesepod.main(word_list) == expected_output


def test_get_audio_urls(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the sentences are fetched for each individual word
    - THEN check the sentences are correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict["japanesepod"]["expected_sections"]
    full_expected_output = test_dict["japanesepod"]["expected_output"]

    for word in word_list:
        html = sections[word]['html']
        monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(html))
        expected_output = full_expected_output[word]
        assert japanesepod.get_audio_urls(word) == expected_output


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['japanesepod']['expected_sections']

    for word in word_list:
        assert japanesepod.get_url(word) == sections[word]["url"]


def test_get_html_string(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTML page is fetched
    - THEN check it is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['japanesepod']['expected_sections']

    for word in word_list:
        html = sections[word]['html']
        monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(html))
        assert japanesepod.get_html_string(word) == HTMLString(html)


def test_get_html_string_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(response, status_code=400))

    try:
        japanesepod.get_html_string(word_list[0])
        raise Exception("api error should have been raised")
    except japanesepod.JapanesePodAPIError as api_error:
        assert api_error.error_msg == json.dumps({"error": "could not connect"})
        assert api_error.status_code == 400


def test_extract_rows(test_dict: FullTestDict):
    for word in test_dict["input"]:
        html = HTMLString(test_dict["japanesepod"]["expected_sections"][word]["html"])
        expected_rows = test_dict["japanesepod"]["expected_sections"][word]["expected_rows"]
        assert japanesepod.extract_rows(html) == [row["raw_row"] for row in expected_rows]


@pytest.mark.parametrize(
    "invalid_html",
    [
        pytest.param("", id="empty html"),
        pytest.param("result text", id="just text"),
        pytest.param("<pre>result text", id="only pre"),
        pytest.param("result text</pre>", id="only post"),
    ]
)
def test_extract_rows_failure(invalid_html):
    try:
        japanesepod.extract_rows(invalid_html)
        raise Exception("japanesepod.extract_rows() should have thrown an error")
    except japanesepod.JapanesePodParsingError as parsing_error:
        assert parsing_error.error_msg == "could not extract results from html"
        assert parsing_error.status_code == 400


def test_extract_matches_from_row_string(test_dict: FullTestDict):
    for word in test_dict["input"]:
        expected_rows = test_dict["japanesepod"]["expected_sections"][word]["expected_rows"]
        for row in expected_rows:
            assert japanesepod.extract_matches_from_row_string(row["raw_row"]) == row["matches"]


@pytest.mark.parametrize(
    "invalid_row",
    [
        "",
        "\n",
        " testwriting) [test reading] test definition",
        " testwriting) test definition",
        " [testreading]",
        "\n(test writing)",
    ]
)
def test_extract_matches_from_row_string_failure(invalid_row: str):
    try:
        japanesepod.extract_matches_from_row_string(invalid_row)
        raise Exception("japanesepod.extract_matches_from_row() should have thrown an error")
    except japanesepod.JapanesePodParsingError as parsing_error:
        assert parsing_error.error_msg == "could not extract results from row"
        assert parsing_error.status_code == 400


def test_build_row_result_from_matches(test_dict: FullTestDict):
    for word in test_dict["input"]:
        expected_rows = test_dict["japanesepod"]["expected_sections"][word]["expected_rows"]
        for row in expected_rows:
            assert japanesepod.build_row_result_from_matches(*row["matches"]) == row["results"]


def test_format_row(test_dict: FullTestDict):
    for word in test_dict["input"]:
        expected_rows = test_dict["japanesepod"]["expected_sections"][word]["expected_rows"]
        for row in expected_rows:
            assert japanesepod.format_row(row["raw_row"]) == row["results"]


def test_extract_results(test_dict: FullTestDict):
    for word in test_dict["input"]:
        html = HTMLString(test_dict["japanesepod"]["expected_sections"][word]["html"])
        expected_rows = test_dict["japanesepod"]["expected_sections"][word]["expected_rows"]
        assert japanesepod.extract_results(html) == [row["results"] for row in expected_rows]


def test_filter_results(test_dict: FullTestDict):
    result_type = tuple[list[Kaki], list[Yomi]]
    for word in test_dict["input"]:
        expected_rows = test_dict["japanesepod"]["expected_sections"][word]["expected_rows"]
        results = [cast(result_type, row["results"]) for row in expected_rows]
        filtered_results = [cast(result_type, row["results"]) for row in expected_rows if row["relevant"] is True]
        assert japanesepod.filter_results(results, Kaki(word)) == filtered_results


def test_generate_audio_urls(test_dict: FullTestDict):
    result_type = tuple[list[Kaki], list[Yomi]]
    for word in test_dict["input"]:
        expected_section = test_dict["japanesepod"]["expected_sections"][word]
        filtered_results = [cast(result_type, row["results"]) for row in expected_section["expected_rows"] if row["relevant"] is True]
        assert japanesepod.generate_audio_urls(filtered_results) == expected_section["all_urls"]
