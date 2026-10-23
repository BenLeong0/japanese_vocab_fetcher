from collections import defaultdict
from typing import Any

import pytest  # type: ignore

from api import coordinator
from api.custom_types.alternative_string_types import Kaki
from api.utils import convert_dict_str_keys_to_kaki, convert_list_of_str_to_kaki
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS


@pytest.fixture(name="test_dict", params=TEST_DICTS, ids=lambda d: d.test_name)
def fixture_test_dict(request):
    return request.param


MODULES = (
    "japanesepod",
    "jisho",
    "ojad",
    "suzuki",
    "wadoku",
    "forvo",
    "tatoeba",
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
    monkeypatch.setattr(
        "api.modules.japanesepod.main", lambda x: test_dict.japanesepod.expected_output
    )
    monkeypatch.setattr(
        "api.modules.jisho.main", lambda x: test_dict.jisho.expected_output
    )
    monkeypatch.setattr(
        "api.modules.ojad.main", lambda x: test_dict.ojad.expected_output
    )
    monkeypatch.setattr(
        "api.modules.suzuki.main", lambda x: test_dict.suzuki.expected_output
    )
    monkeypatch.setattr(
        "api.modules.wadoku.main", lambda x: test_dict.wadoku.expected_output
    )
    monkeypatch.setattr(
        "api.modules.forvo.main", lambda x: test_dict.forvo.expected_output
    )
    monkeypatch.setattr(
        "api.modules.tatoeba.main", lambda x: test_dict.tatoeba.expected_output
    )
    monkeypatch.setattr(
        "api.modules.wanikani.main", lambda x: test_dict.wanikani.expected_output
    )

    word_list = convert_list_of_str_to_kaki(test_dict.input)
    expected_result = test_dict.expected_result

    assert coordinator.get_info(word_list) == expected_result


def test_generate_results_dict(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the results dict is generated
    - THEN check the output is as expected
    """
    monkeypatch.setattr(
        "api.modules.japanesepod.main", lambda x: test_dict.japanesepod.expected_output
    )
    monkeypatch.setattr(
        "api.modules.jisho.main", lambda x: test_dict.jisho.expected_output
    )
    monkeypatch.setattr(
        "api.modules.ojad.main", lambda x: test_dict.ojad.expected_output
    )
    monkeypatch.setattr(
        "api.modules.suzuki.main", lambda x: test_dict.suzuki.expected_output
    )
    monkeypatch.setattr(
        "api.modules.wadoku.main", lambda x: test_dict.wadoku.expected_output
    )
    monkeypatch.setattr(
        "api.modules.forvo.main", lambda x: test_dict.forvo.expected_output
    )
    monkeypatch.setattr(
        "api.modules.tatoeba.main", lambda x: test_dict.tatoeba.expected_output
    )
    monkeypatch.setattr(
        "api.modules.wanikani.main", lambda x: test_dict.wanikani.expected_output
    )

    word_list = convert_list_of_str_to_kaki(test_dict.input)

    expected_result_dict: defaultdict[str, dict] = defaultdict(
        dict,
        {
            "japanesepod": test_dict.japanesepod.expected_output,
            "jisho": test_dict.jisho.expected_output,
            "ojad": test_dict.ojad.expected_output,
            "suzuki": test_dict.suzuki.expected_output,
            "wadoku": test_dict.wadoku.expected_output,
            "forvo": test_dict.forvo.expected_output,
            "tatoeba": test_dict.tatoeba.expected_output,
            "wanikani": test_dict.wanikani.expected_output,
        },
    )

    assert coordinator.generate_results_dict(word_list) == expected_result_dict


def test_generate_response(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN full results are generated
    - THEN check the output is as expected
    """
    word_list = convert_list_of_str_to_kaki(test_dict.input)
    result_dict: defaultdict[str, dict[Kaki, Any]] = defaultdict(
        dict,
        {
            "japanesepod": convert_dict_str_keys_to_kaki(
                test_dict.japanesepod.expected_output
            ),
            "jisho": convert_dict_str_keys_to_kaki(test_dict.jisho.expected_output),
            "ojad": convert_dict_str_keys_to_kaki(test_dict.ojad.expected_output),
            "suzuki": convert_dict_str_keys_to_kaki(test_dict.suzuki.expected_output),
            "wadoku": convert_dict_str_keys_to_kaki(test_dict.wadoku.expected_output),
            "forvo": convert_dict_str_keys_to_kaki(test_dict.forvo.expected_output),
            "tatoeba": convert_dict_str_keys_to_kaki(test_dict.tatoeba.expected_output),
            "wanikani": convert_dict_str_keys_to_kaki(
                test_dict.wanikani.expected_output
            ),
        },
    )

    expected_result = test_dict.expected_result

    assert coordinator.generate_response(result_dict, word_list) == expected_result


def test_get_modules_all():
    """
    - GIVEN no sources
    - WHEN modules are selected
    - THEN check all modules are returned
    """
    assert coordinator.get_modules(None) == coordinator.MODULES


def test_get_modules_subset():
    """
    - GIVEN a subset of sources
    - WHEN modules are selected
    - THEN check only those modules are returned
    """
    modules = coordinator.get_modules(["ojad", "jisho"])
    assert [module.NAME for module in modules] == ["jisho", "ojad"]


def test_get_modules_unknown():
    """
    - GIVEN an unknown source
    - WHEN modules are selected
    - THEN check a ValueError is raised
    """
    with pytest.raises(ValueError, match="notasource"):
        coordinator.get_modules(["jisho", "notasource"])


def test_get_info_with_sources(monkeypatch, test_dict: FullTestDict):
    """
    - GIVEN a list of words and a subset of sources
    - WHEN results are generated
    - THEN check only the requested sources are called and returned
    """
    monkeypatch.setattr(
        "api.modules.jisho.main", lambda x: test_dict.jisho.expected_output
    )
    monkeypatch.setattr(
        "api.modules.ojad.main", lambda x: test_dict.ojad.expected_output
    )
    for name in set(MODULES) - {"jisho", "ojad"}:
        monkeypatch.setattr(f"api.modules.{name}.main", pytest.fail)

    word_list = convert_list_of_str_to_kaki(test_dict.input)
    expected_result = [
        {"word": item["word"], "jisho": item["jisho"], "ojad": item["ojad"]}
        for item in test_dict.expected_result
    ]

    assert coordinator.get_info(word_list, ["ojad", "jisho"]) == expected_result
