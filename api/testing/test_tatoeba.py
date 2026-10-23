import json

import pytest  # type: ignore

from api.custom_types.alternative_string_types import URL, Kaki
from api.custom_types.tatoeba_api_types import TatoebaAPIResult
from api.modules import tatoeba
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


BASE_URL = "https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query="


def build_result(
    direct_translations: list[str], indirect_translations: list[str]
) -> TatoebaAPIResult:
    return {
        "id": 1,
        "text": "日本語の文",
        "lang": "jpn",
        "correctness": 0,
        "script": None,
        "license": "CC BY 2.0 FR",
        "translations": [
            [{"text": text} for text in direct_translations],
            [{"text": text} for text in indirect_translations],
        ],
        "transcriptions": [],
        "audios": [],
        "user": {"username": "user"},
        "lang_name": "Japanese",
        "dir": "ltr",
        "lang_tag": "ja",
        "is_favorite": None,
        "is_owned_by_current_user": False,
        "permissions": None,
        "current_user_review": None,
    }


#####################
## TESTS  ###########
#####################


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the sentences dict is generated
    - THEN check all the tatoeba info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.tatoeba.expected_sections
    expected_output = test_dict.tatoeba.expected_output
    words_by_url = {sections[word]["url"]: word for word in word_list}

    def get_api_response(url: URL) -> str:
        return json.dumps(sections[words_by_url[url]]["api_response"])

    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse(get_api_response(url))
    )
    assert tatoeba.main(word_list) == expected_output


