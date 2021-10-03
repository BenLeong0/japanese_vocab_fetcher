from functools import partial
import re
from typing import List

from bs4 import BeautifulSoup as Soup
import pytest   # type: ignore

from modules import forvo
from testing.dict_typing import FullTestDict
from testing.dicts import TEST_DICTS, TEST_DICT_IDS
from utils import convert_list_of_str_to_kaki


# For each test, try with every dict in TEST_DICTS
@pytest.fixture(params=TEST_DICTS, ids=TEST_DICT_IDS)
def test_dict(request):
    return request.param


class FakeResponse:
    def __init__(self, text):
        self.text = text


def _get_forvo_html_string(url: str, htmls: List[Soup], timeout: int = 20) -> FakeResponse:
    """Given a url return the corresponding (test) html, or a blank page if out of range"""
    page_number_match = re.search(r"page:\d+", url)

    if not page_number_match:
        raise Exception("Page number not found")

    page_number = int(page_number_match.group()[5:])
    if page_number > len(htmls):
        with open("testing/html_files/ojad_BLANK.html", encoding="utf8") as file:
            return FakeResponse(str(file))
    return FakeResponse(htmls[page_number - 1])


def test_api_key_import():
    """Check the API_KEY is successfully imported"""
    assert forvo.API_KEY[:4] == "0300"
    assert len(forvo.API_KEY) == 32


# def test_main(monkeypatch, test_dict: FullTestDict):
#     """
#     - GIVEN a list of words
#     - WHEN the accent dict is generated
#     - THEN check all the forvo info is correct and complete
#     """
#     word_list = convert_list_of_str_to_kaki(test_dict['input'])
#     html = test_dict['forvo']['html']
#     expected_output = test_dict['forvo']['expected_output']

#     monkeypatch.setattr("requests.post", lambda url, formdata, timeout: FakeResponse(html))
#     assert forvo.main(word_list) == expected_output
