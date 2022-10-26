import json
import re

from bs4 import BeautifulSoup as Soup
import pytest   # type: ignore

from custom_types.alternative_string_types import Kaki, URL
from modules import tangorin
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(name="test_dict", params=TEST_DICTS, ids=lambda d:d['id'])
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
    - THEN check all the tangorin info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['tangorin']['expected_sections']
    expected_output = test_dict['tangorin']['expected_output']

    def get_word_from_tangorin_url(url: URL) -> Kaki:
        match = re.search(r"\?search=(.+?)$", url)
        assert match is not None
        return Kaki(match.group(1))

    def get_html_response(url: URL) -> str:
        word = get_word_from_tangorin_url(url)
        return sections[word]["html"]

    monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(get_html_response(url)))

    assert tangorin.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert tangorin.main([]) == {}


def test_main_api_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    response = json.dumps({"error": "api_error"})
    sections = test_dict["tangorin"]["expected_sections"]
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": json.dumps({"error": "api_error"}),
                "status_code": 400,
                "url": sections[word]["url"]
            },
            "main_data": {
                "sentences": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr("requests.get", lambda x, timeout: FakeResponse(response, status_code=400))
    assert tangorin.main(word_list) == expected_output


def test_get_sentences(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the sentences are fetched for each individual word
    - THEN check the sentences are correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict["tangorin"]["expected_sections"]
    full_expected_output = test_dict["tangorin"]["expected_output"]

    for word in word_list:
        html = sections[word]['html']
        monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(html))
        expected_output = full_expected_output[word]
        assert tangorin.get_sentences(word) == expected_output


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['tangorin']['expected_sections']

    for word in word_list:
        assert tangorin.get_url(word) == sections[word]["url"]


def test_get_html(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTML page is fetched
    - THEN check it is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['tangorin']['expected_sections']

    for word in word_list:
        html = sections[word]['html']
        monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(html))
        assert tangorin.get_html(word) == Soup(html, 'html.parser')


def test_get_html_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(response, status_code=400))

    try:
        tangorin.get_html(word_list[0])
        assert False
    except tangorin.TangorinAPIError as api_error:
        assert api_error.error_msg == json.dumps({"error": "could not connect"})
        assert api_error.status_code == 400


@pytest.mark.parametrize(
    "html, expected_html",
    [
        pytest.param(
            Soup("<div>test</div>", "html.parser"),
            Soup("<div>test</div>", "html.parser"),
            id="empty div",
        ),
        pytest.param(
            Soup("<div>test<mark></mark></div>", "html.parser"),
            Soup("<div>test<mark></mark></div>", "html.parser"),
            id="single mark tag",
        ),
        pytest.param(
            Soup("<div>test<mark></mark><mark></mark></div>", "html.parser"),
            Soup("<div>test<mark></mark> <mark></mark></div>", "html.parser"),
            id="double mark tag",
        ),
        pytest.param(
            Soup("<div>test<rt>furi</rt></div>", "html.parser"),
            Soup("<div>test</div>", "html.parser"),
            id="remove furigana",
        ),
        pytest.param(
            Soup("<div>test<rt>furi</rt>text<rt>morefuri</rt></div>", "html.parser"),
            Soup("<div>testtext</div>", "html.parser"),
            id="remove multiple furigana",
        ),
        pytest.param(
            Soup("<div>test<mark></mark><mark></mark><rt>furi</rt></div>", "html.parser"),
            Soup("<div>test<mark></mark> <mark></mark></div>", "html.parser"),
            id="double mark tag and remove furigana",
        ),
        pytest.param(
            Soup("<div>test<mark></mark><rt>furi</rt><mark></mark><rt>furi</rt></div>", "html.parser"),
            Soup("<div>test<mark></mark> <mark></mark></div>", "html.parser"),
            id="furigana inside double mark tag",
        ),
    ],
)
def test_clean_html(html: Soup, expected_html: Soup):
    """
    - GIVEN an html section
    - WHEN clean_html() is run on it
    - THEN check it is properly cleaned
    """
    tangorin.clean_html(html)
    assert str(html) == str(expected_html)


def test_extract_sentences(test_dict: FullTestDict):
    """
    - GIVEN an html section
    - WHEN the subsections are extracted
    - THEN check the array of subsections is correct for each word
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    sections = test_dict['tangorin']['expected_sections']
    expected_output = test_dict['tangorin']['expected_output']

    for word in word_list:
        html = sections[word]['html']
        expected_sentences = expected_output[word]["main_data"]["sentences"]
        assert tangorin.extract_sentences(Soup(html, "html.parser")) == expected_sentences
