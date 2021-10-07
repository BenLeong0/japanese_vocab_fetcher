import json
import pytest   # type: ignore

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
    response = utils.create_successful_response(payload)

    assert response.data.decode("unicode-escape") == expected_data
    assert response.status == "200 OK"


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
    response = utils.create_failed_response(payload)

    assert response.data.decode("unicode-escape") == expected_data
    assert response.status == "400 BAD REQUEST"


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["hello", "hello"],
        ["dont remove single spaces", "dont remove single spaces"],
        ["remove  double  spaces", "removedoublespaces"],
        ["remove\n\ndouble\n\nnewline", "removedoublenewline"],
        ["remove\n newline\n and\n space", "removenewlineandspace"],
    ]
)
def test_make_single_line(input_string, expected_result):
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
    assert utils.decode_unicode(input_string) == expected_result
