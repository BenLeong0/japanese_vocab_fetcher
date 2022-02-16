import pytest  # type: ignore

from custom_types.alternative_string_types import Kaki
from modules import tatoeba
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=lambda d:d['id'])
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text, status_code=200, error=""):
        self.text = text
        self.status_code = status_code


#####################
## TESTS  ###########
#####################

def test_main(test_dict: FullTestDict):
    """
    - GIVEN a list of words
    - WHEN the accent dict is generated
    - THEN check all the tatoeba info is correct and complete
    """
    word_list = convert_list_of_str_to_kaki(test_dict['input'])
    expected_output = test_dict['tatoeba']['expected_output']

    assert tatoeba.main(word_list) == expected_output


def test_empty_input():
    """
    - GIVEN an empty input
    - WHEN an accent dictionary is generated
    - THEN check it returns and empty dict
    """
    assert tatoeba.main([]) == {}


@pytest.mark.parametrize(
    "word, expected_query",
    [
        pytest.param(Kaki(""), "", id="Empty"),
        pytest.param(Kaki("踵"), "踵", id="Single Char"),
        pytest.param(Kaki("みる"), "み", id="Ichidan1"),
        pytest.param(Kaki("変える"), "変え", id="Ichidan2"),
        pytest.param(Kaki("したためる"), "したため", id="Ichidan3"),
        pytest.param(Kaki("帰る"), "帰ら|帰り|帰る|帰れ|帰ろ|帰っ", id="Godan1"),
        pytest.param(Kaki("合う"), "合わ|合い|合う|合え|合お|合っ", id="Godan2"),
        pytest.param(Kaki("残す"), "残さ|残し|残す|残せ|残そ", id="Godan3"),
        pytest.param(Kaki("活殺自在"), "活殺自在", id="Nonverb1"),
        pytest.param(Kaki("眼鏡"), "眼鏡", id="Nonverb2"),
    ]
)
def test_get_url_query(word: Kaki, expected_query: str):
    assert tatoeba.get_url_query(word) == expected_query
