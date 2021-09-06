# pylint: disable=line-too-long

import pytest

import coordinator
from testing.dicts import TEST_DICTS

test_dict_ids = [test_dict['id'] for test_dict in TEST_DICTS]


class FakeResponse:
    def __init__(self, text):
        self.text = text


@pytest.mark.parametrize(
    "test_dict",
    TEST_DICTS,
    ids=test_dict_ids,
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


@pytest.mark.parametrize(
    "test_dict",
    TEST_DICTS,
    ids=test_dict_ids,
)
def test_generate_response(monkeypatch, test_dict):
    """
    - GIVEN a list of words
    - WHEN full results are generated
    - THEN check the output is as expected
    """
    monkeypatch.setattr("modules.wadoku.get_accent_dict", lambda x: test_dict['wadoku']['expected_output'])
    word_list = test_dict['input']
    expected_result = test_dict['expected_result']

    resp = coordinator.generate_response(
        word_list=word_list,
        ojad_dict=test_dict['ojad']['expected_output'],
        suzuki_dict=test_dict['suzuki']['expected_output'],
        wadoku_dict=test_dict['wadoku']['expected_output'],
    )

    assert resp == expected_result
