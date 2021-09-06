# pylint: disable=line-too-long

import pytest

import coordinator
from testing.dicts import TEST_DICTS, TEST_DICT_IDS


@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


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