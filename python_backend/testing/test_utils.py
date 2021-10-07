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
