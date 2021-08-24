from collections import defaultdict
import pytest
from requests.models import Response

from modules import wadoku

from testing.test_wadoku.example_responses import (
    WADOKU_MEGANE,
    WADOKU_COMEBACK
)

class FakeResponse:
    def __init__(self, text):
        self.text = text

@pytest.mark.parametrize("test_dict", [WADOKU_MEGANE, WADOKU_COMEBACK])
def test_get_accent_dict(monkeypatch, test_dict):
    monkeypatch.setattr("requests.post", lambda x, timeout: FakeResponse(test_dict['resp']))
    print(wadoku.get_accent_dict(test_dict['input']))
    assert False
