from collections import defaultdict
import os
import re
from typing import Dict, List

from bs4 import BeautifulSoup as Soup

from testing.dict_typing import FullTestDict

# TODO: DICTS TO ADD:
# - Extra results for ojad (words not in original word list)
# - OJAD with particles (eg kirei)
# - Word with な but not [な], eg なる


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
    "jisho": {
        "expected_output": {
            '眼鏡': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("megane"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:眼鏡/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'11209\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'11209\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">眼鏡</p></div></td>', "html.parser"),
                'writings': ["眼鏡"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class=" accent_top mola_-3"><span class="inner"><span class="char">め</span></span></span><span class="mola_-2"><span class="inner"><span class="char">が</span></span></span><span class="mola_-1"><span class="inner"><span class="char">ね</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser")],
                'readings': ["め' がね"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '眼鏡': ["め' がね"],
        }),
        "expected_output": {
            '眼鏡': ["め' がね"],
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
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "眼鏡",
            "jisho": {},
            "accent": {
                "ojad": ["め' がね"],
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
    "jisho": {
        "expected_output": {
            'カムバック': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("comeback"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:カムバック/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'4965\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'4965\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">カムバック</p></div></td>', "html.parser"),
                'writings': ["カムバック"],
                'reading_sections': [
                    Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-5"><span class="inner"><span class="char">か</span></span></span><span class=" accent_plain mola_-4"><span class="inner"><span class="char">む</span></span></span><span class=" accent_top mola_-3"><span class="inner"><span class="char">ば</span></span></span><span class="mola_-2"><span class="inner"><span class="char">っ</span></span></span><span class="mola_-1"><span class="inner"><span class="char">く</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser"),
                    Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class=" accent_top mola_-5"><span class="inner"><span class="char">か</span></span></span><span class="mola_-4"><span class="inner"><span class="char">む</span></span></span><span class="mola_-3"><span class="inner"><span class="char">ば</span></span></span><span class="mola_-2"><span class="inner"><span class="char">っ</span></span></span><span class="mola_-1"><span class="inner"><span class="char">く</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser"),
                ],
                'readings': ["かむば' っく", "か' むばっく"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            'カムバック': ["かむば' っく", "か' むばっく"],
        }),
        "expected_output": {
            'カムバック': ["かむば' っく", "か' むばっく"],
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
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "カムバック",
            "jisho": {},
            "accent": {
                "ojad": ["かむば' っく", "か' むばっく"],
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
    "jisho": {
        "expected_output": {
            '食べる': {},
            '学生': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("taberu_gakusei"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:食べる%%20学生/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'1238\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'1238\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">食べる・食べます</p></div></td>', "html.parser"),
                'writings': ["食べる", "食べます"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-3"><span class="inner"><span class="char">た</span></span></span><span class=" accent_top mola_-2"><span class="inner"><span class="char">べ</span></span></span><span class="mola_-1"><span class="inner"><span class="char">る</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="1238_1_1_female" href="#" onclick="pronounce_play(\'1238_1_1_female\');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="1238_1_1_male" href="#" onclick="pronounce_play(\'1238_1_1_male\');return false;"></a></div></div>', "html.parser")],
                'readings': ["たべ' る"],
            },
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'4733\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'4733\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">学生</p></div></td>', "html.parser"),
                'writings': ["学生"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-4"><span class="inner"><span class="char">が</span></span></span><span class=" accent_plain mola_-3"><span class="inner"><span class="char">く</span></span></span><span class=" accent_plain mola_-2"><span class="inner"><span class="char">せ</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">い</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser")],
                'readings': ["がくせい"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '食べる': ["たべ' る"],
            '食べます': ["たべ' る"],
            '学生': ["がくせい"],
        }),
        "expected_output": {
            '食べる': ["たべ' る"],
            '学生': ["がくせい"],
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
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "食べる",
            "jisho": {},
            "accent": {
                "ojad": ["たべ' る"],
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
                "ojad": ["がくせい"],
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
    "jisho": {
        "expected_output": {
            '言葉': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("kotoba"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:言葉/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'6204\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'6204\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">言葉</p></div></td>', "html.parser"),
                'writings': ["言葉"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-3"><span class="inner"><span class="char">こ</span></span></span><span class=" accent_plain mola_-2"><span class="inner"><span class="char">と</span></span></span><span class=" accent_top mola_-1"><span class="inner"><span class="char">ば</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser")],
                'readings': ["ことば'"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '言葉': ["ことば'"],
        }),
        "expected_output": {
            '言葉': ["ことば'"],
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
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "言葉",
            "jisho": {},
            "accent": {
                "ojad": ["ことば'"],
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


BADINPUT: FullTestDict = {
    "id": "BADINPUT",
    'input': ['BADINPUT'],
    "jisho": {
        "expected_output": {
            'BADINPUT': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("badinput"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:BADINPUT/page:%s",
        "expected_sections": [],
        "full_accent_dict" : defaultdict(list),
        "expected_output": {
            'BADINPUT': [],
        },
    },
    "suzuki": {
        "html": get_file_as_string("badinput", "suzuki"),
        "formdata": build_suzuki_formdata("BADINPUTは"),
        "expected_sections": [
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>BADINPUTは</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': 'BADINPUT',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_0_0\',1,[0],1,0,0);});</script>', "html.parser"),
                'reading': "",
            },
        ],
        "expected_output": {
            'BADINPUT': [],
        },
    },
    "wadoku": {
        "html": get_file_as_string("badinput", "wadoku"),
        "url": "https://www.wadoku.de/search/BADINPUT",
        "expected_sections": [],
        "full_accent_dict" : defaultdict(list),
        "expected_output": {
            'BADINPUT': [],
        },
    },
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "BADINPUT",
            "jisho": {},
            "accent": {
                "ojad": [],
                "suzuki": [],
                "wadoku": [],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
    ],
}


USAGI_IKU_KAGO: FullTestDict = {
    "id": "USAGI_IKU_KAGO",
    'input': ['兎', '行く', '籠'],
    "jisho": {
        "expected_output": {
            '兎': {},
            '行く': {},
            '籠': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("usagi_iku_kago"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:兎%%20行く%%20籠/page:%s",
        "expected_sections": [
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'740\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'740\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">行く・行きます</p></div></td>', "html.parser"),
                'writings': ["行く", "行きます"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-2"><span class="inner"><span class="char">い</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">く</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="740_1_1_female" href="#" onclick="pronounce_play(\'740_1_1_female\');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="740_1_1_male" href="#" onclick="pronounce_play(\'740_1_1_male\');return false;"></a></div></div>', "html.parser")],
                'readings': ["いく"],
            },
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'4771\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'4771\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">籠</p></div></td>', "html.parser"),
                'writings': ["籠"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-2"><span class="inner"><span class="char">か</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">ご</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser")],
                'readings': ["かご"],
            },
            {
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'4070\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'4070\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">兎</p></div></td>', "html.parser"),
                'writings': ["兎"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-3"><span class="inner"><span class="char">う</span></span></span><span class=" accent_plain mola_-2"><span class="inner"><span class="char">さ</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">ぎ</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser")],
                'readings': ["うさぎ"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '行く': ["いく"],
            '行きます': ["いく"],
            '籠': ["かご"],
            '兎': ["うさぎ"],
        }),
        "expected_output": {
            '行く': ["いく"],
            '籠': ["かご"],
            '兎': ["うさぎ"],
        },
    },
    "suzuki": {
        "html": get_file_as_string("usagi_iku_kago", "suzuki"),
        "formdata": build_suzuki_formdata("兎は\n行くは\n籠は"),
        "expected_sections": [
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>兎は</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '兎',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">う</span></span></span><span class="accent_plain mola_1"><span class="inner"><span class="char">さ</span></span></span><span class="accent_plain mola_2"><span class="inner"><span class="char">ぎ</span></span></span><span class="accent_plain mola_3"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_0_0\',4,[0,1,1,1],1,0,0);});</script>', "html.parser"),
                'reading': "うさぎ",
            },
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>行くは</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '行く',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">い</span></span></span><span class="accent_plain mola_1"><span class="inner"><span class="char">く</span></span></span><span class="accent_plain mola_2"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_1_0\',3,[0,1,1],1,0,0);});</script>', "html.parser"),
                'reading': "いく",
            },
            {
                'writing_section': Soup('<div class="phrasing_subscript"><span>籠は</span><span class="inner endspace"><span class="char"></span></span></div>', "html.parser"),
                'writing': '籠',
                'reading_section': Soup('<div class="phrasing_text"><span class="mola_0"><span class="inner"><span class="char">か</span></span></span><span class="accent_plain mola_1"><span class="inner"><span class="char">ご</span></span></span><span class="accent_plain mola_2"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>',"html.parser"),
                'accent_section': Soup('<script type="text/javascript">$(function () { set_accent_curve_phrase(\'#phrase_2_0\',3,[0,1,1],1,0,0);});</script>', "html.parser"),
                'reading': "かご",
            },
        ],
        "expected_output": {
            '兎': ["うさぎ"],
            '行く': ["いく"],
            '籠': ["かご"],
        },
    },
    "wadoku": {
        "html": get_file_as_string("usagi_iku_kago", "wadoku"),
        "url": "https://www.wadoku.de/search/兎%20行く%20籠",
        "expected_sections": [
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/5431043"><span class="orth" lang="ja" xml:lang="ja"><span class="njk">兎</span></span></a></div>', "html.parser"),
                'writings': ["兎"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">う</span><span class="t l">さぎ</span></span>', "html.parser")],
                'readings': ["うさぎ"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8480460"><span class="orth" lang="ja" xml:lang="ja">兎</span></a></div>', "html.parser"),
                'writings': ["兎"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">う</span><span class="t l"></span></span>', "html.parser")],
                'readings': ["う"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/5945030"><span class="orth" lang="ja" xml:lang="ja">行く</span></a></div>', "html.parser"),
                'writings': ["行く"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">ゆ~</span><span class="t l">く</span></span>', "html.parser")],
                'readings': ["ゆく"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/8042046"><span class="orth" lang="ja" xml:lang="ja">行く<span class="divider">；</span><span class="njok">往</span>く</span></a></div>', "html.parser"),
                'writings': ["行く", "往く"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">い~</span><span class="t l">く</span></span>', "html.parser")],
                'readings': ["いく"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/3388927"><span class="orth" lang="ja" xml:lang="ja">籠</span></a></div>', "html.parser"),
                'writings': ["籠"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b">か</span><span class="t l">ご</span></span>', "html.parser")],
                'readings': ["かご"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/3895667"><span class="orth" lang="ja" xml:lang="ja"><span class="njk">篭</span><span class="divider">；</span><span class="njok">籠</span></span></a></div>', "html.parser"),
                'writings': ["篭", "籠"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="t r">こ</span><span class="b"></span></span>', "html.parser")],
                'readings': ["こ'"],
            },
            {
                'writing_section': Soup('<div class="japanese"><a href="/entry/view/10104508"><span class="orth" lang="ja" xml:lang="ja">籠<span class="paren">も</span>り<span class="divider">；</span>隠<span class="paren">り</span></span></a></div>', "html.parser"),
                'writings': ["籠もり", "隠り"],
                'reading_sections': [Soup('<span class="pron accent" data-accent-id="1"><span class="b r">こ</span><span class="t r">もり</span></span>', "html.parser")],
                'readings': ["こもり'"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '兎': ["うさぎ", "う"],
            '行く': ["ゆく", "いく"],
            '往く': ["いく"],
            '籠': ["かご", "こ'"],
            '篭': ["こ'"],
            '籠もり': ["こもり'"],
            '隠り': ["こもり'"],
        }),
        "expected_output": {
            '兎': ["うさぎ", "う"],
            '行く': ["ゆく", "いく"],
            '籠': ["かご", "こ'"],
        },
    },
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "兎",
            "jisho": {},
            "accent": {
                "ojad": ["うさぎ"],
                "suzuki": ["うさぎ"],
                "wadoku": ["うさぎ", "う"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
        {
            "word": "行く",
            "jisho": {},
            "accent": {
                "ojad": ["いく"],
                "suzuki": ["いく"],
                "wadoku": ["ゆく", "いく"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
        {
            "word": "籠",
            "jisho": {},
            "accent": {
                "ojad": ["かご"],
                "suzuki": ["かご"],
                "wadoku": ["かご", "こ'"],
            },
            "audio": {
                "forvo": [],
                "wanikani": [],
            },
        },
    ],
}


SHIZUKA: FullTestDict = {
    "id": "SHIZUKA",
    'input': ['静か'],
    "jisho": {
        "expected_output": {
            '静か': {},
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("shizuka"),
        "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:静か/page:%s",
        "expected_sections": [
            {
                'na_adj': True,
                'writing_section': Soup("""<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch('word','3149','female');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch('word','3149','male');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">静か[な]・静かです</p></div></td>""", "html.parser"),
                'writings': ["静か", "静かです"],
                'reading_sections': [Soup("""<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class=" accent_top mola_-4"><span class="inner"><span class="char">し</span></span></span><span class="mola_-3"><span class="inner"><span class="char">ず</span></span></span><span class="mola_-2"><span class="inner"><span class="char">か</span></span></span><span class="mola_-1"><span class="inner"><span class="char">な</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="3149_1_1_female" href="#" onclick="pronounce_play('3149_1_1_female');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="3149_1_1_male" href="#" onclick="pronounce_play('3149_1_1_male');return false;"></a></div></div>""", "html.parser")],
                'readings': ["し' ずか"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '静か': ["し' ずか"],
            '静かです': ["し' ずか"],
        }),
        "expected_output": {
            '静か': ["し' ずか"],
        },
    },
    "suzuki": {
        "html": get_file_as_string("shizuka", "suzuki"),
        "formdata": build_suzuki_formdata("静かは"),
        "expected_sections": [
            {
                'writing_section': Soup("""<div class="phrasing_subscript"><span>静かは</span><span class="inner endspace"><span class="char"></span></span></div>""", "html.parser"),
                'writing': '静か',
                'reading_section': Soup("""<div class="phrasing_text"><span class="accent_top mola_0"><span class="inner"><span class="char">し</span></span></span><span class="mola_1"><span class="inner"><span class="char">ず</span></span></span><span class="mola_2"><span class="inner"><span class="char">か</span></span></span><span class="mola_3"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>""","html.parser"),
                'accent_section': Soup("""<script type="text/javascript">$(function () { set_accent_curve_phrase('#phrase_0_0',4,[1,0,0,0],1,0,0);});</script>""", "html.parser"),
                'reading': "し' ずか",
            },
        ],
        "expected_output": {
            '静か': ["し' ずか"],
        },
    },
    "wadoku": {
        "html": get_file_as_string("shizuka", "wadoku"),
        "url": "https://www.wadoku.de/search/静か",
        "expected_sections": [
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/928029"><span class="orth" lang="ja" xml:lang="ja">静<span class="paren">か</span></span></a></div>""", "html.parser"),
                'writings': ['静か'],
                'reading_sections': [Soup("""<span class="pron accent" data-accent-id="1"><span class="t r">し</span><span class="b">ずか</span></span>""", "html.parser")],
                'readings': ["し' ずか"],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/1134980"><span class="orth" lang="ja" xml:lang="ja">静かに</span></a></div>""", "html.parser"),
                'writings': ['静かに'],
                'reading_sections': [],
                'readings': [],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/6264891"><span class="orth" lang="ja" xml:lang="ja">静かな</span></a></div>""", "html.parser"),
                'writings': ['静かな'],
                'reading_sections': [],
                'readings': [],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/4992206"><span class="orth" lang="ja" xml:lang="ja">静かの海</span></a></div>""", "html.parser"),
                'writings': ['静かの海'],
                'reading_sections': [
                    Soup("""<span class="pron accent" data-accent-id="1"><span class="t r">し</span><span class="b">ずか･の･うみ</span></span>""", "html.parser"),
                    Soup("""<span class="pron accent hidden" data-accent-id="2"><span class="t r">し</span><span class="b">ずか･の･</span><span class="t r">う</span><span class="b">み</span></span>""", "html.parser")
                ],
                'readings': ["し' ずかのうみ", "し' ずかの* う' み"],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/4528218"><span class="orth" lang="ja" xml:lang="ja">静かな声</span></a></div>""", "html.parser"),
                'writings': ['静かな声'],
                'reading_sections': [],
                'readings': [],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '静か': ["し' ずか"],
            '静かに': [],
            '静かな': [],
            '静かの海': ["し' ずかのうみ", "し' ずかの* う' み"],
            '静かな声': [],
        }),
        "expected_output": {
            '静か': ["し' ずか"],
        },
    },
    "forvo": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "wanikani": {
        "expected_output": {
            '眼鏡': [],
        },
    },
    "expected_result": [
        {
            "word": "静か",
            "jisho": {},
            "accent": {
                "ojad": ["し' ずか"],
                "suzuki": ["し' ずか"],
                "wadoku": ["し' ずか"],
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
    BADINPUT,
    USAGI_IKU_KAGO,
    SHIZUKA,
]

TEST_DICT_IDS = [test_dict['id'] for test_dict in TEST_DICTS]


# TEMPLATE: FullTestDict = {
#     "id": "",
#     'input': [''],
#     "forvo": {},
#     "jisho": {},
#     "ojad": {
#         "htmls": get_ojad_html_files(""),
#         "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:/page:%s",
#         "expected_sections": [
#             {
#                 'writing_section': Soup("""""", "html.parser"),
#                 'writings': [""],
#                 'reading_sections': [Soup("""""", "html.parser")],
#                 'readings': [""],
#             },
#         ],
#         "full_accent_dict" : defaultdict(list, {
#             '': [],
#         }),
#         "expected_output": {
#             '': [],
#         },
#     },
#     "suzuki": {
#         "html": get_file_as_string("", "suzuki"),
#         "formdata": build_suzuki_formdata(""),
#         "expected_sections": [
#             {
#                 'writing_section': Soup("""""", "html.parser"),
#                 'writing': '',
#                 'reading_section': Soup("""""","html.parser"),
#                 'accent_section': Soup("""""", "html.parser"),
#                 'reading': "",
#             },
#         ],
#         "expected_output": {
#             '': [],
#         },
#     },
#     "wadoku": {
#         "html": get_file_as_string("", "wadoku"),
#         "url": "https://www.wadoku.de/search/",
#         "expected_sections": [
#             {
#                 'writing_section': Soup("""""", "html.parser"),
#                 'writings': [],
#                 'reading_sections': [Soup("""""", "html.parser")],
#                 'readings': [],
#             },
#         ],
#         "full_accent_dict" : defaultdict(list, {
#             '': [],
#         }),
#         "expected_output": {
#             '': [],
#         },
#     },
#     "expected_result": [
#         {
#             "word": "",
#             "jisho": {},
#             "accent": {
#                 "ojad": [],
#                 "suzuki": [],
#                 "wadoku": [],
#             },
#             "audio": {
#                 "forvo": [],
#                 "wanikani": [],
#             },
#         },
#     ],
# }
