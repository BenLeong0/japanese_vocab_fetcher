import json

import pytest  # type: ignore

from api.custom_types.alternative_string_types import (  # type: ignore
    URL,
    HTMLString,
    Kaki,
)
from api.modules import jdict
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
    - WHEN the results dict is generated
    - THEN check all the jdict info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jdict.expected_sections
    expected_output = test_dict.jdict.expected_output

    def get_word_from_wwwjdic_url(url: URL) -> Kaki:
        return Kaki(url[50:])

    def get_html_response(url: URL) -> str:
        word = get_word_from_wwwjdic_url(url)
        return sections[word]["html"]

    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse(get_html_response(url))
    )

    assert jdict.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN a results dictionary is generated
    - THEN check it returns and empty dict
    """
    assert jdict.main([]) == {}


def test_main_api_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "api_error"})
    sections = test_dict.jdict.expected_sections
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": json.dumps({"error": "api_error"}),
                "status_code": 400,
                "url": sections[word]["url"],
            },
            "main_data": {
                "results": [],
                "extra": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda x, timeout: FakeResponse(response, status_code=400)
    )
    assert jdict.main(word_list) == expected_output


def test_main_request_exception(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the request raises
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jdict.expected_sections
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": "request failed",
                "status_code": 500,
                "url": sections[word]["url"],
            },
            "main_data": {
                "results": [],
                "extra": [],
            },
        }
        for word in word_list
    }

    def raise_error(url, timeout):
        raise ConnectionError("boom")

    monkeypatch.setattr("requests.get", raise_error)
    assert jdict.main(word_list) == expected_output


def test_main_parsing_html_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTML cannot be parsed
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": "could not extract results from html",
                "status_code": 400,
                "url": URL(""),
            },
            "main_data": {
                "results": [],
                "extra": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse("invalid html")
    )
    assert jdict.main(word_list) == expected_output


def test_main_parsing_row_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a row cannot be parsed
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": "could not extract results from row",
                "status_code": 400,
                "url": URL(""),
            },
            "main_data": {
                "results": [],
                "extra": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse("<pre> invalid row</pre>")
    )
    assert jdict.main(word_list) == expected_output


def test_get_jdict_data(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the entries are fetched for each individual word
    - THEN check the results are correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jdict.expected_sections
    full_expected_output = test_dict.jdict.expected_output

    for word in word_list:
        html = sections[word]["html"]
        monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(html))
        assert jdict.get_jdict_data(word) == full_expected_output[word]


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jdict.expected_sections

    for word in word_list:
        assert jdict.get_url(word) == sections[word]["url"]


def test_get_html_string(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTML page is fetched
    - THEN check it is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.jdict.expected_sections

    for word in word_list:
        html = sections[word]["html"]
        monkeypatch.setattr("requests.get", lambda url, timeout: FakeResponse(html))
        assert jdict.get_html_string(word) == HTMLString(html)


def test_get_html_string_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse(response, status_code=400)
    )

    with pytest.raises(jdict.JDictAPIError) as excinfo:
        jdict.get_html_string(word_list[0])
    assert excinfo.value.error_msg == json.dumps({"error": "could not connect"})
    assert excinfo.value.status_code == 400


NO_MATCHES_HTML = HTMLString(
    "<HTML><BODY><br>&nbsp;<br>No matches were found for this key!<p></BODY></HTML>"
)


def test_main_no_matches(monkeypatch):
    """
    - GIVEN a word with no entries
    - WHEN the results dict is generated
    - THEN check an empty (successful) result is returned
    """
    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse(NO_MATCHES_HTML)
    )
    assert jdict.main([Kaki("xyzzy")]) == {
        "xyzzy": {
            "success": True,
            "error": None,
            "main_data": {"results": [], "extra": []},
        }
    }


def test_extract_rows_no_matches():
    assert jdict.extract_rows(NO_MATCHES_HTML) == []


def test_extract_rows(test_dict: FullTestDict):
    for word in test_dict.input:
        section = test_dict.jdict.expected_sections[word]
        html = HTMLString(section["html"])
        assert jdict.extract_rows(html) == section["expected_rows"]


@pytest.mark.parametrize(
    "invalid_html",
    [
        pytest.param("", id="empty html"),
        pytest.param("result text", id="just text"),
        pytest.param("<pre>result text", id="only pre"),
        pytest.param("result text</pre>", id="only post"),
    ],
)
def test_extract_rows_failure(invalid_html):
    with pytest.raises(jdict.JDictParsingError) as excinfo:
        jdict.extract_rows(invalid_html)
    assert excinfo.value.error_msg == "could not extract results from html"
    assert excinfo.value.status_code == 400


def test_format_row(test_dict: FullTestDict):
    for word in test_dict.input:
        section = test_dict.jdict.expected_sections[word]
        for row, entry in zip(
            section["expected_rows"], section["expected_entries"], strict=True
        ):
            assert jdict.format_row(row) == entry


@pytest.mark.parametrize(
    "invalid_row",
    [
        "",
        "\n",
        " testwriting) [test reading] /test definition/",
        "testwriting [testreading] test definition",
        "testwriting [testreading] /test definition",
        " [testreading]",
    ],
)
def test_format_row_failure(invalid_row: str):
    with pytest.raises(jdict.JDictParsingError) as excinfo:
        jdict.format_row(invalid_row)
    assert excinfo.value.error_msg == "could not extract results from row"
    assert excinfo.value.status_code == 400


@pytest.mark.parametrize(
    "row,expected",
    [
        pytest.param(
            "眼鏡 [めがね(P);がんきょう;メガネ(P)] /(n) (1) (uk) glasses/eyeglasses"
            "/(n) (2) (めがね, メガネ only) (uk) insight/(P)/EntL1572640X/",
            {
                "writings": ["眼鏡"],
                "readings": ["めがね", "がんきょう", "メガネ"],
                "is_common": True,
                "senses": [
                    {
                        "parts_of_speech": ["n"],
                        "tags": ["uk"],
                        "definitions": ["glasses", "eyeglasses"],
                    },
                    {
                        "parts_of_speech": ["n"],
                        "tags": ["めがね, メガネ only", "uk"],
                        "definitions": ["insight"],
                    },
                ],
            },
            id="multi sense with entry id",
        ),
        pytest.param(
            "カムバック /(n,vs,vi) comeback/",
            {
                "writings": [],
                "readings": ["カムバック"],
                "is_common": False,
                "senses": [
                    {
                        "parts_of_speech": ["n", "vs", "vi"],
                        "tags": [],
                        "definitions": ["comeback"],
                    }
                ],
            },
            id="kana only, single sense",
        ),
        pytest.param(
            "行方(P);行くえ [ゆくえ] /(n) (1) (one's) whereabouts"
            "/(n) (2) destination/(P)/",
            {
                "writings": ["行方", "行くえ"],
                "readings": ["ゆくえ"],
                "is_common": True,
                "senses": [
                    {
                        "parts_of_speech": ["n"],
                        "tags": [],
                        "definitions": ["(one's) whereabouts"],
                    },
                    {
                        "parts_of_speech": ["n"],
                        "tags": [],
                        "definitions": ["destination"],
                    },
                ],
            },
            id="bracketed text kept in definition",
        ),
        pytest.param(
            "牢;籠 [ろう] /(n) (1) prison/(adj-t) (2) (obs) (See 牢として) firm/solid/",
            {
                "writings": ["牢", "籠"],
                "readings": ["ろう"],
                "is_common": False,
                "senses": [
                    {"parts_of_speech": ["n"], "tags": [], "definitions": ["prison"]},
                    {
                        "parts_of_speech": ["adj-t"],
                        "tags": ["obs", "See 牢として"],
                        "definitions": ["firm", "solid"],
                    },
                ],
            },
            id="part of speech changes between senses",
        ),
        pytest.param(
            "学生 [がくせい] /(n) student (esp. a university student)/(P)/",
            {
                "writings": ["学生"],
                "readings": ["がくせい"],
                "is_common": True,
                "senses": [
                    {
                        "parts_of_speech": ["n"],
                        "tags": [],
                        "definitions": ["student (esp. a university student)"],
                    },
                ],
            },
            id="trailing (P) marks entry as common",
        ),
        pytest.param(
            "食べるラー油 [たべるラーゆ] /(exp,n) {food} (See 辣油) chili oil/",
            {
                "writings": ["食べるラー油"],
                "readings": ["たべるラーゆ"],
                "is_common": False,
                "senses": [
                    {
                        "parts_of_speech": ["exp", "n"],
                        "tags": ["food", "See 辣油"],
                        "definitions": ["chili oil"],
                    },
                ],
            },
            id="{field} tags are extracted",
        ),
    ],
)
def test_format_row_examples(row: str, expected):
    assert jdict.format_row(row) == expected


def test_extract_entries(test_dict: FullTestDict):
    for word in test_dict.input:
        section = test_dict.jdict.expected_sections[word]
        assert (
            jdict.extract_entries(HTMLString(section["html"]))
            == section["expected_entries"]
        )


def test_segregate_entries(test_dict: FullTestDict):
    for word in test_dict.input:
        entries = test_dict.jdict.expected_sections[word]["expected_entries"]
        expected_output = test_dict.jdict.expected_output[word]
        main_data = expected_output["main_data"]
        assert jdict.segregate_entries(entries, Kaki(word)) == main_data


def test_entry_is_matching():
    entry = jdict.format_row("成る(P);為る [なる] /(v5r,vi) (uk) to become/(P)/")
    assert jdict.entry_is_matching(entry, Kaki("成る"))
    assert jdict.entry_is_matching(entry, Kaki("為る"))
    assert jdict.entry_is_matching(entry, Kaki("なる"))
    assert not jdict.entry_is_matching(entry, Kaki("成"))
