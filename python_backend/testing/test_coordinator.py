from collections import defaultdict
from typing import Any, DefaultDict

import pytest   # type: ignore

import coordinator
from custom_types.alternative_string_types import Kaki
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_list_of_str_to_kaki, convert_dict_str_keys_to_kaki


@pytest.fixture(params=TEST_DICTS, ids=lambda d:d['id'])
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
    monkeypatch.setattr("modules.jisho.main", lambda x: test_dict['jisho']['expected_output'])
    monkeypatch.setattr("modules.ojad.main", lambda x: test_dict['ojad']['expected_output'])
    monkeypatch.setattr("modules.suzuki.main", lambda x: test_dict['suzuki']['expected_output'])
    monkeypatch.setattr("modules.wadoku.main", lambda x: test_dict['wadoku']['expected_output'])
    monkeypatch.setattr("modules.forvo.main", lambda x: test_dict['forvo']['expected_output'])
    monkeypatch.setattr("modules.wanikani.main", lambda x: test_dict['wanikani']['expected_output'])

    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_result = test_dict['expected_result']

    assert coordinator.get_info(word_list) == expected_result


def test_generate_results_dict(monkeypatch, test_dict):
    """
    - GIVEN a list of words
    - WHEN the results dict is generated
    - THEN check the output is as expected
    """
    monkeypatch.setattr("modules.jisho.main", lambda x: test_dict['jisho']['expected_output'])
    monkeypatch.setattr("modules.ojad.main", lambda x: test_dict['ojad']['expected_output'])
    monkeypatch.setattr("modules.suzuki.main", lambda x: test_dict['suzuki']['expected_output'])
    monkeypatch.setattr("modules.wadoku.main", lambda x: test_dict['wadoku']['expected_output'])
    monkeypatch.setattr("modules.forvo.main", lambda x: test_dict['forvo']['expected_output'])
    monkeypatch.setattr("modules.wanikani.main", lambda x: test_dict['wanikani']['expected_output'])

    word_list = convert_list_of_str_to_kaki(test_dict['input'])

    expected_result_dict = defaultdict(dict,
        {
            module: test_dict[module]['expected_output']
            for module in MODULES
        }
    )

    assert coordinator.generate_results_dict(word_list) == expected_result_dict



def test_generate_response(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN full results are generated
    - THEN check the output is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    result_dict: DefaultDict[str, dict[Kaki, Any]] = defaultdict(dict, {
        "jisho": convert_dict_str_keys_to_kaki(test_dict["jisho"]['expected_output']),
        "ojad": convert_dict_str_keys_to_kaki(test_dict["ojad"]['expected_output']),
        "suzuki": convert_dict_str_keys_to_kaki(test_dict["suzuki"]['expected_output']),
        "wadoku": convert_dict_str_keys_to_kaki(test_dict["wadoku"]['expected_output']),
        "forvo": convert_dict_str_keys_to_kaki(test_dict["forvo"]['expected_output']),
        "wanikani": convert_dict_str_keys_to_kaki(test_dict["wanikani"]['expected_output']),
    })

    expected_result = test_dict['expected_result']

    assert coordinator.generate_response(result_dict, word_list) == expected_result
