import json

import pytest   # type: ignore

from custom_types.alternative_string_types import HTMLString, Kaki, URL, Yomi
import utils


class FakeRequest:
    def __init__(self, words):
        self.data = json.dumps({"words": words})


@pytest.mark.parametrize(
    "fake_request, expected_result",
    [
        [FakeRequest([]), []],
        [FakeRequest(["食べる"]), ["食べる"]],
        [FakeRequest(["食べる", "学生"]), ["食べる", "学生"]],
    ]
)
def test_get_words_from_request(fake_request, expected_result):
    """
    - GIVEN an HTTP request
    - WHEN the `word_list` is extracted
    - THEN check it is extracted correctly
    """
    assert utils.get_words_from_request(fake_request) == expected_result


@pytest.mark.parametrize(
    "payload, expected_data",
    [
        [[], '[]'],
        [[{"word": "食べる"}], '[{"word": "食べる"}]'],
        [[{"word": "食べる"}, {"word": "学生"}], '[{"word": "食べる"}, {"word": "学生"}]'],
        [
            [
                {
                    "word": "食べる",
                    "accent": {
                        "wanikani": ["url1", "url2"]
                    },
                }
            ],
            r'[{"word": "食べる", "accent": {"wanikani": ["url1", "url2"]}}]'
        ],
        ["test_string", '"test_string"'],
        [{"test": "dictionary"}, '{"test": "dictionary"}'],
    ]
)
def test_create_successful_response(payload, expected_data):
    """
    - GIVEN a payload
    - WHEN it is converted into a successful HTTP response
    - THEN check the response has the correct data and status code
    """
    response = utils.create_successful_response(payload)

    assert response.data.decode("unicode-escape") == expected_data
    assert response.status_code == 200


@pytest.mark.parametrize(
    "payload, expected_data",
    [
        [[], '[]'],
        [[{"word": "食べる"}], '[{"word": "食べる"}]'],
        [[{"word": "食べる"}, {"word": "学生"}], '[{"word": "食べる"}, {"word": "学生"}]'],
        [
            [
                {
                    "word": "食べる",
                    "accent": {
                        "wanikani": ["url1", "url2"]
                    },
                }
            ],
            r'[{"word": "食べる", "accent": {"wanikani": ["url1", "url2"]}}]'
        ],
        ["test_string", '"test_string"'],
        [{"test": "dictionary"}, '{"test": "dictionary"}'],
    ]
)
def test_create_failed_response(payload, expected_data):
    """
    - GIVEN a payload
    - WHEN it is converted into an unsuccessful HTTP response
    - THEN check the response has the correct data and status code
    """
    response = utils.create_failed_response(payload)

    assert response.data.decode("unicode-escape") == expected_data
    assert response.status_code == 400


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["hello", "hello"],
        ["dont remove single spaces", "dont remove single spaces"],
        ["remove  double  spaces", "removedoublespaces"],
        ["remove\n\ndouble\n\nnewline", "removedoublenewline"],
        ["remove\n newline\n and\n space", "removenewlineandspace"],
        ["    <div>\n        content\n    </div>", "<div>content</div>"],
    ]
)
def test_make_single_line(input_string, expected_result):
    """
    - GIVEN a string, potentially with extra spaces or newlines
    - WHEN the extrea spaces are removed
    - THEN check the final result is as expected
    """
    assert utils.make_single_line(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["hello", "hello"],
        ["食べる", "\\u98df\\u3079\\u308b"],
        ["学生", "\\u5b66\\u751f"],
    ]
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
    ]
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
    ]
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
    ]
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
        [["www.test.com", "www.test.co.uk"], [URL("www.test.com"), URL("www.test.co.uk")]],
    ]
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
        [["<div>hi</div>", "<span>a span</span>"], [HTMLString("<div>hi</div>"), HTMLString("<span>a span</span>")]],
    ]
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
        [
            {"食べる": {}},
            {Kaki("食べる"): {}}
        ],
        [
            {"食べる": "たべる"},
            {Kaki("食べる"): "たべる"}
        ],
        [
            {"食べる": {}, "学生": {}},
            {Kaki("食べる"): {}, Kaki("学生"): {}}
        ],
    ]
)
def test_convert_dict_str_keys_to_kaki(input_dict, expected_output):
    """
    - GIVEN a list of dictionaries, with `string` keys
    - WHEN the keys are all converted to the `Kaki` type
    - THEN check they are all converted correctly
    """
    assert utils.convert_dict_str_keys_to_kaki(input_dict) == expected_output
