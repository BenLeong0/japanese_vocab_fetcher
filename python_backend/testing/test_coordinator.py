# pylint: disable=line-too-long

import pytest

import coordinator
from testing.dicts import (
    MEGANE,
    COMEBACK,
    TABERU_GAKUSEI,
    KOTOBA,
)


class FakeResponse:
    def __init__(self, text):
        self.text = text


@pytest.mark.parametrize(
    "test_dict",
    [
        MEGANE,
        COMEBACK,
        TABERU_GAKUSEI,
        KOTOBA,
    ]
)
def test_get_info(monkeypatch, test_dict):
    """
    - GIVEN a list of words
    - WHEN full results are generated
    - THEN check the output is as expected
    """
    monkeypatch.setattr("modules.wadoku.get_accent_dict", lambda x: test_dict['wadoku']['expected_output'])
    word_list = test_dict['input']
    expected_result = test_dict['expected_result']

    assert coordinator.get_info(word_list) == expected_result