def test_main_api_error(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the API returns an unsuccessful status code
    - THEN check the failed dict is returned as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    response = json.dumps({"error": "api_error"})
    sections = test_dict.tatoeba.expected_sections
    expected_output = {
        word: {
            "success": False,
            "error": {
                "error_msg": json.dumps({"error": "api_error"}),
                "status_code": 400,
                "url": sections[word]["url"],
            },
            "main_data": {
                "sentences": [],
            },
        }
        for word in word_list
    }

    monkeypatch.setattr(
        "requests.get", lambda x, timeout: FakeResponse(response, status_code=400)
    )
    assert tatoeba.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN a sentences dictionary is generated
    - THEN check it returns and empty dict
    """
    assert tatoeba.main([]) == {}


def test_get_sentences(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the sentences are fetched for each individual word
    - THEN check the sentences are correct
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.tatoeba.expected_sections
    full_expected_output = test_dict.tatoeba.expected_output

    for word in word_list:
        api_response = json.dumps(sections[word]["api_response"])
        monkeypatch.setattr(
            "requests.get", lambda url, timeout: FakeResponse(api_response)
        )
        assert tatoeba.get_sentences(word) == full_expected_output[word]


@pytest.mark.parametrize(
    "word, expected_query",
    [
        pytest.param(Kaki(""), "", id="Empty"),
        pytest.param(Kaki("踵"), "踵", id="Single Char"),
        pytest.param(Kaki("面白い"), "面白", id="I-adjective 1"),
        pytest.param(Kaki("赤い"), "赤", id="I-adjective 2"),
        pytest.param(Kaki("みる"), "み", id="Ichidan 1"),
        pytest.param(Kaki("変える"), "変え", id="Ichidan 2"),
        pytest.param(Kaki("したためる"), "したため", id="Ichidan 3"),
        pytest.param(Kaki("食べる"), "食べ", id="Ichidan 4"),
        pytest.param(
            Kaki("帰る"),
            "帰ら%22|%22帰り%22|%22帰る%22|%22帰れ%22|%22帰ろ%22|%22帰っ",
            id="Godan 1",
        ),
        pytest.param(
            Kaki("合う"),
            "合わ%22|%22合い%22|%22合う%22|%22合え%22|%22合お%22|%22合っ",
            id="Godan 2",
        ),
        pytest.param(
            Kaki("残す"),
            "残さ%22|%22残し%22|%22残す%22|%22残せ%22|%22残そ",
            id="Godan 3",
        ),
        pytest.param(Kaki("活殺自在"), "活殺自在", id="Non-verb 1"),
        pytest.param(Kaki("眼鏡"), "眼鏡", id="Non-verb 2"),
    ],
)
def test_get_url_query(word: Kaki, expected_query: str):
    """
    - GIVEN a word
    - WHEN the search query is generated
    - THEN check all the conjugations are included
    """
    assert tatoeba.get_url_query(word) == expected_query


@pytest.mark.parametrize(
    "word, expected_url",
    [
        pytest.param(Kaki(""), URL(BASE_URL + "%3D%22%22"), id="Empty"),
        pytest.param(Kaki("変える"), URL(BASE_URL + "%3D%22変え%22"), id="Ichidan"),
        pytest.param(
            Kaki("残す"),
            URL(BASE_URL + "%3D%22残さ%22|%22残し%22|%22残す%22|%22残せ%22|%22残そ%22"),
            id="Godan",
        ),
        pytest.param(
            Kaki("活殺自在"), URL(BASE_URL + "%3D%22活殺自在%22"), id="Non-verb"
        ),
    ],
)
def test_get_url_parametrized(word: Kaki, expected_url: URL):
    """
    - GIVEN a word
    - WHEN a url is generated
    - THEN check the query is wrapped in an exact-match search
    """
    assert tatoeba.get_url(word) == expected_url


def test_get_url(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN a url is generated
    - THEN check the url is encoded
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.tatoeba.expected_sections

    for word in word_list:
        assert tatoeba.get_url(word) == sections[word]["url"]


def test_call_api(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN an API URL
    - WHEN the API is called
    - THEN check the response is handled correctly
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.tatoeba.expected_sections

    for word in word_list:
        api_response = sections[word]["api_response"]
        monkeypatch.setattr(
            "requests.get",
            lambda url, timeout: FakeResponse(json.dumps(api_response)),
        )
        assert tatoeba.call_api(word) == api_response


def test_call_api_failure(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN an unsuccessful HTTP request is made
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.tatoeba.expected_sections
    response = json.dumps({"error": "could not connect"})
    monkeypatch.setattr(
        "requests.get", lambda url, timeout: FakeResponse(response, status_code=400)
    )

    for word in word_list:
        with pytest.raises(tatoeba.TatoebaAPIError) as api_error:
            tatoeba.call_api(word)
        assert api_error.value.error_msg == json.dumps({"error": "could not connect"})
        assert api_error.value.status_code == 400
        assert api_error.value.url == sections[word]["url"]


def test_call_api_request_exception(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the HTTP request itself raises
    - THEN check an exception is thrown
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)

    def raise_error(url, timeout):
        raise ConnectionError("site is down")

    monkeypatch.setattr("requests.get", raise_error)

    for word in word_list:
        with pytest.raises(tatoeba.TatoebaAPIError) as api_error:
            tatoeba.call_api(word)
        assert api_error.value.error_msg == "request failed"
        assert api_error.value.status_code == 500


@pytest.mark.parametrize(
    "result, expected_sentence",
    [
        pytest.param(
            build_result(["Direct"], ["Indirect"]),
            {"ja": "日本語の文", "en": "Direct"},
            id="direct translation preferred",
        ),
        pytest.param(
            build_result(["Direct 1", "Direct 2"], []),
            {"ja": "日本語の文", "en": "Direct 1"},
            id="first direct translation",
        ),
        pytest.param(
            build_result([], ["Indirect"]),
            {"ja": "日本語の文", "en": "Indirect"},
            id="indirect fallback",
        ),
        pytest.param(build_result([], []), None, id="no translations"),
    ],
)
def test_extract_sentence(result: TatoebaAPIResult, expected_sentence):
    """
    - GIVEN a result from the Tatoeba API
    - WHEN the sentence is extracted
    - THEN check the first available translation is used
    """
    assert tatoeba.extract_sentence(result) == expected_sentence


def test_extract_sentences(test_dict: FullTestDict):
    """
    - GIVEN an API response
    - WHEN the sentences are extracted
    - THEN check the array of sentences is correct for each word
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    sections = test_dict.tatoeba.expected_sections
    expected_output = test_dict.tatoeba.expected_output

    for word in word_list:
        api_response = sections[word]["api_response"]
        expected_sentences = expected_output[word]["main_data"]["sentences"]
        assert tatoeba.extract_sentences(api_response) == expected_sentences
