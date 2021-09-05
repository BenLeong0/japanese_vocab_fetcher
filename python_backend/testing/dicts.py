# pylint: disable=line-too-long

import re

from bs4 import BeautifulSoup as Soup

from coordinator import Modules

def get_file_as_string(filename: str, module: Modules):
    path = f"testing/html_files/{module.name}_{filename}.html"
    with open(path, "r", encoding="utf8") as myfile:
        return re.sub(r'>\s*<', '><', myfile.read())


MEGANE = {
    "input": ["眼鏡"],
    "forvo": {},
    "jisho": {},
    "ojad": {},
    "suzuki": {},
    "wadoku": {
        "html": get_file_as_string("megane", Modules.WADOKU),
        "url": "https://www.wadoku.de/search/眼鏡",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/6038617"><span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span></span></a></div>', "html.parser"),
                'writings': ['眼鏡'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="t r">め<span class="divider">￨</span></span><span class="b">がね</span></span>', "html.parser")],
                'readings': ["め' がね"]
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/6900624"><span class="orth" lang="ja" xml:lang="ja">眼鏡</span></a></div>', "html.parser"),
                'writings': ['眼鏡'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">が</span><span class="t l">ん<span class="divider">￨</span>きょう</span></span>', "html.parser")],
                'readings': ["がんきょう"]
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/2719205"><span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span>屋</span></a></div>', "html.parser"),
                'writings': ['眼鏡屋'],
                'reading_sections': [],
                'readings': []
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8239645"><span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span>橋</span></a></div>', "html.parser"),
                'writings': ['眼鏡橋'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">め</span><span class="t r">がね･</span><span class="b">ばし</span></span>', "html.parser")],
                'readings': ["めがね' ばし"]
            },
        ],
        "expected_output": {
            "眼鏡": ["め' がね", "がんきょう" ],
        },
    },
}


COMEBACK = {
    'input': ['カムバック'],
    "forvo": {},
    "jisho": {},
    "ojad": {},
    "suzuki": {},
    "wadoku": {
        "html": get_file_as_string("comeback", Modules.WADOKU),
        "url": "https://www.wadoku.de/search/カムバック",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8009906"><span class="orth" lang="ja" xml:lang="ja">カム･バック</span></a></div>', "html.parser"),
                'writings': ['カムバック'],
                'reading_sections': [
                    Soup('<span class="pron accent" data-accent-id="1"><span class="b r">か</span><span class="t r">む･ば</span><span class="b">っく</span></span>', "html.parser"),
                    Soup('<span class="pron accent hidden" data-accent-id="2"><span class="t r">か</span><span class="b">む･ばっく</span></span>', "html.parser")
                ],
                'readings': ["かむば' っく", "か' むばっく"]
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/1669030"><span class="orth" lang="ja" xml:lang="ja">カムバックする</span></a></div>', "html.parser"),
                'writings': ['カムバックする'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">か</span><span class="t r">むば</span><span class="b">っくする</span></span>', "html.parser")],
                'readings': ["かむば' っくする"]
            },
        ],
        "expected_output": {
            'カムバック': ["かむば' っく", "か' むばっく"],
        },
    },
}


TABERU_GAKUSEI = {
    'input': ['食べる', '学生'],
    "forvo": {},
    "jisho": {},
    "ojad": {},
    "suzuki": {},
    "wadoku": {
        "html": get_file_as_string("taberu_gakusei", Modules.WADOKU),
        "url": "https://www.wadoku.de/search/食べる%20学生",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8610599"><span class="orth" lang="ja" xml:lang="ja">食べる</span></a></div>', "html.parser"),
                'writings': ['食べる'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">た~</span><span class="t r">べ</span><span class="b">る</span></span>', "html.parser")],
                'readings': ["たべ' る"]
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/7011248"><span class="orth" lang="ja" xml:lang="ja">学生</span></a></div>', "html.parser"),
                'writings': ['学生'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">が</span><span class="t l">く<span class="divider">￨</span>せい</span></span>', "html.parser")],
                'readings': ["がくせい"]
            },
        ],
        "expected_output": {
            '食べる': ["たべ' る"],
            '学生': ["がくせい"],
        },
    },
}


KOTOBA = {
    'input': ['言葉'],
    "forvo": {},
    "jisho": {},
    "ojad": {},
    "suzuki": {},
    "wadoku": {
        "html": get_file_as_string("kotoba", Modules.WADOKU),
        "url": "https://www.wadoku.de/search/言葉",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8978613"><span class="orth" lang="ja" xml:lang="ja">言葉<span class="divider">；</span><span class="njok">辞</span><span class="divider">；</span><span class="njok">詞</span></span></a></div>', "html.parser"),
                'writing': ['言葉', '辞', '詞'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">こ</span><span class="t r">と<span class="divider">￨</span>ば</span></span>', "html.parser")],
                'readings': ["ことば'"]
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/6727285"><span class="orth" lang="ja" xml:lang="ja">言葉数</span></a></div>', "html.parser"),
                'writing': ['言葉数'],
                'reading_sections': [
                    Soup('<span class="pron accent" data-accent-id="1"><span class="b r">こ</span><span class="t r">とば･か</span><span class="b">ず</span></span>', "html.parser"),
                    Soup('<span class="pron accent hidden" data-accent-id="2"><span class="b">こ</span><span class="t l">とば･かず</span></span>', "html.parser"),
                ],
                'readings': ["ことばか' ず", "ことばかず"]
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/10628117"><span class="orth" lang="ja" xml:lang="ja">言葉典<span class="divider">；</span><span class="njok">辞</span>典</span></a></div>', "html.parser"),
                'writing': ['言葉典', '辞典'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">こ</span><span class="t l">とば･てん</span></span>', "html.parser")],
                'readings': ["ことばてん"]
            },
        ],
        "expected_output": {
            '言葉': ["ことば'"],
        },
    },
}
