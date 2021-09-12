from collections import defaultdict
import os
import re
from typing import Dict, List

from bs4 import BeautifulSoup as Soup

from testing.dict_typing import FullTestDict

# TODO: DICTS TO ADD:
# - Multiple pages for ojad
# - No result for ojad
# - No result for wadoku
# - Extra results for ojad (not in original word list)


def get_file_as_string(filename: str, module: str):
    path = f"testing/html_files/{module}_{filename}.html"
    with open(path, "r", encoding="utf8") as myfile:
        return re.sub(r'>\s*<', '><', myfile.read())


def get_ojad_html_files(slug: str) -> List[str]:
    htmls: List[str] = []
    i: int = 0
    while True:
        file_index = f"{i:02d}"
        path = f"testing/html_files/ojad_{slug}_{file_index}.html"
        if os.path.exists(path):
            with open(path, "r", encoding="utf8") as myfile:
                htmls.append(re.sub(r'>\s*<', '><', myfile.read()))
            i += 1
        else:
            break
    return htmls


def build_suzuki_formdata(word_list_string: str) -> Dict[str, str]:
    return {
        "data[Phrasing][curve]": "advanced",
        "data[Phrasing][accent]": "advanced",
        "data[Phrasing][accent_mark]": "all",
        "data[Phrasing][estimation]": "crf",
        "data[Phrasing][analyze]": "true",
        "data[Phrasing][phrase_component]": "invisible",
        "data[Phrasing][param]": "invisible",
        "data[Phrasing][subscript]": "visible",
        "data[Phrasing][text]": word_list_string,
    }


