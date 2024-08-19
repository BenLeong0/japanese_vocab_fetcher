import json

import pytest  # type: ignore

from api import flask_utils


class FakeRequest:
    def __init__(self, words):
        self.args = {"words": json.dumps(words)}


#####################
## TESTS  ###########
#####################


@pytest.mark.parametrize(
    "fake_request, expected_result",
    [
        [FakeRequest([]), []],
        [FakeRequest(["食べる"]), ["食べる"]],
        [FakeRequest(["食べる", "学生"]), ["食べる", "学生"]],
    ],
)
def test_get_words_from_request(fake_request, expected_result):
    """
    - GIVEN an HTTP request
    - WHEN the `word_list` is extracted
    - THEN check it is extracted correctly
    """
    assert flask_utils.get_words_from_request(fake_request) == expected_result


@pytest.mark.parametrize(
    "payload, expected_data",
    [
        [[], "[]"],
        [[{"word": "食べる"}], '[{"word": "食べる"}]'],
        [
            [{"word": "食べる"}, {"word": "学生"}],
            '[{"word": "食べる"}, {"word": "学生"}]',
        ],
        [
            [
                {
                    "word": "食べる",
                    "accent": {"wanikani": ["url1", "url2"]},
                }
            ],
            r'[{"word": "食べる", "accent": {"wanikani": ["url1", "url2"]}}]',
        ],
        ["test_string", '"test_string"'],
        [{"test": "dictionary"}, '{"test": "dictionary"}'],
    ],
)
def test_create_successful_response(payload, expected_data):
    """
    - GIVEN a payload
    - WHEN it is converted into a successful HTTP response
    - THEN check the response has the correct data and status code
    """
    response = flask_utils.create_successful_response(payload)

    assert response.data.decode("unicode-escape") == expected_data
    assert response.status_code == 200


@pytest.mark.parametrize(
    "payload, expected_data",
    [
        [[], "[]"],
        [[{"word": "食べる"}], '[{"word": "食べる"}]'],
        [
            [{"word": "食べる"}, {"word": "学生"}],
            '[{"word": "食べる"}, {"word": "学生"}]',
        ],
        [
            [
                {
                    "word": "食べる",
                    "accent": {"wanikani": ["url1", "url2"]},
                }
            ],
            r'[{"word": "食べる", "accent": {"wanikani": ["url1", "url2"]}}]',
        ],
        ["test_string", '"test_string"'],
        [{"test": "dictionary"}, '{"test": "dictionary"}'],
    ],
)
def test_create_failed_response(payload, expected_data):
    """
    - GIVEN a payload
    - WHEN it is converted into an unsuccessful HTTP response
    - THEN check the response has the correct data and status code
    """
    response = flask_utils.create_failed_response(payload)

    assert response.data.decode("unicode-escape") == expected_data
    assert response.status_code == 400
