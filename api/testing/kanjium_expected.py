"""Expected Kanjium results for every word used in the test dicts"""

from api.custom_types.alternative_string_types import Yomi
from api.custom_types.response_types import ResponseItemKanjium
from testing.dict_typing import KanjiumTestDict

# Excerpt of Kanjium's accents.txt covering the test words (plus a few edge cases)
ACCENTS_PATH = "testing/data/kanjium_accents.txt"


def get_accents_text() -> str:
    with open(ACCENTS_PATH, encoding="utf8") as f:
        return f.read()


ACCENTS: dict[str, list[Yomi]] = {
    "眼鏡": [Yomi("がんきょう"), Yomi("め' がね")],
    "カムバック": [Yomi("カムバ' ック"), Yomi("カ' ムバック")],
    "食べる": [Yomi("たべ' る")],
    "学生": [Yomi("がくしょう"), Yomi("がくせい")],
    "言葉": [Yomi("ことば'")],
    "BADINPUT": [],
    "兎": [Yomi("うさぎ")],
    "行く": [Yomi("いく"), Yomi("ゆく")],
    "籠": [Yomi("かご")],
    "静か": [Yomi("し' ずか")],
    "なる": [],
}


def response(word: str) -> ResponseItemKanjium:
    return {"success": True, "error": None, "main_data": {"accent": ACCENTS[word]}}


OUTPUTS: dict[str, ResponseItemKanjium] = {word: response(word) for word in ACCENTS}


def build_test_dict(words: list[str]) -> KanjiumTestDict:
    return KanjiumTestDict(expected_output={word: OUTPUTS[word] for word in words})
