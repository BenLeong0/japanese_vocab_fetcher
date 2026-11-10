import pytest  # type: ignore

from api.custom_types.alternative_string_types import Kaki, Yomi
from api.modules import kanjium
from api.utils import convert_list_of_str_to_kaki
from testing import kanjium_expected
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(name="test_dict", params=TEST_DICTS, ids=lambda d: d.test_name)
def fixture_test_dict(request):
    return request.param


@pytest.fixture(autouse=True)
def reset_cache(monkeypatch):
    monkeypatch.setattr(kanjium, "_accent_dict", None)


class FakeResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
        self.encoding = None


def fake_get(text, status_code=200):
    def get(url, timeout):
        assert url == kanjium.ACCENTS_URL
        return FakeResponse(text, status_code)

    return get


#####################
## TESTS  ###########
#####################


def test_main(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the kanjium info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    monkeypatch.setattr("requests.get", fake_get(kanjium_expected.get_accents_text()))
    assert kanjium.main(word_list) == test_dict.kanjium.expected_output


def test_main_empty():
    assert kanjium.main([]) == {}


def test_main_caches_data(monkeypatch):
    """
    - GIVEN the data has already been fetched
    - WHEN main is called again
    - THEN no new request is made
    """
    calls = []

    def get(url, timeout):
        calls.append(url)
        return FakeResponse(kanjium_expected.get_accents_text())

    monkeypatch.setattr("requests.get", get)
    word_list = convert_list_of_str_to_kaki(["食べる"])
    kanjium.main(word_list)
    kanjium.main(word_list)
    assert len(calls) == 1


@pytest.mark.parametrize("status_code", [404, 500])
def test_main_bad_status(monkeypatch, status_code):
    """
    - GIVEN the data file request fails
    - WHEN main is called
    - THEN every word gets an error response, and the failure isn't cached
    """
    monkeypatch.setattr("requests.get", fake_get("Not Found", status_code))
    word_list = convert_list_of_str_to_kaki(["食べる", "学生"])
    error_response = {
        "success": False,
        "error": {
            "error_msg": "Not Found",
            "status_code": status_code,
            "url": kanjium.ACCENTS_URL,
        },
        "main_data": {"accent": []},
    }
    assert kanjium.main(word_list) == {
        "食べる": error_response,
        "学生": error_response,
    }
    assert kanjium._accent_dict is None


def test_main_request_exception(monkeypatch):
    def get(url, timeout):
        raise ConnectionError

    monkeypatch.setattr("requests.get", get)
    result = kanjium.main(convert_list_of_str_to_kaki(["食べる"]))[Kaki("食べる")]
    assert result["success"] is False
    assert result["error"] is not None
    assert result["error"]["error_msg"] == "request failed"


def test_main_normalises_full_width():
    """Words with half-width digits match Kanjium's full-width entries"""
    accent_dict = kanjium.build_accent_dict(kanjium_expected.get_accents_text())
    kanjium._accent_dict = accent_dict
    result = kanjium.main(convert_list_of_str_to_kaki(["10月", "2つ"]))
    assert result[Kaki("10月")]["main_data"]["accent"] == [
        Yomi("じゅうがつ'"),
        Yomi("じゅうがつ"),
    ]
    assert result[Kaki("2つ")]["main_data"]["accent"] == [
        Yomi("ふたつ"),
        Yomi("ふたつ'"),
    ]


@pytest.mark.parametrize(
    "accent_field, expected",
    [
        ("0", [0]),
        ("3,1", [3, 1]),
        ("(副)0,(名)3", [0, 3]),
        ("(名)2,(代)2,0", [2, 0]),
        ("(名;形動)1", [1]),
        ("", []),
    ],
)
def test_parse_accent_field(accent_field, expected):
    assert kanjium.parse_accent_field(accent_field) == expected


@pytest.mark.parametrize(
    "reading, expected",
    [
        ("たべる", ["た", "べ", "る"]),
        ("きょう", ["きょ", "う"]),
        ("がっこう", ["が", "っ", "こ", "う"]),
        ("シャワー", ["シャ", "ワ", "ー"]),
    ],
)
def test_split_moras(reading, expected):
    assert kanjium.split_moras(reading) == expected


@pytest.mark.parametrize(
    "reading, position, expected",
    [
        ("がんきょう", 0, "がんきょう"),
        ("めがね", 1, "め' がね"),
        ("たべる", 2, "たべ' る"),
        ("ことば", 3, "ことば'"),
        ("きょう", 1, "きょ' う"),
        ("きょう", 3, None),
    ],
)
def test_format_accent(reading, position, expected):
    assert kanjium.format_accent(reading, position) == expected


def test_build_accent_dict_kana_word():
    """Kana-only words have an empty reading column"""
    accent_dict = kanjium.build_accent_dict("かさかさ\t\t(副)1,(形動)0\n")
    assert accent_dict == {"かさかさ": [Yomi("か' さかさ"), Yomi("かさかさ")]}
