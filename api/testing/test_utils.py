import json

import pytest  # type: ignore

from api import utils
from api.custom_types.alternative_string_types import URL, HTMLString, Kaki, Yomi


class FakeRequest:
    def __init__(self, words):
        self.args = {"words": json.dumps(words)}


#####################
## TESTS  ###########
#####################


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["hello", "hello"],
        ["dont remove single spaces", "dont remove single spaces"],
        ["remove  double  spaces", "removedoublespaces"],
        ["remove\n\ndouble\n\nnewline", "removedoublenewline"],
        ["remove\n newline\n and\n space", "removenewlineandspace"],
        ["    <div>\n        content\n    </div>", "<div>content</div>"],
    ],
)
def test_make_single_line(input_string, expected_result):
    """
    - GIVEN a string, potentially with extra spaces or newlines
    - WHEN the extra spaces are removed
    - THEN check the final result is as expected
    """
    assert utils.make_single_line(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["", ""],
        ["hello", "hello"],
        ["hello(there)", "hello"],
        ["hello(there)(you)", "hello"],
        ["hello(there) you", "hello"],
        ["hello(there ) you (yesy ou)", "hello"],
    ],
)
def test_remove_end_brackets(input_string, expected_result):
    """
    - GIVEN a string, potentially with brackets
    - WHEN the end brackets are removed
    - THEN check the final result is as expected
    """
    assert utils.remove_end_brackets(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["hello", "hello"],
        ["食べる", "\\u98df\\u3079\\u308b"],
        ["学生", "\\u5b66\\u751f"],
    ],
)
def test_escape_unicode(input_string, expected_result):
    """
    - GIVEN a string
    - WHEN any unicode characters are escaped
    - THEN check they are escaped corrected
    """
    assert utils.escape_unicode(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["hello", "hello"],
        ["\\u98df\\u3079\\u308b", "食べる"],
        ["\\u5b66\\u751f", "学生"],
    ],
)
def test_decode_unicode(input_string, expected_result):
    """
    - GIVEN a string, potentially with escaped unicode characters
    - WHEN the characters are decoded
    - THEN check they are decoded correctly
    """
    assert utils.decode_unicode(input_string) == expected_result


@pytest.mark.parametrize(
    "string_list, expected_output",
    [
        [[], []],
        [["食べる"], [Kaki("食べる")]],
        [["食べる", "学生"], [Kaki("食べる"), Kaki("学生")]],
    ],
)
def test_convert_list_of_str_to_kaki(string_list, expected_output):
    """
    - GIVEN a list of strings
    - WHEN they are all converted to the `Kaki` type
    - THEN check they are all converted correctly
    """
    assert utils.convert_list_of_str_to_kaki(string_list) == expected_output


@pytest.mark.parametrize(
    "string_list, expected_output",
    [
        [[], []],
        [["たべる"], [Yomi("たべる")]],
        [["たべる", "がくせい"], [Yomi("たべる"), Yomi("がくせい")]],
    ],
)
def test_convert_list_of_str_to_yomi(string_list, expected_output):
    """
    - GIVEN a list of strings
    - WHEN they are all converted to the `Yomi` type
    - THEN check they are all converted correctly
    """
    assert utils.convert_list_of_str_to_yomi(string_list) == expected_output


@pytest.mark.parametrize(
    "string_list, expected_output",
    [
        [[], []],
        [["www.test.com"], [URL("www.test.com")]],
        [
            ["www.test.com", "www.test.co.uk"],
            [URL("www.test.com"), URL("www.test.co.uk")],
        ],
    ],
)
def test_convert_list_of_str_to_url(string_list, expected_output):
    """
    - GIVEN a list of strings
    - WHEN they are all converted to the `URL` type
    - THEN check they are all converted correctly
    """
    assert utils.convert_list_of_str_to_url(string_list) == expected_output


@pytest.mark.parametrize(
    "string_list, expected_output",
    [
        [[], []],
        [["<div>hi</div>"], [HTMLString("<div>hi</div>")]],
        [
            ["<div>hi</div>", "<span>a span</span>"],
            [HTMLString("<div>hi</div>"), HTMLString("<span>a span</span>")],
        ],
    ],
)
def test_convert_list_of_str_to_htmlstring(string_list, expected_output):
    """
    - GIVEN a list of strings
    - WHEN they are all converted to the `HTMLString` type
    - THEN check they are all converted correctly
    """
    assert utils.convert_list_of_str_to_htmlstring(string_list) == expected_output


@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        [{}, {}],
        [{"食べる": {}}, {Kaki("食べる"): {}}],
        [{"食べる": "たべる"}, {Kaki("食べる"): "たべる"}],
        [{"食べる": {}, "学生": {}}, {Kaki("食べる"): {}, Kaki("学生"): {}}],
    ],
)
def test_convert_dict_str_keys_to_kaki(input_dict, expected_output):
    """
    - GIVEN a list of dictionaries, with `string` keys
    - WHEN the keys are all converted to the `Kaki` type
    - THEN check they are all converted correctly
    """
    assert utils.convert_dict_str_keys_to_kaki(input_dict) == expected_output