MEGANE: FullTestDict = {
    "id": "MEGANE",
    "input": ["眼鏡"],
    "forvo": {},
    "jisho": {},
    "ojad": {
        "htmls": get_ojad_html_files("megane"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:眼鏡/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup(''),
                'writings': [],
                'reading_sections': [Soup('')],
                'readings': [],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '眼鏡': ["め' がね"],
        }),
        "expected_output": {
            '眼鏡': [],
        },
    },
    "suzuki": {
        "html": get_file_as_string("megane", "suzuki"),
        "formdata": build_suzuki_formdata("眼鏡は"),
        "expected_sections": [
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>眼鏡は</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '眼鏡',
                'reading_section': Soup('<div class="phrasing_text"><span class="accent_top mola_0"><span class="inner"><span class="char">め</span></span></span><span class="mola_1"><span class="inner"><span class="char">が</span></span></span><span class="mola_2"><span class="inner"><span class="char">ね</span></span></span><span class="mola_3"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_0_0\',4,[1,0,0,0],1,0,0);});</script>', "html.parser"),
                'reading': "め' がね",
            },
        ],
        "expected_output": {
            '眼鏡': ["め' がね"],
        },
    },
    "wadoku": {
        "html": get_file_as_string("megane", "wadoku"),
        "url": "https://www.wadoku.de/search/眼鏡",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/6038617"><span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span></span></a></div>', "html.parser"),
                'writings': ['眼鏡'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="t r">め<span class="divider">￨</span></span><span class="b">がね</span></span>', "html.parser")],
                'readings': ["め' がね"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/6900624"><span class="orth" lang="ja" xml:lang="ja">眼鏡</span></a></div>', "html.parser"),
                'writings': ['眼鏡'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">が</span><span class="t l">ん<span class="divider">￨</span>きょう</span></span>', "html.parser")],
                'readings': ["がんきょう"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/2719205"><span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span>屋</span></a></div>', "html.parser"),
                'writings': ['眼鏡屋'],
                'reading_sections': [],
                'readings': [],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8239645"><span class="orth" lang="ja" xml:lang="ja"><span class="fjjk">眼鏡</span>橋</span></a></div>', "html.parser"),
                'writings': ['眼鏡橋'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">め</span><span class="t r">がね･</span><span class="b">ばし</span></span>', "html.parser")],
                'readings': ["めがね' ばし"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '眼鏡': ["め' がね", "がんきょう"],
            '眼鏡屋': [],
            '眼鏡橋': ["めがね' ばし"],
        }),
        "expected_output": {
            "眼鏡": ["め' がね", "がんきょう" ],
        },
    },
    "expected_result": [
        {
            "word": "眼鏡",
            "jisho": {},
            "accent": {
                "ojad": [],
                "suzuki": ["め' がね"],
                "wadoku": ["め' がね", "がんきょう" ],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
    ],
}


COMEBACK: FullTestDict= {
    "id": "COMEBACK",
    'input': ['カムバック'],
    "forvo": {},
    "jisho": {},
    "ojad": {
        "htmls": get_ojad_html_files("comeback"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:カムバック/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup(''),
                'writings': [],
                'reading_sections': [Soup('')],
                'readings': [],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            'カムバック': ["かむば' っく", "か' むばっく"],
        }),
        "expected_output": {
            'カムバック': [],
        },
    },
    "suzuki": {
        "html": get_file_as_string("comeback", "suzuki"),
        "formdata": build_suzuki_formdata("カムバックは"),
        "expected_sections": [
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>カムバックは</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': 'カムバック',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">カ</span></span></span><span class="accent_plain mola_1"><span class="inner"><span class="char">ム</span></span></span><span class="accent_top mola_2"><span class="inner"><span class="char">バ</span></span></span><span class="mola_3"><span class="inner"><span class="char">ッ</span></span></span><span class="mola_4"><span class="inner"><span class="char">ク</span></span></span><span class="mola_5"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_0_0\',6,[0,1,1,0,0,0],1,0,0);});</script>', "html.parser"),
                'reading': "カムバ' ック",
            },
        ],
        "expected_output": {
            'カムバック': ["カムバ' ック"],
        },
    },
    "wadoku": {
        "html": get_file_as_string("comeback", "wadoku"),
        "url": "https://www.wadoku.de/search/カムバック",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8009906"><span class="orth" lang="ja" xml:lang="ja">カム･バック</span></a></div>', "html.parser"),
                'writings': ['カムバック'],
                'reading_sections': [
                    Soup('<span class="pron accent" data-accent-id="1"><span class="b r">か</span><span class="t r">む･ば</span><span class="b">っく</span></span>', "html.parser"),
                    Soup('<span class="pron accent hidden" data-accent-id="2"><span class="t r">か</span><span class="b">む･ばっく</span></span>', "html.parser")
                ],
                'readings': ["かむば' っく", "か' むばっく"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/1669030"><span class="orth" lang="ja" xml:lang="ja">カムバックする</span></a></div>', "html.parser"),
                'writings': ['カムバックする'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">か</span><span class="t r">むば</span><span class="b">っくする</span></span>', "html.parser")],
                'readings': ["かむば' っくする"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            'カムバック': ["かむば' っく", "か' むばっく"],
            'カムバックする': ["かむば' っくする"],
        }),
        "expected_output": {
            'カムバック': ["かむば' っく", "か' むばっく"],
        },
    },
    "expected_result": [
        {
            "word": "カムバック",
            "jisho": {},
            "accent": {
                "ojad": [],
                "suzuki": ["カムバ' ック"],
                "wadoku": ["かむば' っく", "か' むばっく"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
    ],
}


TABERU_GAKUSEI: FullTestDict = {
    "id": "TABERU_GAKUSEI",
    'input': ['食べる', '学生'],
    "forvo": {},
    "jisho": {},
    "ojad": {
        "htmls": get_ojad_html_files("taberu_gakusei"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:食べる%%20学生/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup(''),
                'writings': [],
                'reading_sections': [Soup('')],
                'readings': [],
            },
            {
                'writing_section': Soup(''),
                'writings': [],
                'reading_sections': [Soup('')],
                'readings': [],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '食べる': ["たべ' る"],
            '学生': ["がくせい"],
        }),
        "expected_output": {
            '食べる': [],
            '学生': [],
        },
    },
    "suzuki": {
        "html": get_file_as_string("taberu_gakusei", "suzuki"),
        "formdata": build_suzuki_formdata("食べるは\n学生は"),
        "expected_sections": [
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>食べるは</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '食べる',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">た</span></span></span><span class="accent_top mola_1"><span class="inner"><span class="char">べ</span></span></span><span class="mola_2"><span class="inner"><span class="char">る</span></span></span><span class="mola_3"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_0_0\',4,[0,1,0,0],1,0,0);});</script>', "html.parser"),
                'reading': "たべ' る",
            },
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>学生は</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '学生',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">が</span></span></span><span class="accent_plain unvoiced mola_1"><span class="inner"><span class="char">く</span></span></span><span class="accent_plain mola_2"><span class="inner"><span class="char">せ</span></span></span><span class="accent_plain mola_3"><span class="inner"><span class="char">い</span></span></span><span class="accent_plain mola_4"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_1_0\',5,[0,1,1,1,1],1,0,0);});</script>', "html.parser"),
                'reading': "がくせい",
            },
        ],
        "expected_output": {
            '食べる': ["たべ' る"],
            '学生': ["がくせい"],
        },
    },
    "wadoku": {
        "html": get_file_as_string("taberu_gakusei", "wadoku"),
        "url": "https://www.wadoku.de/search/食べる%20学生",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8610599"><span class="orth" lang="ja" xml:lang="ja">食べる</span></a></div>', "html.parser"),
                'writings': ['食べる'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">た~</span><span class="t r">べ</span><span class="b">る</span></span>', "html.parser")],
                'readings': ["たべ' る"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/7011248"><span class="orth" lang="ja" xml:lang="ja">学生</span></a></div>', "html.parser"),
                'writings': ['学生'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">が</span><span class="t l">く<span class="divider">￨</span>せい</span></span>', "html.parser")],
                'readings': ["がくせい"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '食べる': ["たべ' る"],
            '学生': ["がくせい"],
        }),
        "expected_output": {
            '食べる': ["たべ' る"],
            '学生': ["がくせい"],
        },
    },
    "expected_result": [
        {
            "word": "食べる",
            "jisho": {},
            "accent": {
                "ojad": [],
                "suzuki": ["たべ' る"],
                "wadoku": ["たべ' る"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
        {
            "word": "学生",
            "jisho": {},
            "accent": {
                "ojad": [],
                "suzuki": ["がくせい"],
                "wadoku": ["がくせい"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
    ],
}


KOTOBA: FullTestDict = {
    "id": "KOTOBA",
    'input': ['言葉'],
    "forvo": {},
    "jisho": {},
    "ojad": {
        "htmls": get_ojad_html_files("kotoba"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:言葉/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup(''),
                'writings': [],
                'reading_sections': [Soup('')],
                'readings': [],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '言葉': ["ことば'"],
        }),
        "expected_output": {
            '言葉': [],
        },
    },
    "suzuki": {
        "html": get_file_as_string("kotoba", "suzuki"),
        "formdata": build_suzuki_formdata("言葉は"),
        "expected_sections": [
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>言葉は</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '言葉',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">こ</span></span></span><span class="accent_plain mola_1"><span class="inner"><span class="char">と</span></span></span><span class="accent_top mola_2"><span class="inner"><span class="char">ば</span></span></span><span class="mola_3"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_0_0\',4,[0,1,1,0],1,0,0);});</script>', "html.parser"),
                'reading': "ことば'",
            },
        ],
        "expected_output": {
            '言葉': ["ことば'"],
        },
    },
    "wadoku": {
        "html": get_file_as_string("kotoba", "wadoku"),
        "url": "https://www.wadoku.de/search/言葉",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8978613"><span class="orth" lang="ja" xml:lang="ja">言葉<span class="divider">；</span><span class="njok">辞</span><span class="divider">；</span><span class="njok">詞</span></span></a></div>', "html.parser"),
                'writings': ['言葉', '辞', '詞'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">こ</span><span class="t r">と<span class="divider">￨</span>ば</span></span>', "html.parser")],
                'readings': ["ことば'"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/6727285"><span class="orth" lang="ja" xml:lang="ja">言葉数</span></a></div>', "html.parser"),
                'writings': ['言葉数'],
                'reading_sections': [
                    Soup('<span class="pron accent" data-accent-id="1"><span class="b r">こ</span><span class="t r">とば･か</span><span class="b">ず</span></span>', "html.parser"),
                    Soup('<span class="pron accent hidden" data-accent-id="2"><span class="b">こ</span><span class="t l">とば･かず</span></span>', "html.parser"),
                ],
                'readings': ["ことばか' ず", "ことばかず"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/10628117"><span class="orth" lang="ja" xml:lang="ja">言葉典<span class="divider">；</span><span class="njok">辞</span>典</span></a></div>', "html.parser"),
                'writings': ['言葉典', '辞典'],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">こ</span><span class="t l">とば･てん</span></span>', "html.parser")],
                'readings': ["ことばてん"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '言葉': ["ことば'"],
            '辞': ["ことば'"],
            '詞': ["ことば'"],
            '言葉数': ["ことばか' ず", "ことばかず"],
            '言葉典': ["ことばてん"],
            '辞典': ["ことばてん"],
        }),
        "expected_output": {
            '言葉': ["ことば'"],
        },
    },
    "expected_result": [
        {
            "word": "言葉",
            "jisho": {},
            "accent": {
                "ojad": [],
                "suzuki": ["ことば'"],
                "wadoku": ["ことば'"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
    ],
}


TEST_DICTS = [
    MEGANE,
    COMEBACK,
    TABERU_GAKUSEI,
    KOTOBA,
]

TEST_DICT_IDS = [test_dict['id'] for test_dict in TEST_DICTS]
