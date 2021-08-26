# pylint: disable=line-too-long

from collections import defaultdict
import pytest
from requests.models import Response

from modules import wadoku

from testing.test_wadoku.example_responses import (
    WADOKU_MEGANE,
    WADOKU_COMEBACK,
    WADOKU_TABERU_GAKUSEI
)

class FakeResponse:
    def __init__(self, text):
        self.text = text


@pytest.mark.parametrize(
    "word_list, expected_url",
    [
        [['眼鏡'], "https://www.wadoku.de/search/%E7%9C%BC%E9%8F%A1"],
        [['食べる', '学生'], "https://www.wadoku.de/search/%E9%A3%9F%E3%81%B9%E3%82%8B%20%E5%AD%A6%E7%94%9F"]
    ]
)
def test_get_url(word_list, expected_url):
    assert wadoku.get_url(word_list) == expected_url

# @pytest.mark.parametrize("test_dict", [WADOKU_MEGANE, WADOKU_COMEBACK, WADOKU_TABERU_GAKUSEI])
# def test_get_accent_dict(monkeypatch, test_dict):
#     monkeypatch.setattr("requests.post", lambda x, timeout: FakeResponse(test_dict['html']))
#     print(wadoku.get_accent_dict(test_dict['input']))
#     assert False
