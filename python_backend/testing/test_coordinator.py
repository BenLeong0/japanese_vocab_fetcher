from collections import defaultdict
import pytest

import coordinator
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS


@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


MODULES = (
    "jisho",
    "ojad",
    "suzuki",
    "wadoku",
    "forvo",
    "wanikani",
)


# Ensure no actual requests are being made
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


def test_get_info(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN full results are generated
    - THEN check the output is as expected
    """
    monkeypatch.setattr("modules.ojad.get_accent_dict", lambda x: test_dict['ojad']['expected_output'])
    monkeypatch.setattr("modules.suzuki.get_accent_dict", lambda x: test_dict['suzuki']['expected_output'])
    monkeypatch.setattr("modules.wadoku.get_accent_dict", lambda x: test_dict['wadoku']['expected_output'])
    word_list = test_dict['input']
    expected_result = test_dict['expected_result']

    assert coordinator.get_info(word_list) == expected_result


def test_generate_results_dict(monkeypatch, test_dict):
    """
    - GIVEN a list of words
    - WHEN the results dict is generated
    - THEN check the output is as expected
    """
    monkeypatch.setattr("modules.ojad.get_accent_dict", lambda x: test_dict['ojad']['expected_output'])
    monkeypatch.setattr("modules.suzuki.get_accent_dict", lambda x: test_dict['suzuki']['expected_output'])
    monkeypatch.setattr("modules.wadoku.get_accent_dict", lambda x: test_dict['wadoku']['expected_output'])
    word_list = test_dict['input']



def test_generate_response(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN full results are generated
    - THEN check the output is as expected
    """
    word_list = test_dict['input']
    result_dict = defaultdict(dict,
        {
            module: test_dict[module]['expected_output']
            for module in MODULES
        }
    )

    expected_result = test_dict['expected_result']

    assert coordinator.generate_response(result_dict, word_list) == expected_result
