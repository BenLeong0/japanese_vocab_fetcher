import pytest  # type: ignore

from custom_types.alternative_string_types import Kaki, URL
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
        pytest.param(Kaki("面白い"), "面白", id="Ichidan1"),
        pytest.param(Kaki("赤い"), "赤", id="Ichidan1"),
        pytest.param(Kaki("みる"), "み", id="Ichidan1"),
        pytest.param(Kaki("変える"), "変え", id="Ichidan2"),
        pytest.param(Kaki("したためる"), "したため", id="Ichidan3"),
        pytest.param(Kaki("帰る"), "帰ら%22|%22帰り%22|%22帰る%22|%22帰れ%22|%22帰ろ%22|%22帰っ", id="Godan1"),
        pytest.param(Kaki("合う"), "合わ%22|%22合い%22|%22合う%22|%22合え%22|%22合お%22|%22合っ", id="Godan2"),
        pytest.param(Kaki("残す"), "残さ%22|%22残し%22|%22残す%22|%22残せ%22|%22残そ", id="Godan3"),
        pytest.param(Kaki("活殺自在"), "活殺自在", id="Nonverb1"),
        pytest.param(Kaki("眼鏡"), "眼鏡", id="Nonverb2"),
    ]
)
def test_get_url_query(word: Kaki, expected_query: str):
    assert tatoeba.get_url_query(word) == expected_query



@pytest.mark.parametrize(
    "word, expected_url",
    [
        pytest.param(Kaki(""), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22%22"), id="Empty"),
        pytest.param(Kaki("踵"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22踵%22"), id="Single Char"),
        pytest.param(Kaki("みる"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22み%22"), id="Ichidan1"),
        pytest.param(Kaki("変える"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22変え%22"), id="Ichidan2"),
        pytest.param(Kaki("したためる"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22したため%22"), id="Ichidan3"),
        pytest.param(Kaki("帰る"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22帰ら|帰り|帰る|帰れ|帰ろ|帰っ%22"), id="Godan1"),
        pytest.param(Kaki("合う"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22合わ|合い|合う|合え|合お|合っ%22"), id="Godan2"),
        pytest.param(Kaki("残す"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22残さ|残し|残す|残せ|残そ%22"), id="Godan3"),
        pytest.param(Kaki("活殺自在"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22活殺自在%22"), id="Nonverb1"),
        pytest.param(Kaki("眼鏡"), URL("https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22眼鏡%22"), id="Nonverb2"),
    ]
)
def test_get_url(word: Kaki, expected_url: URL):
    assert tatoeba.get_url(word) == expected_url
