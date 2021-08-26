# pylint: disable=line-too-long

from collections import defaultdict
from bs4 import BeautifulSoup as Soup
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


@pytest.mark.parametrize(
    "html, expected_sections",
    [
        [WADOKU_MEGANE['html'], [
            (
                Soup('<div class="japanese">\n<a href="/entry/view/6038617">\n<span class="orth" lang="ja" xml:lang="ja">\n<span class="fjjk">眼鏡</span>\n</span>\n</a>\n</div>', "html.parser"),
                [Soup('<span class="pron accent" data-accent-id="1">\n<span class="t r">め<span class="divider">￨</span></span><span class="b">がね</span>\n</span>', "html.parser")]
            ),
            (
                Soup('<div class="japanese">\n<a href="/entry/view/6900624">\n<span class="orth" lang="ja" xml:lang="ja">眼鏡</span>\n</a>\n</div>', "html.parser"),
                [Soup('<span class="pron accent" data-accent-id="1">\n<span class="b">が</span><span class="t l">ん<span class="divider">￨</span>きょう</span>\n</span>', "html.parser")]
            ),
            (
                Soup('<div class="japanese">\n<a href="/entry/view/2719205">\n<span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span>屋</span>\n</a>\n</div>', "html.parser"),
                []
            ),
            (
                Soup('<div class="japanese">\n<a href="/entry/view/8239645">\n<span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span>橋</span>\n</a>\n</div>', "html.parser"),
                [Soup('<span class="pron accent" data-accent-id="1"> <span class="b r">め</span><span class="t r">がね･</span><span class="b">ばし</span> </span>', "html.parser")]
            )
        ]],
        [WADOKU_COMEBACK['html'], [
            (
                Soup('<div class="japanese">\n<a href="/entry/view/8009906"><span class="orth" lang="ja" xml:lang="ja">カム･バック</span></a>\n</div>', "html.parser"),
                [
                    Soup('<span class="pron accent" data-accent-id="1"><span class="b r">か</span><span class="t r">む･ば</span><span class="b">っく</span></span>', "html.parser"),
                    Soup('<span class="pron accent hidden" data-accent-id="2"><span class="t r">か</span><span class="b">む･ばっく</span></span>', "html.parser")
                ]
            ),
            (
                Soup('<div class="japanese">\n<a href="/entry/view/1669030"><span class="orth" lang="ja" xml:lang="ja">カムバックする</span></a>\n</div>', "html.parser"),
                [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">か</span><span class="t r">むば</span><span class="b">っくする</span></span>', "html.parser")]
            ),
        ]],
        [WADOKU_TABERU_GAKUSEI['html'], [
            (
                Soup('<div class="japanese">\n<a href="/entry/view/8610599"><span class="orth" lang="ja" xml:lang="ja">食べる</span></a>\n</div>', "html.parser"),
                [
                    Soup('<span class="pron accent" data-accent-id="1"><span class="b r">た~</span><span class="t r">べ</span><span class="b">る</span></span>', "html.parser")
                ]
            ),
            (
                Soup('<div class="japanese">\n<a href="/entry/view/7011248"><span class="orth" lang="ja" xml:lang="ja">学生</span></a>\n</div>', "html.parser"),
                [Soup('<span class="pron accent" data-accent-id="1">\n<span class="b">が</span><span class="t l">く<span class="divider">￨</span>せい</span>\n</span>', "html.parser")]
            ),
        ]],
    ]
)
def test_get_sections(html, expected_sections):
    assert wadoku.get_sections(Soup(html, "html.parser")) == expected_sections

# @pytest.mark.parametrize("test_dict", [WADOKU_MEGANE, WADOKU_COMEBACK, WADOKU_TABERU_GAKUSEI])
# def test_get_accent_dict(monkeypatch, test_dict):
#     monkeypatch.setattr("requests.post", lambda x, timeout: FakeResponse(test_dict['html']))
#     print(wadoku.get_accent_dict(test_dict['input']))
#     assert False
