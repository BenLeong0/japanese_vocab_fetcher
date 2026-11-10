import pytest  # type: ignore

from api.custom_types.alternative_string_types import Kaki, Yomi
from api.modules import nhk


# Ensure no actual requests are being made
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.mark.parametrize(
    "word, expected",
    [
        ("眼鏡", ["め' がね"]),  # 頭高
        ("食べる", ["たべ' る"]),  # 中高
        ("言葉", ["ことば'"]),  # 尾高
        ("学生", ["がくせい"]),  # 平板
        ("今日", ["きょ' う", "こ' んにち"]),  # 拗音
        ("学校", ["がっこう"]),  # standard spelling preferred over がっこー
        ("カムバック", ["かむば' っく", "か' むばっく"]),  # katakana
        (
            "相容れない",
            ["あ' いいれない", "あ' い・いれない"],
        ),  # multiple accent phrases
    ],
)
def test_main(word: str, expected: list[str]):
    """
    - GIVEN a word in the NHK dictionary
    - WHEN its accent is looked up
    - THEN check the accents are as expected
    """
    result = nhk.main([Kaki(word)])
    assert result == {word: nhk.response_factory(list(map(Yomi, expected)))}


def test_main_kana_input():
    """
    - GIVEN a word written in kana
    - WHEN its accent is looked up
    - THEN check the accents of words with that reading are included
    """
    result = nhk.main([Kaki("はし")])
    assert result["はし"]["main_data"]["accent"] == ["は' し", "はし", "はし'"]

    result = nhk.main([Kaki("たべる")])
    assert result["たべる"]["main_data"]["accent"] == ["たべ' る"]


def test_main_multiple_words():
    result = nhk.main([Kaki("眼鏡"), Kaki("BADINPUT"), Kaki("学生")])
    assert result == {
        "眼鏡": nhk.response_factory([Yomi("め' がね")]),
        "BADINPUT": nhk.response_factory(),
        "学生": nhk.response_factory([Yomi("がくせい")]),
    }


def test_main_empty():
    assert nhk.main([]) == {}


def test_main_load_error(monkeypatch):
    """
    - GIVEN the data file fails to load
    - WHEN accents are looked up
    - THEN check an error response is returned for each word
    """

    def fail():
        raise OSError("missing")

    monkeypatch.setattr(nhk, "load_indices", fail)
    result = nhk.main([Kaki("眼鏡")])
    assert result["眼鏡"]["success"] is False
    assert result["眼鏡"]["main_data"]["accent"] == []
    assert result["眼鏡"]["error"] is not None


def test_build_indices():
    lines = ["端\tは' し", "端\tはし", "箸\tは' し", "はし\tは' し"]
    word_index, reading_index = nhk.build_indices(lines)
    assert word_index == {
        "端": ["は' し", "はし"],
        "箸": ["は' し"],
        "はし": ["は' し"],
    }
    assert reading_index == {"はし": ["は' し", "はし"]}


@pytest.mark.parametrize(
    "accent, reading",
    [
        ("め' がね", "めがね"),
        ("がくせい", "がくせい"),
        ("あ' い・いれない", "あいいれない"),
    ],
)
def test_accent_to_reading(accent: str, reading: str):
    assert nhk.accent_to_reading(accent) == reading


@pytest.mark.parametrize(
    "word, expected",
    [
        ("はし", True),
        ("カムバック", True),
        ("コンピューター", True),
        ("箸", False),
        ("食べる", False),
    ],
)
def test_is_kana(word: str, expected: bool):
    assert nhk.is_kana(word) is expected
