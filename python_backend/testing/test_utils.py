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
