from collections import defaultdict
import os
import re

from bs4 import BeautifulSoup as Soup
from dotenv import dotenv_values

from custom_types.alternative_string_types import HTMLString, URL, Yomi
from testing import jisho_api_responses, wanikani_api_responses
from testing.dict_typing import FullTestDict

if os.path.exists(".env"):
    API_KEY: str = dotenv_values()['FORVO_API_KEY']
else:
    API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
print(API_KEY)


def get_file_as_string(filename: str, module: str):
    path = f"testing/html_files/{module}_{filename}.html"
    with open(path, "r", encoding="utf8") as myfile:
        return re.sub(r'>\s*<', '><', myfile.read())


def get_ojad_html_files(slug: str) -> list[HTMLString]:
    htmls: list[str] = []
    file_index: int = 0
    while True:
        path = f"testing/html_files/ojad_{slug}_{file_index:02d}.html"
        if not os.path.exists(path):
            break
        with open(path, "r", encoding="utf8") as myfile:
            htmls.append(re.sub(r'>\s*<', '><', myfile.read()))
        file_index += 1
    return list(map(HTMLString, htmls))


def build_suzuki_formdata(word_list_string: str) -> dict[str, str]:
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
    "japanesepod": {
        "expected_sections": {
            "眼鏡": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ眼鏡"),
                "html": get_file_as_string("megane", "japanesepod"),
            },
        },
        "expected_output": {
            "眼鏡": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            '眼鏡': {
                "url": URL("https://jisho.org/api/v1/search/words?keyword=眼鏡"),
                "api_response": jisho_api_responses.MEGANE["眼鏡"],
                "filtered_items": jisho_api_responses.MEGANE_FILTERED_ITEMS["眼鏡"],
                "extra_items": jisho_api_responses.MEGANE_EXTRA_ITEMS["眼鏡"],
            },
        },
        "expected_output": {
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.MEGANE_FILTERED_ITEMS["眼鏡"],
                    "extra": jisho_api_responses.MEGANE_EXTRA_ITEMS["眼鏡"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("megane"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:眼鏡/page:%s"),
        "expected_sections": [
            {
                'na_adj': False,
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
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("め' がね")],
                },
            },
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
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("め' がね")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("megane", "wadoku"),
        "url": URL("https://www.wadoku.de/search/眼鏡"),
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
            "眼鏡": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("め' がね"), Yomi("がんきょう") ],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            '眼鏡': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/眼鏡/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":5},"items":[{"id":949210,"word":"\\u773c\\u93e1","original":"\\u773c\\u93e1","addtime":"2011-01-04 10:48:31","hits":1273,"username":"akitomo","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/332129393h1k363n2c3i2b3k25283b2i323b3235232h2j263c2e3g2o2m3i351o3c3f3e26391j2i1m243c1l1o35332g2g2h3h3g382i1i2h2a3b3a243n3m3b2j3m3c1g1i253a2i3d213a3g312l1b1l343c1o3e1j2j3e211t1t_3q3l2b272e2h3c2e3g342629253338333o2b1n1h35211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1i3i3k2l372g2b3j233p1l381l2n382d3d2q1b372p1l2b252q213o1l322e3o2637373e212g3o3h3q213i273j1j2m3b2j3m1g2d2b3j2n211f3h2q2i2j393p3g362n211l291f2l2k2l3l3q3c3a3q3p3o3o342k353g36371t1t_2j281g293q3b1f3e2k1g1g291b3p1h311m1k293e1g211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5038127,"word":"\\u773c\\u93e1","original":"\\u773c\\u93e1","addtime":"2017-06-08 01:20:52","hits":761,"username":"Akiko3001","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3b2f1j26333o3l393d3c2n253h2p1n2n312m3k252k2c2g1j3m2p1f392d1h311i2p2k26242c2i3e222a3h3p3a3q282p262m283i282p383m1l1b35212i1m3m2123392i3e39341h3e341p1m392k3p272i1p291p27291n3n1t1t_2j3j3d1g35363i2i1o332o293f3p241h2n371k3k1f2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/212m3o2p3g212j2g3b211l1f3g3b3m3k393i24263a3534253q1f3k1m2l322d1h3f2p3g2a1i1g3j2e1f2e2e382i2h2l2g1n2f2m1b3g382q1k3e3g2j361b1m362m3l3j232c2k3e271m253e222b2m333g2a2d383d2j3l211t1t_2d2a3l2o2d3c292q2b2p2c292h242e1n2e3q2q2e1j211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5367147,"word":"\\u773c\\u93e1","original":"\\u773c\\u93e1","addtime":"2017-12-14 07:49:03","hits":664,"username":"poyotan","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/332c282f2o3g2f3e3535251m3o1h29381l3n3732213m363n323f3h373h26331i252j3l3m1p3g3a2n1o2d2p3b1l3g3l1m2k3n353n1b363k3l3o1g3626262h3g2q2c3e3c1g233i363o371g382b3521273j283l391l312h1t1t_1m3l342n242q3p2d2m3p2f2h382k242b3l1k3l3h3o211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3f1f2d3n3c23352l3g2m3a2e262o1f273q21222j1h381l1f2g1l2g2k2i212c3n35381g2i29292o1j3k2g342j3g1p2o39373n243d1g2b3l2o1m2h2q2j1h251l3a1j3o32332k2a1k26282i2m1l1m3f3l283e2j351h33211t1t_2p3624243d1n1o3f211k1j2l1m2n2i2j29232d353g211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5386351,"word":"\\u773c\\u93e1","original":"\\u773c\\u93e1","addtime":"2017-12-26 13:12:56","hits":1698,"username":"skent","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3m3i23273h3m253e1n2f3o2e2o1g3k2q1j2e1o3g2l3e3o33222l341b3h1j332p1g2q3j2k1i1n2a1h2j2e3h3a3q28283m2m2c231l362n1i213g1o2n333d3q243f233h341h1j1o32392h2f2h1b3b2k371f1i1o2d2n2l371t1t_2l1f2i2n3i373c3l2m1f3i2h3p3h2b3k2f381h1o323n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/343k2k292q373p2o2l2n3l3h221j2k2g2p1f3a3k3k341p38252k3725313b3q3p232d232q3a3j382c3q2p223k1g1g3g3h3d392a1l23282c3m1k2p281b2q3o1j3c342n1g2e233c363f1h253j3e1j1l1h2l2d3d372k2c3n1t1t_1b2m1b1n393m1j2b3o2n292c3e2m1l1o3o1j2h2p342h1t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":6231492,"word":"\\u773c\\u93e1","original":"\\u773c\\u93e1","addtime":"2019-07-15 17:49:22","hits":147,"username":"monekuson","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3c1n2o3f3n313i2o372i1h2e3o3q2e3a292p3o1j3m2h382k3k2o27291g341f312j2f1f2g3q1b3o3o313n2m283p1l2h3m253939371h1n3q272g2a3a383c3n2i3g2b1g1k2m371f363f281o3i3638253n322e31381g1i211t1t_1o1h3j323637373d2a1h37333l2121371l3a2i1o2f2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/273m3627392f373d3d2o2m28363o2j261k2m2b2m2a28233n3m2m1m3p1l3q2l3p2f21373p3l2h351i2p3q2p313l3k233p1h3d2q1m2e1b2l3a3p1m2q3j2j21332k2i2b2f253f3e1o3p2o243f1l1f332m3m283l3m3b1b211t1t_3631323l2h1m3l2g383p272i3l1h3f3m3j2c3q2g2d3n1t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 5,
            },
        },
        "expected_output": {
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/332129393h1k363n2c3i2b3k25283b2i323b3235232h2j263c2e3g2o2m3i351o3c3f3e26391j2i1m243c1l1o35332g2g2h3h3g382i1i2h2a3b3a243n3m3b2j3m3c1g1i253a2i3d213a3g312l1b1l343c1o3e1j2j3e211t1t_3q3l2b272e2h3c2e3g342629253338333o2b1n1h35211t1t"),
                            "username": "akitomo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3b2f1j26333o3l393d3c2n253h2p1n2n312m3k252k2c2g1j3m2p1f392d1h311i2p2k26242c2i3e222a3h3p3a3q282p262m283i282p383m1l1b35212i1m3m2123392i3e39341h3e341p1m392k3p272i1p291p27291n3n1t1t_2j3j3d1g35363i2i1o332o293f3p241h2n371k3k1f2h1t1t"),
                            "username": "Akiko3001",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/332c282f2o3g2f3e3535251m3o1h29381l3n3732213m363n323f3h373h26331i252j3l3m1p3g3a2n1o2d2p3b1l3g3l1m2k3n353n1b363k3l3o1g3626262h3g2q2c3e3c1g233i363o371g382b3521273j283l391l312h1t1t_1m3l342n242q3p2d2m3p2f2h382k242b3l1k3l3h3o211t1t"),
                            "username": "poyotan",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3m3i23273h3m253e1n2f3o2e2o1g3k2q1j2e1o3g2l3e3o33222l341b3h1j332p1g2q3j2k1i1n2a1h2j2e3h3a3q28283m2m2c231l362n1i213g1o2n333d3q243f233h341h1j1o32392h2f2h1b3b2k371f1i1o2d2n2l371t1t_2l1f2i2n3i373c3l2m1f3i2h3p3h2b3k2f381h1o323n1t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3c1n2o3f3n313i2o372i1h2e3o3q2e3a292p3o1j3m2h382k3k2o27291g341f312j2f1f2g3q1b3o3o313n2m283p1l2h3m253939371h1n3q272g2a3a383c3n2i3g2b1g1k2m371f363f281o3i3638253n322e31381g1i211t1t_1o1h3j323637373d2a1h37333l2121371l3a2i1o2f2h1t1t"),
                            "username": "monekuson",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            '眼鏡': {
                "url": URL("https://tangorin.com/sentences?search=眼鏡",),
                "html": get_file_as_string("megane", "tangorin"),
            },
        },
        "expected_output": {
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "「めがねなくても大丈夫なの？」「あ、これ伊達めがねだから、頭よくなるかなと思って」",
                            "en": "\"You're OK without your glasses?\" \"Ah, these are fake you see, I thought it might make me brainier...\"",
                        },
                        {
                            "ja": "木下さんは昨日眼鏡を事務所に置き忘れた。",
                            "en": "Mr Kinoshita left his glasses behind in the office yesterday.",
                        },
                        {
                            "ja": "僕のメガネをどうしたの。たった今ここにあったのに。",
                            "en": "What did you do with my glasses? They were here a minute ago.",
                        },
                        {
                            "ja": "母はメガネなしでは読書できない。",
                            "en": "My mother can't read without glasses.",
                        },
                        {
                            "ja": "彼女はメガネをはずしてコンタクトをはめた。",
                            "en": "She took off her glasses and put her contacts in.",
                        },
                        {
                            "ja": "彼は眼鏡越しに私をにらみつけた。",
                            "en": "He looked sharply at me over his spectacles.",
                        },
                        {
                            "ja": "彼は眼鏡を外した。",
                            "en": "He took off his glasses.",
                        },
                        {
                            "ja": "彼は眼鏡をはずして看護婦に向かってしかめ面をした。",
                            "en": "He took off his glasses and frowned at the nurse.",
                        },
                        {
                            "ja": "彼は眼鏡ごしに彼女を見た。",
                            "en": "He looked at her over his glasses.",
                        },
                        {
                            "ja": "彼の目はめがねの奥で笑っていた。",
                            "en": "His eyes were smiling behind his glasses.",
                        },
                    ],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=眼鏡"),
        "api_response": wanikani_api_responses.MEGANE,
        "result_dict": {
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/11v648aiw4875mqspzrpn98ly07e"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 7771,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/hoiygkrxyq7a43jujw1skqzla3mx"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 24645,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "You should wipe your glasses.",
                            "ja": "眼鏡を拭いた方がいいですよ。"
                        },
                    ],
                },
            },
        },
        "expected_output": {
            '眼鏡': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/11v648aiw4875mqspzrpn98ly07e"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 7771,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/hoiygkrxyq7a43jujw1skqzla3mx"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 24645,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "You should wipe your glasses.",
                            "ja": "眼鏡を拭いた方がいいですよ。"
                        },
                    ],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "眼鏡",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.MEGANE_FILTERED_ITEMS["眼鏡"],
                    "extra": jisho_api_responses.MEGANE_EXTRA_ITEMS["眼鏡"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("め' がね")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("め' がね")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("め' がね"), Yomi("がんきょう")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/332129393h1k363n2c3i2b3k25283b2i323b3235232h2j263c2e3g2o2m3i351o3c3f3e26391j2i1m243c1l1o35332g2g2h3h3g382i1i2h2a3b3a243n3m3b2j3m3c1g1i253a2i3d213a3g312l1b1l343c1o3e1j2j3e211t1t_3q3l2b272e2h3c2e3g342629253338333o2b1n1h35211t1t"),
                            "username": "akitomo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3b2f1j26333o3l393d3c2n253h2p1n2n312m3k252k2c2g1j3m2p1f392d1h311i2p2k26242c2i3e222a3h3p3a3q282p262m283i282p383m1l1b35212i1m3m2123392i3e39341h3e341p1m392k3p272i1p291p27291n3n1t1t_2j3j3d1g35363i2i1o332o293f3p241h2n371k3k1f2h1t1t"),
                            "username": "Akiko3001",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/332c282f2o3g2f3e3535251m3o1h29381l3n3732213m363n323f3h373h26331i252j3l3m1p3g3a2n1o2d2p3b1l3g3l1m2k3n353n1b363k3l3o1g3626262h3g2q2c3e3c1g233i363o371g382b3521273j283l391l312h1t1t_1m3l342n242q3p2d2m3p2f2h382k242b3l1k3l3h3o211t1t"),
                            "username": "poyotan",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3m3i23273h3m253e1n2f3o2e2o1g3k2q1j2e1o3g2l3e3o33222l341b3h1j332p1g2q3j2k1i1n2a1h2j2e3h3a3q28283m2m2c231l362n1i213g1o2n333d3q243f233h341h1j1o32392h2f2h1b3b2k371f1i1o2d2n2l371t1t_2l1f2i2n3i373c3l2m1f3i2h3p3h2b3k2f381h1o323n1t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3c1n2o3f3n313i2o372i1h2e3o3q2e3a292p3o1j3m2h382k3k2o27291g341f312j2f1f2g3q1b3o3o313n2m283p1l2h3m253939371h1n3q272g2a3a383c3n2i3g2b1g1k2m371f363f281o3i3638253n322e31381g1i211t1t_1o1h3j323637373d2a1h37333l2121371l3a2i1o2f2h1t1t"),
                            "username": "monekuson",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "「めがねなくても大丈夫なの？」「あ、これ伊達めがねだから、頭よくなるかなと思って」",
                            "en": "\"You're OK without your glasses?\" \"Ah, these are fake you see, I thought it might make me brainier...\"",
                        },
                        {
                            "ja": "木下さんは昨日眼鏡を事務所に置き忘れた。",
                            "en": "Mr Kinoshita left his glasses behind in the office yesterday.",
                        },
                        {
                            "ja": "僕のメガネをどうしたの。たった今ここにあったのに。",
                            "en": "What did you do with my glasses? They were here a minute ago.",
                        },
                        {
                            "ja": "母はメガネなしでは読書できない。",
                            "en": "My mother can't read without glasses.",
                        },
                        {
                            "ja": "彼女はメガネをはずしてコンタクトをはめた。",
                            "en": "She took off her glasses and put her contacts in.",
                        },
                        {
                            "ja": "彼は眼鏡越しに私をにらみつけた。",
                            "en": "He looked sharply at me over his spectacles.",
                        },
                        {
                            "ja": "彼は眼鏡を外した。",
                            "en": "He took off his glasses.",
                        },
                        {
                            "ja": "彼は眼鏡をはずして看護婦に向かってしかめ面をした。",
                            "en": "He took off his glasses and frowned at the nurse.",
                        },
                        {
                            "ja": "彼は眼鏡ごしに彼女を見た。",
                            "en": "He looked at her over his glasses.",
                        },
                        {
                            "ja": "彼の目はめがねの奥で笑っていた。",
                            "en": "His eyes were smiling behind his glasses.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/11v648aiw4875mqspzrpn98ly07e"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 7771,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/hoiygkrxyq7a43jujw1skqzla3mx"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 24645,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "You should wipe your glasses.",
                            "ja": "眼鏡を拭いた方がいいですよ。"
                        },
                    ],
                },
            },
        },
    ],
}


COMEBACK: FullTestDict= {
    "id": "COMEBACK",
    "input": ['カムバック'],
    "japanesepod": {
        "expected_sections": {
            "カムバック": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJカムバック"),
                "html": get_file_as_string("comeback", "japanesepod"),
            },
        },
        "expected_output": {
            "カムバック": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            'カムバック': {
                "url": URL("https://jisho.org/api/v1/search/words?keyword=カムバック"),
                "api_response": jisho_api_responses.COMEBACK["カムバック"],
                "filtered_items": jisho_api_responses.COMEBACK_FILTERED_ITEMS["カムバック"],
                "extra_items": jisho_api_responses.COMEBACK_EXTRA_ITEMS["カムバック"],
            },
        },
        "expected_output": {
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.COMEBACK_FILTERED_ITEMS["カムバック"],
                    "extra": jisho_api_responses.COMEBACK_EXTRA_ITEMS["カムバック"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("comeback"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:カムバック/page:%s"),
        "expected_sections": [
            {
                'na_adj': False,
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
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かむば' っく"), Yomi("か' むばっく")],
                },
            },
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
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("カムバ' ック")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("comeback", "wadoku"),
        "url": URL("https://www.wadoku.de/search/カムバック"),
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
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かむば' っく"), Yomi("か' むばっく")],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            'カムバック': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/カムバック/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":1},"items":[{"id":3513252,"word":"\\u30ab\\u30e0\\u30d0\\u30c3\\u30af","original":"\\u30ab\\u30e0\\u30d0\\u30c3\\u30af","addtime":"2015-03-25 00:37:17","hits":336,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1h2d3b292b341f3i2f3m2p3e34253e2h282o3c1i1j3b1o263i2c363q3k2p351p2a1n3j2g1h1p2d291b3b3b3j2233371i333o1f2h1h291m282f381h3p1p3n3b2o3g2n273h372e263m36323m282n382p3k2a271b223d211t1t_2m3b21293b1b322a2q3m3b3b241h1p2j282d2j281n211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/331i2o3o233h1o3h3d3b3a2k1i2e3c2i1l2n213226353c272l393a1i2c1j3j1k1g3m2j3m3n2o1f2p32223n3k2f251j1o2o2d283l1k1b342a3d3o353n233b2l2n37242i26211i2e32352j2h2j3n3i3m2l351n2j3i37211t1t_38382d393d33333a3p1h3e253h3j1m2j1l3q3n2d23211t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 1,
            },
        },
        "expected_output": {
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/1h2d3b292b341f3i2f3m2p3e34253e2h282o3c1i1j3b1o263i2c363q3k2p351p2a1n3j2g1h1p2d291b3b3b3j2233371i333o1f2h1h291m282f381h3p1p3n3b2o3g2n273h372e263m36323m282n382p3k2a271b223d211t1t_2m3b21293b1b322a2q3m3b3b241h1p2j282d2j281n211t1t"),
                            "username": "strawberrybrown",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            'カムバック': {
                "url": URL("https://tangorin.com/sentences?search=カムバック",),
                "html": get_file_as_string("comeback", "tangorin"),
            },
        },
        "expected_output": {
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=カムバック"),
        "api_response": wanikani_api_responses.COMEBACK,
        "result_dict": {},
        "expected_output": {
            'カムバック': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "カムバック",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.COMEBACK_FILTERED_ITEMS["カムバック"],
                    "extra": jisho_api_responses.COMEBACK_EXTRA_ITEMS["カムバック"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かむば' っく"), Yomi("か' むばっく")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("カムバ' ック")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かむば' っく"), Yomi("か' むばっく")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/1h2d3b292b341f3i2f3m2p3e34253e2h282o3c1i1j3b1o263i2c363q3k2p351p2a1n3j2g1h1p2d291b3b3b3j2233371i333o1f2h1h291m282f381h3p1p3n3b2o3g2n273h372e263m36323m282n382p3k2a271b223d211t1t_2m3b21293b1b322a2q3m3b3b241h1p2j282d2j281n211t1t"),
                            "username": "strawberrybrown",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    ],
}


TABERU_GAKUSEI: FullTestDict = {
    "id": "TABERU_GAKUSEI",
    "input": ['食べる', '学生'],
    "japanesepod": {
        "expected_sections": {
            "食べる": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ食べる"),
                "html": get_file_as_string("taberu", "japanesepod"),
            },
            "学生": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ学生"),
                "html": get_file_as_string("gakusei", "japanesepod"),
            },
        },
        "expected_output": {
            "食べる": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "学生": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            '食べる': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=食べる"),
                "api_response": jisho_api_responses.TABERU_GAKUSEI["食べる"],
                "filtered_items": jisho_api_responses.TABERU_GAKUSEI_FILTERED_ITEMS["食べる"],
                "extra_items": jisho_api_responses.TABERU_GAKUSEI_EXTRA_ITEMS["食べる"],
            },
            '学生': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=学生"),
                "api_response": jisho_api_responses.TABERU_GAKUSEI["学生"],
                "filtered_items": jisho_api_responses.TABERU_GAKUSEI_FILTERED_ITEMS["学生"],
                "extra_items": jisho_api_responses.TABERU_GAKUSEI_EXTRA_ITEMS["学生"],
            },
        },
        "expected_output": {
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.TABERU_GAKUSEI_FILTERED_ITEMS["食べる"],
                    "extra": jisho_api_responses.TABERU_GAKUSEI_EXTRA_ITEMS["食べる"],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.TABERU_GAKUSEI_FILTERED_ITEMS["学生"],
                    "extra": jisho_api_responses.TABERU_GAKUSEI_EXTRA_ITEMS["学生"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("taberu_gakusei"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:食べる%%20学生/page:%s"),
        "expected_sections": [
            {
                'na_adj': False,
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'1238\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'1238\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">食べる・食べます</p></div></td>', "html.parser"),
                'writings': ["食べる", "食べます"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-3"><span class="inner"><span class="char">た</span></span></span><span class=" accent_top mola_-2"><span class="inner"><span class="char">べ</span></span></span><span class="mola_-1"><span class="inner"><span class="char">る</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="1238_1_1_female" href="#" onclick="pronounce_play(\'1238_1_1_female\');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="1238_1_1_male" href="#" onclick="pronounce_play(\'1238_1_1_male\');return false;"></a></div></div>', "html.parser")],
                'readings': ["たべ' る"],
            },
            {
                'na_adj': False,
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
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("たべ' る")],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("がくせい")],
                },
            },
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
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("たべ' る")],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("がくせい")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("taberu_gakusei", "wadoku"),
        "url": URL("https://www.wadoku.de/search/食べる%20学生"),
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
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("たべ' る")],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("がくせい")],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            '食べる': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/食べる/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":10},"items":[{"id":1024890,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2011-02-18 01:23:21","hits":4626,"username":"mi8NatsuKi","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3f2n2n1f363f1k1k2p2j2c223q383m1m1k1m222m2b3o2k3k3g2i1l1l362g3n1m3f2i3a1k3f2i2k3d2l2b2333212b232q2n281o271l2g2n313l3a3f1b3n363o2a1p2q2o2q1b1n282i273k2q2q2q2h353m383a3c3q1h371t1t_2n1l2b261o1p1m393i233o2a1g2g392p2q3b2n3e2a3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1p3n223g3o1g242n362o1l3f392p283i3g1g2i331g1m2b311o3623333f1p22353k361j331m1n1g373g2b272k1b3b3g2o2b3a3c291f262p272q1o383i312p3h2e2h2n1g2l231f3i3m2g3k1p2c2c2c2c372o3b1g3b1k211t1t_3b1j2m3l311m3j2h3g2k2p3j29392c3k2c3g2e211m371t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":2676270,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2013-12-26 11:34:16","hits":9245,"username":"kiiro","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2733252e331g2q3h2928353f28373e2i3d2j33222h2p2l2k1h291i3g3l3f22293224362e3l1f392o353i3q1p2q332l2f291n25322f1b3q2i2h2o212g333g3c1h_243j382k291i1i1f3e283a371b333h3q3i1f3d1m26371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2b1g2c3b223n1h3q2c263p1i2k2a3d343h2p3d2j1k3j383h3p393j232m1k3q1b2i393q2o28293d393i3h261b391k1f2i2b3n3q1i2o2b2f2b3728273q3o351p1n_2i212o2n2c2o26383m37311h3i3c1p1b373a1h333b3n1t1t","rate":2,"num_votes":2,"num_positive_votes":2},{"id":3195291,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2014-09-18 11:08:57","hits":25161,"username":"mutsusoken","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/212k29232n2f2e222e31232j243o1m262p3j2j372c2n2q232g351p322l2k2f342d383d2e3q3p3a333a2b2e1g3k3a2a3m2b2f2b1k2n253b263m233q2239332k1j_1g2c1h1l2g2b1m3n1m293k242b2f1n2b2i1f2k1b3b371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3c2232291j1k393m3q1b2k1n2q2o1i3j371f2q1f3727293m263p391l3d3n2h392m1k2g3l3129232h223e353e1n32313p3h3c2c273c2p3n1o2o3g233l1p23262j_1h3q2o2p2i36242k32332a3924212e332m2m2g1n1h371t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":3613670,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2015-05-16 00:23:44","hits":6264,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/261p1k363p312g3p2b3p312g382e1f2a1f3o3j2c36363i353b3m2k3d3q392g1i1l1m361l332e271h2g2q363h2h363l3o1f2p233c3c3j2j3l371p1m2n2c1o2g25_1m3b212k26271l2m3d2k2b3c1l1g37313f3p213h1i211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2o372h1b2m1g3k1l3p3m392n3d1l3g1i311i281f1h3g3l1j3n2g1j3e3l291j2q263c1p1g392m3h2a2q2c2g221m353e2a2d2q1l272l382a2c2i263m1o2c3c3b3d_2m343d21353n262b3f3i3g2q3q2l1i2n311g272k243n1t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":3769720,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2015-07-29 11:42:27","hits":4742,"username":"leona1","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/273i321j3b2k2a2b3k2l3k2p322p391l1f1p262q2k241l1n2j291i292a3j1h1l2d1l36353i332p3c362l3p3j3b1o1f2p1o2j2q3e1g212f3d3c1i392d3d3n1j2c_1l2o3j3b1h2p1f3a3n2o3k1g322f26233o363e1l3h3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/261j36362e3q1o37292e3l3226332k271i341n291k3k312o3c232p2d21233g37282d3b342n21243o27223l2m3n3g2b2c312a2q2n233h332n2q3l2e2b1k271h3a_291l2n38343b24281p2d2g263h39252b2l262b1o3l211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":4376865,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2016-06-16 16:52:44","hits":5321,"username":"chiharu","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3h3e3e3b2a1g1l1k272223281i3h3p3i282d323c3h1h2l211h2c1l2b3c243c27272g21331n3j2k1i353f3h1o331j292p1k241m1n3i39322c353q1j3h1p3e3i2j_263k2o1m2o351l1f2f223e3l2l1h2q3p1j353d2h3d3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2b3m1b3d1o38362b1b3o3937293a3n3m362d1g32312l1m2b3l2a382c3k272b2o1l223f3l243q3h392d1h391j2m1p2g353p2i2i293q3a3m3i2g1l3i3m2k2f1i24_3a1m2c3c1o1j1p2g2l2h372f392i2a2b3n3d333f3l211t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":4400214,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2016-06-30 23:14:14","hits":5356,"username":"skent","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3j2g3o3f2g3q3934322l1o33392g1i361n29353d1l2j1o2n1f362a2k1l3g2h2k29351m3e3a2o1f1i2h2c3l2l2i2j2p283g3c292o212j2h1m3d3p241p1h3q3b2o_242n1f232m263a3j2n2g3i1o1i2d2c3a1m2n1m2d34371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/332a3m3e3h1f232b3g3o2b3d272e3627372h3g3c3j2e3b283q332e2m3q1g2g1p1b32313l1n28391h3e2a353b2i1l372q262j353d1h1i333d1f1o3q3m1b2o223n_1o3a252m362b263o3c311j3o2i3c3m3g2e1p242o1m3n1t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":4983937,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2017-05-06 12:48:08","hits":571,"username":"straycat88","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/39223a3l3g3g2i2l3q272g283m2h2e2726261h1j3j252i273g2p2g243124213b3k3a1o3o2o213m23343j1j3d1o3h3a212h2i332n3d1h2q363j33242i393b3m2l_292o293f2e272j1j33222235373i2q3a38341i373f2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3l272c282k2e39231k3f393n2a231p382e2g1g2a2q1o322j2a2h2i253m3b25321g2a1b2i1o333c312d1b2p2b2g2f273h1o2j35311j312e292722312238312f2l_221m2h382q2c283l2k3q2i2e1j2a1m361m3c382421211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5508706,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2018-02-18 14:29:39","hits":545,"username":"le_temps_perdu","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3f3i241p2g1h3h2f3l251p1j3h2e3q2k38243a3c3h1n2c3k1l1i3e22253d2f3g2i293b1p3f1h2b2d311k2a1g1h3j3o373k1p372l3o1b3h392d3p2i383c1i3633_2q1p2p3a2q3i2n3n2g3f262c382i211m2a3f3p233n2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3f3l36261i232h1f3p291f2i2632293k321f1l2e1o323i3a383i3g3q2c243e2b2k1j362j1o2m2b382h382i2l3a213m1k1l2i2o2b2l2h3g2k282l353q2f3n3c27_2b353o312q3l2n1g2i2p21242m2k282e221h2d3m2q3n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":6227831,"word":"\\u98df\\u3079\\u308b","original":"\\u98df\\u3079\\u308b","addtime":"2019-07-13 06:28:19","hits":199,"username":"monekuson","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1b3n2b2e2m2n383p1h3c2838281h371n3d3h1k3l3c322p2l2o2d3d333l3m1f2i373l1b25383q2g2l3c3k2g1j272l3g3a1j3l2n2q3b1m2h3i292c3j2o26313g2i_3f2f2f312f2o3m23262i2h2e2q2e2n2c272m221m1j2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2l32352p3d3b231n3p2n353g2q1h1b1m3q2e1g3o3c3133273o373q222o3o3n372q2d261m1f23221f1h1b2n26352i1n3b381b332d1f222p1n3e3d353b1f1p3p1k_393k2j1p3i2b3i2g2l2l2g3g3e2g1h3f3d2b371j3p2h1t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 10,
            },
            '学生': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/学生/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":10},"items":[{"id":266646,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2009-08-05 15:16:07","hits":14074,"username":"akiko","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3g3g2a232p261f2k3o273b2q322n272o2n341f1m23351b3f2b1n2o242f281k3829322o1n392329232o1k38272328252l222n312f2p272o1n2m2c2i3j3f2m2k332m361m311f2m363e3h2n2l222m2a212p3p2p333126211t1t_1b2p31222g232d223d1b2q3d3n3p36242g2o272o39371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3o2n3j1k3m2q2c37253d3g3q2h1o2b2o2c1g2939252o2l37393l323q1b3m2f3i3c3c3l1h2e2a3o3l1b2e3627352i2b381b1k1j3h243d3c1b2721253b3d3k2e2k3f253k351i2l3k2l312j1f3e1p262n1o3a212o2a1k3n1t1t_2j3g3l373m1p1j1l332c3n1j332k3i2n1b373h2l28211t1t","rate":0,"num_votes":2,"num_positive_votes":1},{"id":1106335,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2011-04-22 00:41:06","hits":11812,"username":"Emmacaron","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1h2m373o2d212i2a2i2c2l29392q1k2n3h31251i3c2e2f2g3m3q38382i263636232k3l263o34343i322g2n3l2n1b2j1h352j2l2e1l2a212a3j331i3o2n2j3b3e251f1n2i383l3o331p3k2a263f2k2n3b3l2d282l1j211t1t_222324271l3p2p1f2q3537332q251g1h1f29372e2f211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3d1i1j32213i1f3i1p3o1g311f2h283o36342f2d263g3c2q363a3n3i3l1o1n263p1p2q2g382j252e2h2o222g3h3l272o233g1h243l25363g282h29322c222g311l2l222c39273d37222b1i1b1o3d2a1p3e2p2d1b2d2h1t1t_2g1b3p33223h29222q35293a311j263d2d3n213i2n3n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":1326335,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2011-11-21 05:11:59","hits":11685,"username":"yasuo","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/26362n1g34233q3j1b2g2d212c2e1i272f24223p2o2g2c2o1m1g321p1i3b1n1i1g2j333i1p2g3p2k2l2q2k221h2o3l2k2b3n2q3h1j3j3e2h373h283l381j3m2f3o3q2h2q1g1m3k1f27253a3d3m332e3e352h391k2l2h1t1t_2p2g2g3q222f1f2k2g2h393k1f2b28241j3q1h1i3h371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3a1n271n3g2p1m2p341n1f37243l1f21393d2823241p232d2k3f1f2c323m3c3e2e2k1g1f2b3g3b1j3e3p3a32212g3f1m3h2e1i3o332o2g3n2j263q3h1b2g341p2k3l1h3m233k3g1o392m2i2l2q3f2i1k1h2h29373j3n1t1t_1o1m3q312j273q3j3h3d2m2b3h361l3d382q2g3q283n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":3565947,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2015-04-23 05:40:50","hits":24678,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/273j392b242b3e3l3e1f351n2h2e2h1n353p3p2o1g2q273h2k2j3j1l2m283k2o3c24262g3o2b1o293j3j383q31382p1f2k3b3q1h1j212i2k1l371i2a2o263l2d_3h1j2e1l3a222f253c3n1b2l3n3k232d26342g3g2l2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3k3q223o3g212b2a2c2e392a1g2f2f3m283f2f1n292d1m3q2p1b233i262q1m3h1g261p2p2733231o3d34212h3i2n2m1o2j2m1n2q1j1n3g232c3d2g2g283k3c1p_2f332j281l1p242q242p343k292e3j291h2k292932371t1t","rate":8,"num_votes":8,"num_positive_votes":8},{"id":4389512,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2016-06-23 20:36:18","hits":5132,"username":"chiharu","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/242f2i2c3a3q2j1f381n3o211g1o1p292935312o1g2a352o2f2i26241f2k26251p1m2739342h1h2o3b1l381p23251o3k3g2f393n3d1h251j253o2q2h1p2d311j_21352d233b3a352e272b3g1m3b3o2e3i1f3b1b2q332h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1i321k2922233e1i282e221h213m3f39312a393q25313c251m1m2k2k2q3n323c2j373b2g3b1k3o2m352n253f3q3j21393l1m1h333j3q1m3p2h2a2b1j22273e3b_2m2j332j1k3l3o2e2n3n2i1o372g323q251p2p2o23371t1t","rate":-1,"num_votes":1,"num_positive_votes":0},{"id":5240691,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2017-09-30 05:36:18","hits":2346,"username":"le_temps_perdu","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3d1g361g1j3n2j262o2d3o3e2h2l291n1b2n2m3m243e3g212d1b3l2f3j383729293c2k381k262i343e2q2b2b34222j3b2n323d342n3c2m272e1l2q3h1o1f3l2i_2c3g2m2j291l2e3k292h251i3b3l352b27262i1i3i211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2k342k1g2n23222b2c3o1n372q2k3d2q1i36213d1i3q1g3b2k3h3b373l2a1g2l363c231p1f1k2d2j1f2o3a3n2k2l1k233321351l392g3k2h22362e3p3m372d1b_1l1h381p2f3n2e2n2b2i1p3g1i3j2a3b2o3b263j31371t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":5312735,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2017-11-11 20:38:48","hits":2162,"username":"Pantera3","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1g1i2j3l2e332o3e3p2m3h3c231o2e1n3k1g1l261p27273l1f3p1p1m3o2e1k2f292b3p2o283d1l323q211g1l3p243n3k2o2k3j2e1p233m1k3134393i361k2q3c_1k2h3623341p333k2a322j2p3k3g2f2n3721273k1p211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1g2e361p3p3f1h2k2e3o372n2l1o363n341k2m1o3o3i36252f3l2k3322231g3i2b322m3h2i2o3j3e293n3j2a233522262e27233i263c3l2d271n391f1g2l3f2n_3p2n3h291g1k253m2m2l2l3j1f383n2d3c25262a2d211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5451907,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2018-01-26 15:36:42","hits":1695,"username":"erika1993","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2g3j1i343o1k2c3q2c292o3l2o392k39362n351k3a1h1f1j3d2926262a233q2d2f2f3h2k3n1p1i2p31352o243q3n3j2l211f1m33273c3b371o3p29373f1p3q2q_383f272l2m3g1m2e3b39351g2q2h25213q253g3i2e371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1m1j312q3f3o3g1n1p2233223m3233352m3d3l2126311o2q321l292f283p1k2m1l1h27353e1p2822232d2q312a343d2l3c1p1l3n1n363i1k391h3l1l3c3a3h3n_223o252l3q1g313f2i1j253d27223m371m3o3q241j371t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":6228638,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2019-07-13 17:03:52","hits":511,"username":"monekuson","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2q1i2c332j2i3n2q1g2e293m2a3a2b2i2f3e371m2c1k37263a362d1k3p2j2l1h2b22232j3j242k3n2h2q1h1k1n2o2b3a32322n252q272o3o2n3k3n2h3a1h321n_2f2b3p3d2n2j2l3c3n1o1i262e2k3g35372e2i3337211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2a2p3f2n2a3o3q36231o281l3m2j1g1l3f223e35261f213d3c3o3f2b28353d3726242p2l3o1g2i1p2d2m1g3d3q1b3q3a1l223b273q2f3i3f1h2c292o3m2a2g37_3j2m3p3n2d2m2n3528292i2o333a1j3b2j3p2k2931371t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":7825064,"word":"\\u5b66\\u751f","original":"\\u5b66\\u751f","addtime":"2021-06-07 10:43:15","hits":66,"username":"poyotan","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2o1f3g3c1k2i2b2o363f2p1j2d2g2e2e2n3m1j1b2p2d1k1o3q251i3l3i3q3d2g34353i1j3b292q2a1h272l25273h3f36331p1n371h2p343o363f1j2d3d2m322q_2b321o2e3m2p2q37263p1g1n1o273c3j313q2d3p242h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2d1b3c2o1k263c3f2a1f373d2n2l2m2a2g2n2d1g2p3c3l3m223836292g3a2e2c212k1o2i2f3c3g1h3l1l2c283837293c323e2i373i3q2g3k332m3d1p362k1b26_333l3c312q24361o3j3n313d263537383m282o3a1h371t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 10,
            },
        },
        "expected_output": {
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/3f2n2n1f363f1k1k2p2j2c223q383m1m1k1m222m2b3o2k3k3g2i1l1l362g3n1m3f2i3a1k3f2i2k3d2l2b2333212b232q2n281o271l2g2n313l3a3f1b3n363o2a1p2q2o2q1b1n282i273k2q2q2q2h353m383a3c3q1h371t1t_2n1l2b261o1p1m393i233o2a1g2g392p2q3b2n3e2a3n1t1t"),
                            "username": "mi8NatsuKi",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2733252e331g2q3h2928353f28373e2i3d2j33222h2p2l2k1h291i3g3l3f22293224362e3l1f392o353i3q1p2q332l2f291n25322f1b3q2i2h2o212g333g3c1h_243j382k291i1i1f3e283a371b333h3q3i1f3d1m26371t1t"),
                            "username": "kiiro",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/212k29232n2f2e222e31232j243o1m262p3j2j372c2n2q232g351p322l2k2f342d383d2e3q3p3a333a2b2e1g3k3a2a3m2b2f2b1k2n253b263m233q2239332k1j_1g2c1h1l2g2b1m3n1m293k242b2f1n2b2i1f2k1b3b371t1t"),
                            "username": "mutsusoken",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/261p1k363p312g3p2b3p312g382e1f2a1f3o3j2c36363i353b3m2k3d3q392g1i1l1m361l332e271h2g2q363h2h363l3o1f2p233c3c3j2j3l371p1m2n2c1o2g25_1m3b212k26271l2m3d2k2b3c1l1g37313f3p213h1i211t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/273i321j3b2k2a2b3k2l3k2p322p391l1f1p262q2k241l1n2j291i292a3j1h1l2d1l36353i332p3c362l3p3j3b1o1f2p1o2j2q3e1g212f3d3c1i392d3d3n1j2c_1l2o3j3b1h2p1f3a3n2o3k1g322f26233o363e1l3h3n1t1t"),
                            "username": "leona1",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3h3e3e3b2a1g1l1k272223281i3h3p3i282d323c3h1h2l211h2c1l2b3c243c27272g21331n3j2k1i353f3h1o331j292p1k241m1n3i39322c353q1j3h1p3e3i2j_263k2o1m2o351l1f2f223e3l2l1h2q3p1j353d2h3d3n1t1t"),
                            "username": "chiharu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3j2g3o3f2g3q3934322l1o33392g1i361n29353d1l2j1o2n1f362a2k1l3g2h2k29351m3e3a2o1f1i2h2c3l2l2i2j2p283g3c292o212j2h1m3d3p241p1h3q3b2o_242n1f232m263a3j2n2g3i1o1i2d2c3a1m2n1m2d34371t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/39223a3l3g3g2i2l3q272g283m2h2e2726261h1j3j252i273g2p2g243124213b3k3a1o3o2o213m23343j1j3d1o3h3a212h2i332n3d1h2q363j33242i393b3m2l_292o293f2e272j1j33222235373i2q3a38341i373f2h1t1t"),
                            "username": "straycat88",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3f3i241p2g1h3h2f3l251p1j3h2e3q2k38243a3c3h1n2c3k1l1i3e22253d2f3g2i293b1p3f1h2b2d311k2a1g1h3j3o373k1p372l3o1b3h392d3p2i383c1i3633_2q1p2p3a2q3i2n3n2g3f262c382i211m2a3f3p233n2h1t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1b3n2b2e2m2n383p1h3c2838281h371n3d3h1k3l3c322p2l2o2d3d333l3m1f2i373l1b25383q2g2l3c3k2g1j272l3g3a1j3l2n2q3b1m2h3i292c3j2o26313g2i_3f2f2f312f2o3m23262i2h2e2q2e2n2c272m221m1j2h1t1t"),
                            "username": "monekuson",
                        },
                    ],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/3g3g2a232p261f2k3o273b2q322n272o2n341f1m23351b3f2b1n2o242f281k3829322o1n392329232o1k38272328252l222n312f2p272o1n2m2c2i3j3f2m2k332m361m311f2m363e3h2n2l222m2a212p3p2p333126211t1t_1b2p31222g232d223d1b2q3d3n3p36242g2o272o39371t1t"),
                            "username": "akiko",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1h2m373o2d212i2a2i2c2l29392q1k2n3h31251i3c2e2f2g3m3q38382i263636232k3l263o34343i322g2n3l2n1b2j1h352j2l2e1l2a212a3j331i3o2n2j3b3e251f1n2i383l3o331p3k2a263f2k2n3b3l2d282l1j211t1t_222324271l3p2p1f2q3537332q251g1h1f29372e2f211t1t"),
                            "username": "Emmacaron",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/26362n1g34233q3j1b2g2d212c2e1i272f24223p2o2g2c2o1m1g321p1i3b1n1i1g2j333i1p2g3p2k2l2q2k221h2o3l2k2b3n2q3h1j3j3e2h373h283l381j3m2f3o3q2h2q1g1m3k1f27253a3d3m332e3e352h391k2l2h1t1t_2p2g2g3q222f1f2k2g2h393k1f2b28241j3q1h1i3h371t1t"),
                            "username": "yasuo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/273j392b242b3e3l3e1f351n2h2e2h1n353p3p2o1g2q273h2k2j3j1l2m283k2o3c24262g3o2b1o293j3j383q31382p1f2k3b3q1h1j212i2k1l371i2a2o263l2d_3h1j2e1l3a222f253c3n1b2l3n3k232d26342g3g2l2h1t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/242f2i2c3a3q2j1f381n3o211g1o1p292935312o1g2a352o2f2i26241f2k26251p1m2739342h1h2o3b1l381p23251o3k3g2f393n3d1h251j253o2q2h1p2d311j_21352d233b3a352e272b3g1m3b3o2e3i1f3b1b2q332h1t1t"),
                            "username": "chiharu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3d1g361g1j3n2j262o2d3o3e2h2l291n1b2n2m3m243e3g212d1b3l2f3j383729293c2k381k262i343e2q2b2b34222j3b2n323d342n3c2m272e1l2q3h1o1f3l2i_2c3g2m2j291l2e3k292h251i3b3l352b27262i1i3i211t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1g1i2j3l2e332o3e3p2m3h3c231o2e1n3k1g1l261p27273l1f3p1p1m3o2e1k2f292b3p2o283d1l323q211g1l3p243n3k2o2k3j2e1p233m1k3134393i361k2q3c_1k2h3623341p333k2a322j2p3k3g2f2n3721273k1p211t1t"),
                            "username": "Pantera3",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2g3j1i343o1k2c3q2c292o3l2o392k39362n351k3a1h1f1j3d2926262a233q2d2f2f3h2k3n1p1i2p31352o243q3n3j2l211f1m33273c3b371o3p29373f1p3q2q_383f272l2m3g1m2e3b39351g2q2h25213q253g3i2e371t1t"),
                            "username": "erika1993",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2q1i2c332j2i3n2q1g2e293m2a3a2b2i2f3e371m2c1k37263a362d1k3p2j2l1h2b22232j3j242k3n2h2q1h1k1n2o2b3a32322n252q272o3o2n3k3n2h3a1h321n_2f2b3p3d2n2j2l3c3n1o1i262e2k3g35372e2i3337211t1t"),
                            "username": "monekuson",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2o1f3g3c1k2i2b2o363f2p1j2d2g2e2e2n3m1j1b2p2d1k1o3q251i3l3i3q3d2g34353i1j3b292q2a1h272l25273h3f36331p1n371h2p343o363f1j2d3d2m322q_2b321o2e3m2p2q37263p1g1n1o273c3j313q2d3p242h1t1t"),
                            "username": "poyotan",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            '食べる': {
                "url": URL("https://tangorin.com/sentences?search=食べる",),
                "html": get_file_as_string("taberu", "tangorin"),
            },
            '学生': {
                "url": URL("https://tangorin.com/sentences?search=学生",),
                "html": get_file_as_string("gakusei", "tangorin"),
            },
        },
        "expected_output": {
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "私のチョコレートを食べることを考えさえしないで。",
                            "en": "Don't you even think of eating my chocolate!",
                        },
                        {
                            "ja": "野菜を食べたら？",
                            "en": "Why don't you eat some vegetables?",
                        },
                        {
                            "ja": "夏休みの間、私は夜中に夕食を食べていた。",
                            "en": "During summer breaks, I ate dinner at midnight.",
                        },
                        {
                            "ja": "いつご飯食べるの？お腹空いたよ。",
                            "en": "When are we eating? I'm hungry!",
                        },
                        {
                            "ja": "きょう何を昼食に食べましたか。",
                            "en": "What did you have for lunch today?",
                        },
                        {
                            "ja": "私はキャビアを食べた。",
                            "en": "I ate caviar.",
                        },
                        {
                            "ja": "いつから日本人は精白米を食べるようになったのですか？",
                            "en": "When did the Japanese start eating polished rice?",
                        },
                        {
                            "ja": "パックマンが、ある条件を満たすと追ってくるモンスターを逆襲して食べることができる。",
                            "en": "Pac-Man, when a certain condition is reached, can counter attack and eat the monsters chasing him.",
                        },
                        {
                            "ja": "私はストレスがたまると食欲がなくなるのではなく、逆に何か食べないと気が済まなくなる。",
                            "en": "I don't lose my appetite when I get stressed, rather I can't calm down unless I eat something.",
                        },
                        {
                            "ja": "ハゲタカが突っつく死んだ鹿とか、他の動物の食べ残しとか、 そういう腐った肉を死肉と書きました。",
                            "en": "A dead deer being pecked by vultures, remains partly eaten by other animals, that sort of rotten meat is called 'carrion'.",
                        },
                        {
                            "ja": "食べられることなくそのたこは、海に帰ったのであった。",
                            "en": "That octopus returned to the sea without being eaten.",
                        },
                        {
                            "ja": "私達は時々、ドライブを兼ねて大好きなラーメンを食べに行きます。",
                            "en": "We sometimes combine going for a drive with eating the ramen we love so.",
                        },
                    ],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "「以前にどこかで会ったことがありませんか」とその学生はたずねた。",
                            "en": "\"Haven't we met somewhere before?\" asked the student.",
                        },
                        {
                            "ja": "学生が英文論文誌に論文を投稿して、「条件付採録」になっています。",
                            "en": "The student submitted a paper to an English-language journal, and the result was \"conditional acceptance\".",
                        },
                        {
                            "ja": "君たちは学生なんだ、こんなことをやれるのは今だけだ。",
                            "en": "You're students - It's only now what you can do this sort of thing.",
                        },
                        {
                            "ja": "目標は授業設計をするときの、学生の思考を触発するメディア教材の選択および活用方法について理解することである。",
                            "en": "Our aim is that, when planning classes, we know how to select stimulating material for the students and how to put it into use.",
                        },
                        {
                            "ja": "気になってならない俺は思わず、目の前の学生に聞いてしまった。",
                            "en": "It was on my mind so much that I unthinkingly asked the pupil in front of me.",
                        },
                        {
                            "ja": "ただし、学生の本分は学業ですから、期末テストをおろそかにしたらメッ！ですよ？",
                            "en": "However, the duty of a student is to study. So if you neglect the end of term test, that's a \"no!\".",
                        },
                        {
                            "ja": "論文は去年のより長かったが、数人の学生はなんとかし上げた。",
                            "en": "Although the paper was much longer than last year's a few students managed to finish.",
                        },
                        {
                            "ja": "利口な学生達は早くテストを終えた。",
                            "en": "The clever student finished the test quickly.",
                        },
                        {
                            "ja": "利口な学生であればそのような事はしないだろう。",
                            "en": "A clever student would not do such a thing.",
                        },
                        {
                            "ja": "要点を学生に十分理解させた。",
                            "en": "I brought the point home to the student.",
                        },
                    ],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=食べる,学生"),
        "api_response": wanikani_api_responses.TABERU_GAKUSEI,
        "result_dict": {
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/8e5vf9sc17iajyx2d3838oi6chnh"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 27468,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/ng81br3v7kwq5ybljgadillfzqay"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 10592,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        }
                    ],
                    "sentences": [
                        {
                            "en": "I eat natto every morning.",
                            "ja": "毎あさ、なっとうを食べます。"
                        },
                        {
                            "en": "I never have enough time to eat healthy foods.",
                            "ja": "いつも、けんこうにいいものを食べるじかんがないんです。"
                        },
                        {
                            "en": "I like to eat while I’m sleeping. It’s just like sleepwalking, but it’s called sleep-eating.",
                            "ja": "私は、寝ながら食べるのが好きだ。夢遊病のような感じで、それは夢遊食事病と呼ばれる。"
                        },
                    ],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/g2cqz8n0yfcy4n0d45sheojq064j"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 9511,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/l6jqstgdee1l55fnt9906go7fmv1"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 26386,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "Which parts will students study at home today?",
                            "ja": "学生は今日、うちでどこをべんきょうしますか。"
                        },
                        {
                            "en": "Do you have student discount?",
                            "ja": "学生わり引ってありますか？"
                        },
                        {
                            "en": "\"We are all students of life,\" my dad said while farting.",
                            "ja": "「我々はみな人生の学生だ。」と言いながら、父はおならをした。"
                        },
                    ],
                },
            },
        },
        "expected_output": {
            '食べる': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/8e5vf9sc17iajyx2d3838oi6chnh"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 27468,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/ng81br3v7kwq5ybljgadillfzqay"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 10592,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        }
                    ],
                    "sentences": [
                        {
                            "en": "I eat natto every morning.",
                            "ja": "毎あさ、なっとうを食べます。"
                        },
                        {
                            "en": "I never have enough time to eat healthy foods.",
                            "ja": "いつも、けんこうにいいものを食べるじかんがないんです。"
                        },
                        {
                            "en": "I like to eat while I’m sleeping. It’s just like sleepwalking, but it’s called sleep-eating.",
                            "ja": "私は、寝ながら食べるのが好きだ。夢遊病のような感じで、それは夢遊食事病と呼ばれる。"
                        },
                    ],
                },
            },
            '学生': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/g2cqz8n0yfcy4n0d45sheojq064j"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 9511,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/l6jqstgdee1l55fnt9906go7fmv1"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 26386,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "Which parts will students study at home today?",
                            "ja": "学生は今日、うちでどこをべんきょうしますか。"
                        },
                        {
                            "en": "Do you have student discount?",
                            "ja": "学生わり引ってありますか？"
                        },
                        {
                            "en": "\"We are all students of life,\" my dad said while farting.",
                            "ja": "「我々はみな人生の学生だ。」と言いながら、父はおならをした。"
                        },
                    ],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "食べる",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.TABERU_GAKUSEI_FILTERED_ITEMS["食べる"],
                    "extra": jisho_api_responses.TABERU_GAKUSEI_EXTRA_ITEMS["食べる"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("たべ' る")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("たべ' る")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("たべ' る")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/3f2n2n1f363f1k1k2p2j2c223q383m1m1k1m222m2b3o2k3k3g2i1l1l362g3n1m3f2i3a1k3f2i2k3d2l2b2333212b232q2n281o271l2g2n313l3a3f1b3n363o2a1p2q2o2q1b1n282i273k2q2q2q2h353m383a3c3q1h371t1t_2n1l2b261o1p1m393i233o2a1g2g392p2q3b2n3e2a3n1t1t"),
                            "username": "mi8NatsuKi",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2733252e331g2q3h2928353f28373e2i3d2j33222h2p2l2k1h291i3g3l3f22293224362e3l1f392o353i3q1p2q332l2f291n25322f1b3q2i2h2o212g333g3c1h_243j382k291i1i1f3e283a371b333h3q3i1f3d1m26371t1t"),
                            "username": "kiiro",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/212k29232n2f2e222e31232j243o1m262p3j2j372c2n2q232g351p322l2k2f342d383d2e3q3p3a333a2b2e1g3k3a2a3m2b2f2b1k2n253b263m233q2239332k1j_1g2c1h1l2g2b1m3n1m293k242b2f1n2b2i1f2k1b3b371t1t"),
                            "username": "mutsusoken",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/261p1k363p312g3p2b3p312g382e1f2a1f3o3j2c36363i353b3m2k3d3q392g1i1l1m361l332e271h2g2q363h2h363l3o1f2p233c3c3j2j3l371p1m2n2c1o2g25_1m3b212k26271l2m3d2k2b3c1l1g37313f3p213h1i211t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/273i321j3b2k2a2b3k2l3k2p322p391l1f1p262q2k241l1n2j291i292a3j1h1l2d1l36353i332p3c362l3p3j3b1o1f2p1o2j2q3e1g212f3d3c1i392d3d3n1j2c_1l2o3j3b1h2p1f3a3n2o3k1g322f26233o363e1l3h3n1t1t"),
                            "username": "leona1",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3h3e3e3b2a1g1l1k272223281i3h3p3i282d323c3h1h2l211h2c1l2b3c243c27272g21331n3j2k1i353f3h1o331j292p1k241m1n3i39322c353q1j3h1p3e3i2j_263k2o1m2o351l1f2f223e3l2l1h2q3p1j353d2h3d3n1t1t"),
                            "username": "chiharu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3j2g3o3f2g3q3934322l1o33392g1i361n29353d1l2j1o2n1f362a2k1l3g2h2k29351m3e3a2o1f1i2h2c3l2l2i2j2p283g3c292o212j2h1m3d3p241p1h3q3b2o_242n1f232m263a3j2n2g3i1o1i2d2c3a1m2n1m2d34371t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/39223a3l3g3g2i2l3q272g283m2h2e2726261h1j3j252i273g2p2g243124213b3k3a1o3o2o213m23343j1j3d1o3h3a212h2i332n3d1h2q363j33242i393b3m2l_292o293f2e272j1j33222235373i2q3a38341i373f2h1t1t"),
                            "username": "straycat88",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3f3i241p2g1h3h2f3l251p1j3h2e3q2k38243a3c3h1n2c3k1l1i3e22253d2f3g2i293b1p3f1h2b2d311k2a1g1h3j3o373k1p372l3o1b3h392d3p2i383c1i3633_2q1p2p3a2q3i2n3n2g3f262c382i211m2a3f3p233n2h1t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1b3n2b2e2m2n383p1h3c2838281h371n3d3h1k3l3c322p2l2o2d3d333l3m1f2i373l1b25383q2g2l3c3k2g1j272l3g3a1j3l2n2q3b1m2h3i292c3j2o26313g2i_3f2f2f312f2o3m23262i2h2e2q2e2n2c272m221m1j2h1t1t"),
                            "username": "monekuson",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "私のチョコレートを食べることを考えさえしないで。",
                            "en": "Don't you even think of eating my chocolate!",
                        },
                        {
                            "ja": "野菜を食べたら？",
                            "en": "Why don't you eat some vegetables?",
                        },
                        {
                            "ja": "夏休みの間、私は夜中に夕食を食べていた。",
                            "en": "During summer breaks, I ate dinner at midnight.",
                        },
                        {
                            "ja": "いつご飯食べるの？お腹空いたよ。",
                            "en": "When are we eating? I'm hungry!",
                        },
                        {
                            "ja": "きょう何を昼食に食べましたか。",
                            "en": "What did you have for lunch today?",
                        },
                        {
                            "ja": "私はキャビアを食べた。",
                            "en": "I ate caviar.",
                        },
                        {
                            "ja": "いつから日本人は精白米を食べるようになったのですか？",
                            "en": "When did the Japanese start eating polished rice?",
                        },
                        {
                            "ja": "パックマンが、ある条件を満たすと追ってくるモンスターを逆襲して食べることができる。",
                            "en": "Pac-Man, when a certain condition is reached, can counter attack and eat the monsters chasing him.",
                        },
                        {
                            "ja": "私はストレスがたまると食欲がなくなるのではなく、逆に何か食べないと気が済まなくなる。",
                            "en": "I don't lose my appetite when I get stressed, rather I can't calm down unless I eat something.",
                        },
                        {
                            "ja": "ハゲタカが突っつく死んだ鹿とか、他の動物の食べ残しとか、 そういう腐った肉を死肉と書きました。",
                            "en": "A dead deer being pecked by vultures, remains partly eaten by other animals, that sort of rotten meat is called 'carrion'.",
                        },
                        {
                            "ja": "食べられることなくそのたこは、海に帰ったのであった。",
                            "en": "That octopus returned to the sea without being eaten.",
                        },
                        {
                            "ja": "私達は時々、ドライブを兼ねて大好きなラーメンを食べに行きます。",
                            "en": "We sometimes combine going for a drive with eating the ramen we love so.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/8e5vf9sc17iajyx2d3838oi6chnh"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 27468,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/ng81br3v7kwq5ybljgadillfzqay"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 10592,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        }
                    ],
                    "sentences": [
                        {
                            "en": "I eat natto every morning.",
                            "ja": "毎あさ、なっとうを食べます。"
                        },
                        {
                            "en": "I never have enough time to eat healthy foods.",
                            "ja": "いつも、けんこうにいいものを食べるじかんがないんです。"
                        },
                        {
                            "en": "I like to eat while I’m sleeping. It’s just like sleepwalking, but it’s called sleep-eating.",
                            "ja": "私は、寝ながら食べるのが好きだ。夢遊病のような感じで、それは夢遊食事病と呼ばれる。"
                        },
                    ],
                },
            },
        },
        {
            "word": "学生",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.TABERU_GAKUSEI_FILTERED_ITEMS["学生"],
                    "extra": jisho_api_responses.TABERU_GAKUSEI_EXTRA_ITEMS["学生"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("がくせい")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("がくせい")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("がくせい")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/3g3g2a232p261f2k3o273b2q322n272o2n341f1m23351b3f2b1n2o242f281k3829322o1n392329232o1k38272328252l222n312f2p272o1n2m2c2i3j3f2m2k332m361m311f2m363e3h2n2l222m2a212p3p2p333126211t1t_1b2p31222g232d223d1b2q3d3n3p36242g2o272o39371t1t"),
                            "username": "akiko",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1h2m373o2d212i2a2i2c2l29392q1k2n3h31251i3c2e2f2g3m3q38382i263636232k3l263o34343i322g2n3l2n1b2j1h352j2l2e1l2a212a3j331i3o2n2j3b3e251f1n2i383l3o331p3k2a263f2k2n3b3l2d282l1j211t1t_222324271l3p2p1f2q3537332q251g1h1f29372e2f211t1t"),
                            "username": "Emmacaron",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/26362n1g34233q3j1b2g2d212c2e1i272f24223p2o2g2c2o1m1g321p1i3b1n1i1g2j333i1p2g3p2k2l2q2k221h2o3l2k2b3n2q3h1j3j3e2h373h283l381j3m2f3o3q2h2q1g1m3k1f27253a3d3m332e3e352h391k2l2h1t1t_2p2g2g3q222f1f2k2g2h393k1f2b28241j3q1h1i3h371t1t"),
                            "username": "yasuo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/273j392b242b3e3l3e1f351n2h2e2h1n353p3p2o1g2q273h2k2j3j1l2m283k2o3c24262g3o2b1o293j3j383q31382p1f2k3b3q1h1j212i2k1l371i2a2o263l2d_3h1j2e1l3a222f253c3n1b2l3n3k232d26342g3g2l2h1t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/242f2i2c3a3q2j1f381n3o211g1o1p292935312o1g2a352o2f2i26241f2k26251p1m2739342h1h2o3b1l381p23251o3k3g2f393n3d1h251j253o2q2h1p2d311j_21352d233b3a352e272b3g1m3b3o2e3i1f3b1b2q332h1t1t"),
                            "username": "chiharu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3d1g361g1j3n2j262o2d3o3e2h2l291n1b2n2m3m243e3g212d1b3l2f3j383729293c2k381k262i343e2q2b2b34222j3b2n323d342n3c2m272e1l2q3h1o1f3l2i_2c3g2m2j291l2e3k292h251i3b3l352b27262i1i3i211t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1g1i2j3l2e332o3e3p2m3h3c231o2e1n3k1g1l261p27273l1f3p1p1m3o2e1k2f292b3p2o283d1l323q211g1l3p243n3k2o2k3j2e1p233m1k3134393i361k2q3c_1k2h3623341p333k2a322j2p3k3g2f2n3721273k1p211t1t"),
                            "username": "Pantera3",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2g3j1i343o1k2c3q2c292o3l2o392k39362n351k3a1h1f1j3d2926262a233q2d2f2f3h2k3n1p1i2p31352o243q3n3j2l211f1m33273c3b371o3p29373f1p3q2q_383f272l2m3g1m2e3b39351g2q2h25213q253g3i2e371t1t"),
                            "username": "erika1993",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2q1i2c332j2i3n2q1g2e293m2a3a2b2i2f3e371m2c1k37263a362d1k3p2j2l1h2b22232j3j242k3n2h2q1h1k1n2o2b3a32322n252q272o3o2n3k3n2h3a1h321n_2f2b3p3d2n2j2l3c3n1o1i262e2k3g35372e2i3337211t1t"),
                            "username": "monekuson",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2o1f3g3c1k2i2b2o363f2p1j2d2g2e2e2n3m1j1b2p2d1k1o3q251i3l3i3q3d2g34353i1j3b292q2a1h272l25273h3f36331p1n371h2p343o363f1j2d3d2m322q_2b321o2e3m2p2q37263p1g1n1o273c3j313q2d3p242h1t1t"),
                            "username": "poyotan",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "「以前にどこかで会ったことがありませんか」とその学生はたずねた。",
                            "en": "\"Haven't we met somewhere before?\" asked the student.",
                        },
                        {
                            "ja": "学生が英文論文誌に論文を投稿して、「条件付採録」になっています。",
                            "en": "The student submitted a paper to an English-language journal, and the result was \"conditional acceptance\".",
                        },
                        {
                            "ja": "君たちは学生なんだ、こんなことをやれるのは今だけだ。",
                            "en": "You're students - It's only now what you can do this sort of thing.",
                        },
                        {
                            "ja": "目標は授業設計をするときの、学生の思考を触発するメディア教材の選択および活用方法について理解することである。",
                            "en": "Our aim is that, when planning classes, we know how to select stimulating material for the students and how to put it into use.",
                        },
                        {
                            "ja": "気になってならない俺は思わず、目の前の学生に聞いてしまった。",
                            "en": "It was on my mind so much that I unthinkingly asked the pupil in front of me.",
                        },
                        {
                            "ja": "ただし、学生の本分は学業ですから、期末テストをおろそかにしたらメッ！ですよ？",
                            "en": "However, the duty of a student is to study. So if you neglect the end of term test, that's a \"no!\".",
                        },
                        {
                            "ja": "論文は去年のより長かったが、数人の学生はなんとかし上げた。",
                            "en": "Although the paper was much longer than last year's a few students managed to finish.",
                        },
                        {
                            "ja": "利口な学生達は早くテストを終えた。",
                            "en": "The clever student finished the test quickly.",
                        },
                        {
                            "ja": "利口な学生であればそのような事はしないだろう。",
                            "en": "A clever student would not do such a thing.",
                        },
                        {
                            "ja": "要点を学生に十分理解させた。",
                            "en": "I brought the point home to the student.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/g2cqz8n0yfcy4n0d45sheojq064j"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 9511,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/l6jqstgdee1l55fnt9906go7fmv1"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 26386,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "Which parts will students study at home today?",
                            "ja": "学生は今日、うちでどこをべんきょうしますか。"
                        },
                        {
                            "en": "Do you have student discount?",
                            "ja": "学生わり引ってありますか？"
                        },
                        {
                            "en": "\"We are all students of life,\" my dad said while farting.",
                            "ja": "「我々はみな人生の学生だ。」と言いながら、父はおならをした。"
                        },
                    ],
                },
            },
        },
    ],
}


KOTOBA: FullTestDict = {
    "id": "KOTOBA",
    "input": ['言葉'],
    "japanesepod": {
        "expected_sections": {
            "言葉": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ言葉"),
                "html": get_file_as_string("kotoba", "japanesepod"),
            },
        },
        "expected_output": {
            "言葉": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            '言葉': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=言葉"),
                "api_response": jisho_api_responses.KOTOBA["言葉"],
                "filtered_items": jisho_api_responses.KOTOBA_FILTERED_ITEMS["言葉"],
                "extra_items": jisho_api_responses.KOTOBA_EXTRA_ITEMS["言葉"],
            },
        },
        "expected_output": {
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.KOTOBA_FILTERED_ITEMS["言葉"],
                    "extra": jisho_api_responses.KOTOBA_EXTRA_ITEMS["言葉"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("kotoba"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:言葉/page:%s"),
        "expected_sections": [
            {
                'na_adj': False,
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
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ことば'")],
                },
            },
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
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ことば'")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("kotoba", "wadoku"),
        "url": URL("https://www.wadoku.de/search/言葉"),
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
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ことば'")],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            '言葉': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/言葉/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":7},"items":[{"id":525626,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2010-03-26 19:21:25","hits":3543,"username":"renad","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/293o2o1j3e393o1m2636233m3n3b333h1b393e3g2g1n1j342937343n3g1f2h3g3h2d3e3i1f2p1k3n3m332n2k3n21273o1j3j2a1j2d2p352b1k1k1k1b38231l3f3h2f233n2j3j3i2j2p3d37392j1f3n2a352i2q2b25371t1t_3a2k2e2j222c2k212q3b31263g26273g3623352a1k2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2d2i3a1f3l2h3437341h2938233o373g293f1m3o1m2e3o2p1n36232j1n2h3k233d331i313d2p39281k393g2p2c2o1f2732361f3a372k2a29371f3f2p1j1j3i1j3l3j2l3f3n2f1f1h29231o1b2k3p3n3o2e2c3o2323371t1t_1f2l3i3o28243b2f25341h2d262c3q1m2e383d282d371t1t","rate":2,"num_votes":2,"num_positive_votes":2},{"id":1006236,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2011-02-05 05:09:54","hits":2405,"username":"molio","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3a3f3j242g3f1i332l3j2j282a391j23322624351f1l351l242q1g1h2a353k2m29362o3a313k282i2p1f2b3i342o27332k353q2j3n1m2c1p2l26231f2237351n2j373m2n222q3q2l3j392g231p243g3e1n2f243o3l3n1t1t_1o383i3q3m1k3p1f322p332b3i2328242a3e3k3o353n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2p3e21252b3m1g3f2i331m3a273l1p1m2l3m3k3f1f2e1l2k2f3c1g1i3m1b2e2k2527283338371p2e1m3h2d33351k3e2g3637232i2m243g263i3o1i3h3o3q3m2b322d363n3o3a2h31322a2b351o2j3822263n1i1g233n1t1t_2h273k2k3n1i3n291g251f2e3n3a1n3m34393f3q353n1t1t","rate":1,"num_votes":3,"num_positive_votes":2},{"id":1442351,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2012-02-23 08:18:42","hits":2304,"username":"obaka","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/393o3n3p3f3i381n2j273d2i263p2j3d213p3d312c2b3b291n1p283i1b28223b362c37352d1f2m393j3q3b3a2o3p382i341o351b2b382f2n3p293c2e2k2o3p253l1p2h383n362q2d3k2g1m263e231k3g2n392h1g2m371t1t_3o242l1k2j2l29342m2p272h3c2i2d29393d323d3o2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2e211l3f333d1b381m3b1p2j3b1i28241p21312g2i3m3l2g2n1f3l212f3b3i3p2m262i3n2e3h3o2h3j1g1p212n3h3b2a3f37392e1p3k3k241b2931362c273g2k3b222m3c39292g3m3a3o253q1j2n27312a3k243h2i2h1t1t_2k3k3228381l2m322d1p283l2b3n23352o243o37313n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":3613663,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2015-05-16 00:20:39","hits":4343,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1n242n251b3o2g3e291m1h35212d1j1f3n311p1i2e363c1i2j3g3l3q2n3l1h2a2g3h1i1i333o3p3m3n1b393n2c383h2d3b2m3q2j1o1i1j27322c3o1f233k2g2c3p292g3c2j2n252p2c1h231k3a36283h211n3c3c2k2h1t1t_242e2e2c3e3n1k2m2q1o2g2j2j2n1l2i3l2e371p3i3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3b381g352k331f1o2k2n29352g2b2b2j21332c1i322q1f2n372p3d2e1m222f343d211g2k3b2j1k3f221p2o253b2d3p2g262h1b1i1h3n1b2n1p26361o3d39282n3k3h2q1k1b3h233g3j362d1k3q1o3c3p1l3a2d231n371t1t_243g1l2i2o3c221l3c3j363a2f3g2d2i2j3d372h3h3n1t1t","rate":3,"num_votes":3,"num_positive_votes":3},{"id":4747650,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2017-01-05 07:04:03","hits":327,"username":"Kamiike422","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/243a3k282q1i3h332i1g2q3l3q212a1h331m393b31232q3k2c26261m352d3l3b2n2o1b2a3o3b313p3l3k1b3m3e2f36322e1m3e24383k3p2m1o2j362h333n2a1m1n342l29291g2g1j243h272c1n3828271j2f3j3k2k3n1t1t_3n232n2d262i3d1k3p28393h3j3o283c1j1o2q1j3a371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/272m2f372f1o2o3d33242g3c2c1f231k3q2c3q1k3n361m2m3l3e3g1h331p32341i2h1i211g363n3p293g2o1k2b38362j2b372a3a263q293k222p3a1f393j2g1i3e311f2o243g1m2e3j3b291g1b2e2c2g351k1o1o2i211t1t_1n2l3i312o3q3j1o24343q3h3b1g2p3a3i373p2f3e2h1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5239797,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2017-09-29 19:22:56","hits":536,"username":"le_temps_perdu","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2b371j382h1g3o342f2m2g3h2d323e2h31273n363a2p21312i3q2m3p3e1i3e292i3o1h271b1b1j1m1h341p291m3e3c263g2f3a2h3m2e1j332g3g2i1m3g3q1h283a2b2m3d2o391o1p262f3d1j332n2j3a1n222m3n3n211t1t_3p2j2g322b1i2b1h3e2l1i321l292d3a2f331k2i2l3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3k2g1i2i1p3f2k1f1p3f3i3o2q3a31232h21282e3l2p27222p2e2i1j3l2o3e1o1m1o1m281l2o252h32332b3a2g231h2i2d2n3a282e3q3b321h2d311j262q2k392o2n241m24361g342n2g2a1h223a3n2o3n392n2f2k211t1t_1l273e313b2o3h2h3k2i3k2l352h1h1i3a2o3b3n31371t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":7430532,"word":"\\u8a00\\u8449","original":"\\u8a00\\u8449","addtime":"2020-11-11 07:09:46","hits":38,"username":"otiose","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/34363h1n3e271i251i3o3n3q3m2o25383b1i293o2o2o2h2a2d343b2l353127341b3n261k3g2d1n3p1p371p3l3h2i3b221f252q2a223e2e2n2j33323n372a3b28331j1m2h343f3i233a36311f2p1b261n222o3q2h2p211t1t_3h2q392h2g3j1h3j2p3h292b3i212j1o25221k1l1n211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/362m2i3b2k3k2m2f1k26323n373n3j321f341o2l373334222i293l1n292g3m3n3h3a3o3h1p371o2n3p28313h2639382p3p251j1l2a2k3834362o362n3q1b3g3h1h2a1n3k3h3h1o2p321i2k24251g2g2c1o321b361l371t1t_1l341k361b2g391g282n331m3a2c25362f24332j3n211t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 7,
            },
        },
        "expected_output": {
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/293o2o1j3e393o1m2636233m3n3b333h1b393e3g2g1n1j342937343n3g1f2h3g3h2d3e3i1f2p1k3n3m332n2k3n21273o1j3j2a1j2d2p352b1k1k1k1b38231l3f3h2f233n2j3j3i2j2p3d37392j1f3n2a352i2q2b25371t1t_3a2k2e2j222c2k212q3b31263g26273g3623352a1k2h1t1t"),
                            "username": "renad",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3a3f3j242g3f1i332l3j2j282a391j23322624351f1l351l242q1g1h2a353k2m29362o3a313k282i2p1f2b3i342o27332k353q2j3n1m2c1p2l26231f2237351n2j373m2n222q3q2l3j392g231p243g3e1n2f243o3l3n1t1t_1o383i3q3m1k3p1f322p332b3i2328242a3e3k3o353n1t1t"),
                            "username": "molio",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/393o3n3p3f3i381n2j273d2i263p2j3d213p3d312c2b3b291n1p283i1b28223b362c37352d1f2m393j3q3b3a2o3p382i341o351b2b382f2n3p293c2e2k2o3p253l1p2h383n362q2d3k2g1m263e231k3g2n392h1g2m371t1t_3o242l1k2j2l29342m2p272h3c2i2d29393d323d3o2h1t1t"),
                            "username": "obaka",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1n242n251b3o2g3e291m1h35212d1j1f3n311p1i2e363c1i2j3g3l3q2n3l1h2a2g3h1i1i333o3p3m3n1b393n2c383h2d3b2m3q2j1o1i1j27322c3o1f233k2g2c3p292g3c2j2n252p2c1h231k3a36283h211n3c3c2k2h1t1t_242e2e2c3e3n1k2m2q1o2g2j2j2n1l2i3l2e371p3i3n1t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/243a3k282q1i3h332i1g2q3l3q212a1h331m393b31232q3k2c26261m352d3l3b2n2o1b2a3o3b313p3l3k1b3m3e2f36322e1m3e24383k3p2m1o2j362h333n2a1m1n342l29291g2g1j243h272c1n3828271j2f3j3k2k3n1t1t_3n232n2d262i3d1k3p28393h3j3o283c1j1o2q1j3a371t1t"),
                            "username": "Kamiike422",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2b371j382h1g3o342f2m2g3h2d323e2h31273n363a2p21312i3q2m3p3e1i3e292i3o1h271b1b1j1m1h341p291m3e3c263g2f3a2h3m2e1j332g3g2i1m3g3q1h283a2b2m3d2o391o1p262f3d1j332n2j3a1n222m3n3n211t1t_3p2j2g322b1i2b1h3e2l1i321l292d3a2f331k2i2l3n1t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/34363h1n3e271i251i3o3n3q3m2o25383b1i293o2o2o2h2a2d343b2l353127341b3n261k3g2d1n3p1p371p3l3h2i3b221f252q2a223e2e2n2j33323n372a3b28331j1m2h343f3i233a36311f2p1b261n222o3q2h2p211t1t_3h2q392h2g3j1h3j2p3h292b3i212j1o25221k1l1n211t1t"),
                            "username": "otiose",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            '言葉': {
                "url": URL("https://tangorin.com/sentences?search=言葉",),
                "html": get_file_as_string("kotoba", "tangorin"),
            },
        },
        "expected_output": {
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "分からない言葉がたくさんある。",
                            "en": "There are many words that I don't understand.",
                        },
                        {
                            "ja": "このような辞書には、「冷蔵庫」という言葉を使った例文が少なくとも2つは載っているはずだ。",
                            "en": "In a dictionary like this one there should be at least two sentences with \"fridge\".",
                        },
                        {
                            "ja": "あまりに馬鹿げていて言葉にできないことは歌うことで生み出される。",
                            "en": "Everything that is too stupid to say, is sung.",
                        },
                        {
                            "ja": "傍目八目という言葉があるように一度協会から離れて、日本サッカーをみて頂きたい。",
                            "en": "Like the saying that things are seen clearest from outside I wish he'd leave the association for a time and take a look at Japanese soccer.",
                        },
                        {
                            "ja": "「馬鹿」という言葉は、悪い言葉だと言われているが、私の成長してきた環境では、 それほど悪い言葉ではなかったように思う。",
                            "en": "I'm told \"idiot\" is a bad word, but where I grew up it doesn't really feel that bad.",
                        },
                        {
                            "ja": "言葉と行動は一致すべきものだが、実行は難しい。",
                            "en": "Your words are supposed to correspond to your actions, but that is not easy to put into practice.",
                        },
                        {
                            "ja": "お世話になった全ての方々にお礼の言葉を述べたいと思います。",
                            "en": "I'd like to say a word of thanks to all those gentlemen and ladies whose care I have been in.",
                        },
                        {
                            "ja": "ら抜き言葉って知っている？けっこう間違った言葉を使う生徒が多いみたい。",
                            "en": "You know about 'ra-skipped words'? It looks like quite a lot of students are using mistaken words.",
                        },
                        {
                            "ja": "倒置法は言葉の前後を入れ替えることにより文章を強調する効果があります。",
                            "en": "Anastrophe, by switching around words, has the effect of emphasizing text.",
                        },
                        {
                            "ja": "いかにも敬虔なるクリスチャンが送る、礼節重き言葉です。",
                            "en": "So characteristic of what a pious Christian would say, this courteous phrase.",
                        },
                    ],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=言葉"),
        "api_response": wanikani_api_responses.KOTOBA,
        "result_dict": {
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/n7d4o8yizz9oni6whnw5m5ormof7"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 3170,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/07386jhwg98fqg3z9prvdf7n7xr6"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 22011,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "I'd like to hire elves if I could, but It's difficult because of the language barrier.",
                            "ja": "エルフをやといたいのは山々なんですが、言葉のかべがあるのでむずかしいんですよ。"
                        },
                        {
                            "en": "It's hard to put into words, but Koichi is a very special person to me.",
                            "ja": "うまく言葉にできないけど、コウイチはわたしにとってすごく特別な人なの。"
                        },
                        {
                            "en": "I was at a loss for words.",
                            "ja": "私は言葉に詰まった。"
                        },
                    ],
                },
            },
        },
        "expected_output": {
            '言葉': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/n7d4o8yizz9oni6whnw5m5ormof7"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 3170,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/07386jhwg98fqg3z9prvdf7n7xr6"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 22011,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "I'd like to hire elves if I could, but It's difficult because of the language barrier.",
                            "ja": "エルフをやといたいのは山々なんですが、言葉のかべがあるのでむずかしいんですよ。"
                        },
                        {
                            "en": "It's hard to put into words, but Koichi is a very special person to me.",
                            "ja": "うまく言葉にできないけど、コウイチはわたしにとってすごく特別な人なの。"
                        },
                        {
                            "en": "I was at a loss for words.",
                            "ja": "私は言葉に詰まった。"
                        },
                    ],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "言葉",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.KOTOBA_FILTERED_ITEMS["言葉"],
                    "extra": jisho_api_responses.KOTOBA_EXTRA_ITEMS["言葉"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ことば'")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ことば'")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ことば'")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/293o2o1j3e393o1m2636233m3n3b333h1b393e3g2g1n1j342937343n3g1f2h3g3h2d3e3i1f2p1k3n3m332n2k3n21273o1j3j2a1j2d2p352b1k1k1k1b38231l3f3h2f233n2j3j3i2j2p3d37392j1f3n2a352i2q2b25371t1t_3a2k2e2j222c2k212q3b31263g26273g3623352a1k2h1t1t"),
                            "username": "renad",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3a3f3j242g3f1i332l3j2j282a391j23322624351f1l351l242q1g1h2a353k2m29362o3a313k282i2p1f2b3i342o27332k353q2j3n1m2c1p2l26231f2237351n2j373m2n222q3q2l3j392g231p243g3e1n2f243o3l3n1t1t_1o383i3q3m1k3p1f322p332b3i2328242a3e3k3o353n1t1t"),
                            "username": "molio",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/393o3n3p3f3i381n2j273d2i263p2j3d213p3d312c2b3b291n1p283i1b28223b362c37352d1f2m393j3q3b3a2o3p382i341o351b2b382f2n3p293c2e2k2o3p253l1p2h383n362q2d3k2g1m263e231k3g2n392h1g2m371t1t_3o242l1k2j2l29342m2p272h3c2i2d29393d323d3o2h1t1t"),
                            "username": "obaka",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1n242n251b3o2g3e291m1h35212d1j1f3n311p1i2e363c1i2j3g3l3q2n3l1h2a2g3h1i1i333o3p3m3n1b393n2c383h2d3b2m3q2j1o1i1j27322c3o1f233k2g2c3p292g3c2j2n252p2c1h231k3a36283h211n3c3c2k2h1t1t_242e2e2c3e3n1k2m2q1o2g2j2j2n1l2i3l2e371p3i3n1t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/243a3k282q1i3h332i1g2q3l3q212a1h331m393b31232q3k2c26261m352d3l3b2n2o1b2a3o3b313p3l3k1b3m3e2f36322e1m3e24383k3p2m1o2j362h333n2a1m1n342l29291g2g1j243h272c1n3828271j2f3j3k2k3n1t1t_3n232n2d262i3d1k3p28393h3j3o283c1j1o2q1j3a371t1t"),
                            "username": "Kamiike422",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2b371j382h1g3o342f2m2g3h2d323e2h31273n363a2p21312i3q2m3p3e1i3e292i3o1h271b1b1j1m1h341p291m3e3c263g2f3a2h3m2e1j332g3g2i1m3g3q1h283a2b2m3d2o391o1p262f3d1j332n2j3a1n222m3n3n211t1t_3p2j2g322b1i2b1h3e2l1i321l292d3a2f331k2i2l3n1t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/34363h1n3e271i251i3o3n3q3m2o25383b1i293o2o2o2h2a2d343b2l353127341b3n261k3g2d1n3p1p371p3l3h2i3b221f252q2a223e2e2n2j33323n372a3b28331j1m2h343f3i233a36311f2p1b261n222o3q2h2p211t1t_3h2q392h2g3j1h3j2p3h292b3i212j1o25221k1l1n211t1t"),
                            "username": "otiose",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "分からない言葉がたくさんある。",
                            "en": "There are many words that I don't understand.",
                        },
                        {
                            "ja": "このような辞書には、「冷蔵庫」という言葉を使った例文が少なくとも2つは載っているはずだ。",
                            "en": "In a dictionary like this one there should be at least two sentences with \"fridge\".",
                        },
                        {
                            "ja": "あまりに馬鹿げていて言葉にできないことは歌うことで生み出される。",
                            "en": "Everything that is too stupid to say, is sung.",
                        },
                        {
                            "ja": "傍目八目という言葉があるように一度協会から離れて、日本サッカーをみて頂きたい。",
                            "en": "Like the saying that things are seen clearest from outside I wish he'd leave the association for a time and take a look at Japanese soccer.",
                        },
                        {
                            "ja": "「馬鹿」という言葉は、悪い言葉だと言われているが、私の成長してきた環境では、 それほど悪い言葉ではなかったように思う。",
                            "en": "I'm told \"idiot\" is a bad word, but where I grew up it doesn't really feel that bad.",
                        },
                        {
                            "ja": "言葉と行動は一致すべきものだが、実行は難しい。",
                            "en": "Your words are supposed to correspond to your actions, but that is not easy to put into practice.",
                        },
                        {
                            "ja": "お世話になった全ての方々にお礼の言葉を述べたいと思います。",
                            "en": "I'd like to say a word of thanks to all those gentlemen and ladies whose care I have been in.",
                        },
                        {
                            "ja": "ら抜き言葉って知っている？けっこう間違った言葉を使う生徒が多いみたい。",
                            "en": "You know about 'ra-skipped words'? It looks like quite a lot of students are using mistaken words.",
                        },
                        {
                            "ja": "倒置法は言葉の前後を入れ替えることにより文章を強調する効果があります。",
                            "en": "Anastrophe, by switching around words, has the effect of emphasizing text.",
                        },
                        {
                            "ja": "いかにも敬虔なるクリスチャンが送る、礼節重き言葉です。",
                            "en": "So characteristic of what a pious Christian would say, this courteous phrase.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/n7d4o8yizz9oni6whnw5m5ormof7"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 3170,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/07386jhwg98fqg3z9prvdf7n7xr6"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 22011,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "I'd like to hire elves if I could, but It's difficult because of the language barrier.",
                            "ja": "エルフをやといたいのは山々なんですが、言葉のかべがあるのでむずかしいんですよ。"
                        },
                        {
                            "en": "It's hard to put into words, but Koichi is a very special person to me.",
                            "ja": "うまく言葉にできないけど、コウイチはわたしにとってすごく特別な人なの。"
                        },
                        {
                            "en": "I was at a loss for words.",
                            "ja": "私は言葉に詰まった。"
                        },
                    ],
                },
            },
        },
    ],
}


BADINPUT: FullTestDict = {
    "id": "BADINPUT",
    "input": ['BADINPUT'],
    "japanesepod": {
        "expected_sections": {
            "BADINPUT": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJBADINPUT"),
                "html": get_file_as_string("badinput", "japanesepod"),
            },
        },
        "expected_output": {
            "BADINPUT": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            'BADINPUT': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=BADINPUT"),
                "api_response": jisho_api_responses.BADINPUT["BADINPUT"],
                "filtered_items": jisho_api_responses.BADINPUT_FILTERED_ITEMS["BADINPUT"],
                "extra_items": jisho_api_responses.BADINPUT_EXTRA_ITEMS["BADINPUT"],
            },
        },
        "expected_output": {
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.BADINPUT_FILTERED_ITEMS["BADINPUT"],
                    "extra": jisho_api_responses.BADINPUT_EXTRA_ITEMS["BADINPUT"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("badinput"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:BADINPUT/page:%s"),
        "expected_sections": [],
        "full_accent_dict" : defaultdict(list),
        "expected_output": {
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
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
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("badinput", "wadoku"),
        "url": URL("https://www.wadoku.de/search/BADINPUT"),
        "expected_sections": [],
        "full_accent_dict" : defaultdict(list),
        "expected_output": {
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            'BADINPUT': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/BADINPUT/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":0},"items":[]}',
                "total_items": 0,
            },
        },
        "expected_output": {
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            'BADINPUT': {
                "url": URL("https://tangorin.com/sentences?search=BADINPUT",),
                "html": get_file_as_string("badinput", "tangorin"),
            },
        },
        "expected_output": {
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=BADINPUT"),
        "api_response": wanikani_api_responses.BADINPUT,
        "result_dict": {},
        "expected_output": {
            'BADINPUT': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "BADINPUT",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.BADINPUT_FILTERED_ITEMS["BADINPUT"],
                    "extra": jisho_api_responses.BADINPUT_EXTRA_ITEMS["BADINPUT"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    ],
}


USAGI_IKU_KAGO: FullTestDict = {
    "id": "USAGI_IKU_KAGO",
    "input": ['兎', '行く', '籠'],
    "japanesepod": {
        "expected_sections": {
            "兎": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ兎"),
                "html": get_file_as_string("usagi", "japanesepod"),
            },
            "行く": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ行く"),
                "html": get_file_as_string("iku", "japanesepod"),
            },
            "籠": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ籠"),
                "html": get_file_as_string("kago", "japanesepod"),
            },
        },
        "expected_output": {
            "兎": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "行く": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "籠": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            '兎': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=兎"),
                "api_response": jisho_api_responses.USAGI_IKU_KAGO["兎"],
                "filtered_items": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["兎"],
                "extra_items": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["兎"],
            },
            '行く': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=行く"),
                "api_response": jisho_api_responses.USAGI_IKU_KAGO["行く"],
                "filtered_items": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["行く"],
                "extra_items": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["行く"],
            },
            '籠': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=籠"),
                "api_response": jisho_api_responses.USAGI_IKU_KAGO["籠"],
                "filtered_items": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["籠"],
                "extra_items": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["籠"],
            },
        },
        "expected_output": {
            '兎': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["兎"],
                    "extra": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["兎"],
                },
            },
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["行く"],
                    "extra": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["行く"],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["籠"],
                    "extra": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["籠"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("usagi_iku_kago"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:兎%%20行く%%20籠/page:%s"),
        "expected_sections": [
            {
                'na_adj': False,
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'740\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'740\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">行く・行きます</p></div></td>', "html.parser"),
                'writings': ["行く", "行きます"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-2"><span class="inner"><span class="char">い</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">く</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="740_1_1_female" href="#" onclick="pronounce_play(\'740_1_1_female\');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="740_1_1_male" href="#" onclick="pronounce_play(\'740_1_1_male\');return false;"></a></div></div>', "html.parser")],
                'readings': ["いく"],
            },
            {
                'na_adj': False,
                'writing_section': Soup('<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch(\'word\',\'4771\',\'female\');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch(\'word\',\'4771\',\'male\');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">籠</p></div></td>', "html.parser"),
                'writings': ["籠"],
                'reading_sections': [Soup('<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-2"><span class="inner"><span class="char">か</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">ご</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"></div></div>', "html.parser")],
                'readings': ["かご"],
            },
            {
                'na_adj': False,
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
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("いく")],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かご")],
                },
            },
            '兎': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("うさぎ")],
                },
            },
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
            '兎': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("うさぎ")],
                },
            },
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("いく")],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かご")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("usagi_iku_kago", "wadoku"),
        "url": URL("https://www.wadoku.de/search/兎%20行く%20籠"),
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
            '兎': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("うさぎ"), Yomi("う")],
                },
            },
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ゆく"), Yomi("いく")],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かご"), Yomi("こ'")],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            '兎': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/兎/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":3},"items":[{"id":817291,"word":"\\u514e","original":"\\u514e","addtime":"2010-10-11 15:05:37","hits":3331,"username":"akitomo","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/233q3d1n1g3n1h243f3d2i3q24333i2o373d21341h293i2p1j3g3k3p2d2c3i2k2n25382b1g2f2c3g221n1n2i2p2h253636372h262p2c2924352b3e3839331m3722253p3a3k282k333h2g3g3o3q3g381b2e29282i2n2h1t1t_1f2i373c311p2l3q32342g2e1j2q293g2n232e223f2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1k252o3n1j2g2i38231n3g1l282b263l2p3g243d3a1n2l3b322e1k1n36311h3e3k2p323o2o25271h2c2a242g222i1f272h2q3h2c2f3d2g3825242b3o362i2f2n371l222f1h27322c1b1f3d1f2d352h312a3d3o2b2q211t1t_392a29231l31293f3l3f2h2n3j2m27261o1f3e362m211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":1006335,"word":"\\u514e","original":"\\u514e","addtime":"2011-02-05 09:16:09","hits":2950,"username":"molio","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1n2h391n31323i2f3g3o3q3o3m323k1p3p3328242o3n2g3a3h2j34373q2e2o1j3d2j1m3a282i393932263p3m3a2n3e3b1o391g2k1n3d1n1m2e1b243f3g3l1h37312n32233f1k2h1l1b2q1n2o3d2c2q3m392g1o1j2f371t1t_1m2q332d3c2a3e3q323p1k342g2d222a3235271h2i211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2i2p1p353h2l2p3n31223i2k3l391g292g3939273m1i3f3b2f2o3l243e331l352j1g1i3m1g291h3a22271h242g2q3521241m232m1h1g3o3b3n313i2g2b2m3f1i3i2f1p271b3n3d2d3a2k3p3l2g1k3d2323383e2h1f211t1t_1b323l363k2k292d3j3b3k3g392q243a333k1i2j1n211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":2442261,"word":"\\u514e","original":"\\u514e","addtime":"2013-09-07 04:30:07","hits":2985,"username":"naotokyo","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/332m3j3e3l2l333o292b2n2q1o2g1h3n3l3p1l3631223q3c2e313q251j3g2c3f353c251n3d2b3k3i311g1f31242a1g292j2q1i381g1k2f2a3j3k3c3d2k2e3k2k373j3734222o2c371g2a35381n3l3h2n2l2o281n332h1t1t_3h3g2f1b3m313b3e3j2i2n2d3m312i353e1i39342m371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2i2g1h1j2d1f2m2j1l3p26353h1m1i2p31351l2q1i392c383m353p2n1j282d2m22382k392f2k3b2g221n2p3c3e281g2o1b1i292n1i2b3d1m1p3n342d3j1o3b2b3m2229361h1p3g1h3n1k3e233a1i1g2d3b33232e3l3n1t1t_3f3n3j1b2k2i27223i263k2g3e1m33242e381l3o2l371t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 3,
            },
            '行く': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/行く/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":6},"items":[{"id":606126,"word":"\\u884c\\u304f","original":"\\u884c\\u304f","addtime":"2010-05-28 12:42:07","hits":3461,"username":"sorechaude","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/323p3b253h3d1j2d2l21362o39223k1k2f1j37343n332m3533242q2e2d33253i2529211i1f3q2o1l2k3q1j2828391k3d2g3k1j263o2n393k2g3e2q321k3n2j3p1l3n3q2d3j1k3j3a3h1g2j33363o2f251o2b2p3b2a211t1t_3q1h3h1f383m2c39272e1b2c382f3k372n2i3o3i3j211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2d2p2h3b37343i1n232o1h1m2e3g3n3q3i282p3p3f2o2m3m393b2m262239333d1m27242f361f1b3g1b2c1o1b1i1f3924211m3p3k1k3h2q2b3h2q3o3p1j393p3i2j39381i31293k3e1h2m232i281j2j1l2d1i3e3o29211t1t_353j3g213p292m361g3g2l361b3a3l3k25311n221k3n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":1106300,"word":"\\u884c\\u304f","original":"\\u884c\\u304f","addtime":"2011-04-22 00:16:36","hits":3386,"username":"Emmacaron","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3o313m1f292q2l262225283h3f313i1f3e34362m2k2k1n223a2f231f3b3f1b2f1p1g2q28321n3m2k1k2i2e332o2f1l2l3q3a1i211i2k3a3k3l3j3h3g243b3b1b291l273f1l3o2j293c3m212e3f2c2l1j2e2c232c2e371t1t_292d37232g2g393d36282b3p3d263e2j24342k3d3h3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1n3b2f3o3l2d3d2g2j2l1m1f2i38363m2b38221g2q3p213e1n353a3n3g251m3c1f1f3m2a3n392g3o2n221h313k3q2o33322c2m3l3c1f2j3b2k333p2l2n1i2q2n2k353m1l3c1h2l2p3b3c2e1k3j3536331g2l1l1p1i371t1t_1j3b2j322d3j3a2h1o361l2b3b393p3q333a261k3n3n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":3613600,"word":"\\u884c\\u304f","original":"\\u884c\\u304f","addtime":"2015-05-15 23:35:20","hits":5653,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/331j2d3j32333h321g363f28393p2l3o2b2c2l3a1m3k3j3k2l3e1b2m3n3p1o213j1f2g3l222f353q3n2b3o3g2i1m2c1i321n3a2l3j1h3g1l1h2n3e291k3d1m243f253m3o3p2a2q2j293f281g3p363837282m2e21253n1t1t_3527233f3j3q1f353j212g3c233f2m3q2m3l3j2q37371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3b1h392e3l1j3e2p3i372i3o372k3h1g3e26371p361n353a3q362e2c393o372c22312l3d1g3p2n1p3j1f1m2m2e333q2f2h242m371o3g3d322m2h212d3m2j1o312i3e362p1k1p291g363j3b36291p3f1i1l2e2a3h1l371t1t_25292c2d3a2b2b291o271b1b29281i1b1h353h2i292h1t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":3777454,"word":"\\u884c\\u304f","original":"\\u884c\\u304f","addtime":"2015-08-02 21:11:42","hits":4338,"username":"skent","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3p3d353i3k2e2p2m251n3n1l1l2o1m3i1l232k2l281k3l1i333h3k353p3c3o283a1p32332m2c1i3q2b1m1n383f3g3f2a2n362q2f312n342h292a1p212n31361l2b3n3n2l3b2a283e1m371n2a1b371h1i271i242f323n1t1t_1m3b1b2p3p2e2p1k29232c1k2h2o241h2n3d2q3m1l371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3j2h37343c223c1f1g271n332p1o2k1f3e3c2b1p263k342h1l2a1j2d2k3o27331k3l1n313j1g2b1b3l2i1n1b3l22353m3i3728281h3828392g352a282c1b263i2h253a2i1f3h2i282i3b3n2h2d2c3h23232e2k2j3d2h1t1t_1m28262g213d242c2e2e293g3h3l271k1m3j211m2b3n1t1t","rate":1,"num_votes":3,"num_positive_votes":2},{"id":5202023,"word":"\\u884c\\u304f","original":"\\u884c\\u304f","addtime":"2017-09-11 17:39:03","hits":420,"username":"le_temps_perdu","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/37281i1n2f311m2b2k3d1i3p3e3q2b1p2n35241p3o3f3b241j362l1b342k3q2h3f2j241m2h381n2h1b292d2p2l262h3o3g2b3p1i1m341m2128362n1k2h2p1j1g2839383g312i1l21362a3e2o2a2e261h1f3d2e3p2p211t1t_3i263l2k372822241l3h2q3j3i2p2m2a3k252k2p3m371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1g2g3j2f371m1o3k29312d2d2f1l1p2o323h3p343g2e332l3h3e3n1n2a3h1o3f3n2i2i28232j292k33382e3l3c3n3d292k343n2o3b2825351i25343c2n2l352i3f2g3i2i3n3e2k1i3k3j351i1b271f3o243q2h242h2h1t1t_3a272f3c3q2o3b1g362o362j3j252g1b381l33343q371t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5243487,"word":"\\u884c\\u304f","original":"\\u884c\\u304f","addtime":"2017-10-01 00:08:35","hits":343,"username":"usako_usagiclub","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3h242h2e3c3a1j3g2c2g243832332n2n272h1m3k3l3l3i3938321g3q3i2o2j3h321i333g1l2o311h2h353q33242o1f352g2n383l3422353b3a3p2i271j332l3m2l3i1j253q252e3g3j3q1k3h3g3m2l243l36233f3m371t1t_1j213138243c3c27353k3a2m2e3m213l3p252b3e36371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1j1g3k2g372k371h3d1h2c2q3b1f1j3b2b2j1j2a2p3h393j2q2m31341n1k29233h3j2k2a3l2f1m2k33282p1k2j1h1l373n1p2c28292k2k2f1m3b2g32213n3736281b322d3p392g2g382d362l2h1n382e2e2h3a2b1p2h1t1t_1m1b1o1k32272c2l3o3g2i313b2i36393m3d2n353m3n1t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 6,
            },
            '籠': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/籠/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":3},"items":[{"id":1789073,"word":"\\u7c60","original":"\\u7c60","addtime":"2012-10-15 13:01:36","hits":2297,"username":"lemmone","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2d3p3j2i262i3l2g3b371n3g3q2f222o2f341f1j2f3c392j2p1m253f3433232k2g1g2f3q1n281g2i3d1j322q2d2h1k1i2l1p3m233c233j2p39282q3f3g3f3l2o392e2o1b3n3b3a1k2n3l261k371o2d213e1p2m383i371t1t_1m3d1g2m38213h1h2b363f39282c263d283n2c3k2g3n1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/322h2c3i3o3e223139352p3a3c231h3l2j1h363k1p3i3l1n3j1n3b2k221o2h3o1h2p1g3m232632312d2m3g36232f1n27353h3g363c3h37332e2q2k1j3a1g1b1b1b1b2n373d3c3m2c1k3o3k2o38271b1l3m3335223o2h1t1t_29371i361k2n3i2i1p3o33233g2c3l2m3c3a2l2b212h1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":3710676,"word":"\\u7c60","original":"\\u7c60","addtime":"2015-06-27 09:03:02","hits":2220,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/232g3i3a291m331m1h24321o1n2o231g252l261h2h1p2e2q2d2m272e1l353d1n35251i1j321g3p31253k3825313h3p24392c3o3c1g1g1b2j3o3n32212d2g1m3d263g2928213b1f3i3o2l3k1p2k2p393i3c3d2c2135371t1t_1l2g371i1k371n283q29391p261h1n221p25252h3a2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/342d3p3o1g3c1k2k3k383p3322321f1b2h223l371g1f31251b1p1b3b392a3i2l1n2424211l1l2l2k3a3j2q2o2j211i332p1f1o263l323h3i241m1i3n1g1i3b3p2e3e392839332g2l281l292d231j2a242g3n29323i3n1t1t_1i2i1p1m2j1f3o3k3h383f231i23283h1h3e3n3m2h211t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":4059184,"word":"\\u7c60","original":"\\u7c60","addtime":"2015-12-26 04:47:12","hits":2363,"username":"usako_usagiclub","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2c3838233d1o2h2b1p393434271g3q1f3c223g262g1k272k34351j3a1h2934383g1g3c2e3835391k3q36273g2i242j1l2c2b3234253121343g1f253i1n3i262n2p1f2g3d1n2b27392h2321393i1i1m382931371m2b371t1t_2j1j1h2h233g342o1g1n2e29242f2n1f2k331l3839371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3j3b1n3l1f211j2n2a3a2d282f2f1o1f3a1n332n3433372o2l3p3q372j313e25382q2d2k3n313g2l3d3e3b1h212a332a2a2i3j283g253q2d2b2a3g313l2222283l3o3e2e1i3n281b3g3k2e36352i3j333a2q2j2g3n371t1t_1k331h2l2m1f291g1i1m331j323m3j33313p2c1l363n1t1t","rate":1,"num_votes":1,"num_positive_votes":1}]}',
                "total_items": 3,
            },
        },
        "expected_output": {
            '兎':{
                "success": True,
                "error": None,
                "main_data": {
                    "audio":  [
                        {
                            "url": URL("https://apifree.forvo.com/audio/233q3d1n1g3n1h243f3d2i3q24333i2o373d21341h293i2p1j3g3k3p2d2c3i2k2n25382b1g2f2c3g221n1n2i2p2h253636372h262p2c2924352b3e3839331m3722253p3a3k282k333h2g3g3o3q3g381b2e29282i2n2h1t1t_1f2i373c311p2l3q32342g2e1j2q293g2n232e223f2h1t1t"),
                            "username": "akitomo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1n2h391n31323i2f3g3o3q3o3m323k1p3p3328242o3n2g3a3h2j34373q2e2o1j3d2j1m3a282i393932263p3m3a2n3e3b1o391g2k1n3d1n1m2e1b243f3g3l1h37312n32233f1k2h1l1b2q1n2o3d2c2q3m392g1o1j2f371t1t_1m2q332d3c2a3e3q323p1k342g2d222a3235271h2i211t1t"),
                            "username": "molio",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/332m3j3e3l2l333o292b2n2q1o2g1h3n3l3p1l3631223q3c2e313q251j3g2c3f353c251n3d2b3k3i311g1f31242a1g292j2q1i381g1k2f2a3j3k3c3d2k2e3k2k373j3734222o2c371g2a35381n3l3h2n2l2o281n332h1t1t_3h3g2f1b3m313b3e3j2i2n2d3m312i353e1i39342m371t1t"),
                            "username": "naotokyo",
                        },
                    ],
                },
            },
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/323p3b253h3d1j2d2l21362o39223k1k2f1j37343n332m3533242q2e2d33253i2529211i1f3q2o1l2k3q1j2828391k3d2g3k1j263o2n393k2g3e2q321k3n2j3p1l3n3q2d3j1k3j3a3h1g2j33363o2f251o2b2p3b2a211t1t_3q1h3h1f383m2c39272e1b2c382f3k372n2i3o3i3j211t1t"),
                            "username": "sorechaude",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3o313m1f292q2l262225283h3f313i1f3e34362m2k2k1n223a2f231f3b3f1b2f1p1g2q28321n3m2k1k2i2e332o2f1l2l3q3a1i211i2k3a3k3l3j3h3g243b3b1b291l273f1l3o2j293c3m212e3f2c2l1j2e2c232c2e371t1t_292d37232g2g393d36282b3p3d263e2j24342k3d3h3n1t1t"),
                            "username": "Emmacaron",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/331j2d3j32333h321g363f28393p2l3o2b2c2l3a1m3k3j3k2l3e1b2m3n3p1o213j1f2g3l222f353q3n2b3o3g2i1m2c1i321n3a2l3j1h3g1l1h2n3e291k3d1m243f253m3o3p2a2q2j293f281g3p363837282m2e21253n1t1t_3527233f3j3q1f353j212g3c233f2m3q2m3l3j2q37371t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3p3d353i3k2e2p2m251n3n1l1l2o1m3i1l232k2l281k3l1i333h3k353p3c3o283a1p32332m2c1i3q2b1m1n383f3g3f2a2n362q2f312n342h292a1p212n31361l2b3n3n2l3b2a283e1m371n2a1b371h1i271i242f323n1t1t_1m3b1b2p3p2e2p1k29232c1k2h2o241h2n3d2q3m1l371t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/37281i1n2f311m2b2k3d1i3p3e3q2b1p2n35241p3o3f3b241j362l1b342k3q2h3f2j241m2h381n2h1b292d2p2l262h3o3g2b3p1i1m341m2128362n1k2h2p1j1g2839383g312i1l21362a3e2o2a2e261h1f3d2e3p2p211t1t_3i263l2k372822241l3h2q3j3i2p2m2a3k252k2p3m371t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3h242h2e3c3a1j3g2c2g243832332n2n272h1m3k3l3l3i3938321g3q3i2o2j3h321i333g1l2o311h2h353q33242o1f352g2n383l3422353b3a3p2i271j332l3m2l3i1j253q252e3g3j3q1k3h3g3m2l243l36233f3m371t1t_1j213138243c3c27353k3a2m2e3m213l3p252b3e36371t1t"),
                            "username": "usako_usagiclub",
                        },
                    ],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/2d3p3j2i262i3l2g3b371n3g3q2f222o2f341f1j2f3c392j2p1m253f3433232k2g1g2f3q1n281g2i3d1j322q2d2h1k1i2l1p3m233c233j2p39282q3f3g3f3l2o392e2o1b3n3b3a1k2n3l261k371o2d213e1p2m383i371t1t_1m3d1g2m38213h1h2b363f39282c263d283n2c3k2g3n1t1t"),
                            "username": "lemmone",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/232g3i3a291m331m1h24321o1n2o231g252l261h2h1p2e2q2d2m272e1l353d1n35251i1j321g3p31253k3825313h3p24392c3o3c1g1g1b2j3o3n32212d2g1m3d263g2928213b1f3i3o2l3k1p2k2p393i3c3d2c2135371t1t_1l2g371i1k371n283q29391p261h1n221p25252h3a2h1t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2c3838233d1o2h2b1p393434271g3q1f3c223g262g1k272k34351j3a1h2934383g1g3c2e3835391k3q36273g2i242j1l2c2b3234253121343g1f253i1n3i262n2p1f2g3d1n2b27392h2321393i1i1m382931371m2b371t1t_2j1j1h2h233g342o1g1n2e29242f2n1f2k331l3839371t1t"),
                            "username": "usako_usagiclub",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            '兎': {
                "url": URL("https://tangorin.com/sentences?search=兎",),
                "html": get_file_as_string("usagi", "tangorin"),
            },
            '行く': {
                "url": URL("https://tangorin.com/sentences?search=行く",),
                "html": get_file_as_string("iku", "tangorin"),
            },
            '籠': {
                "url": URL("https://tangorin.com/sentences?search=籠",),
                "html": get_file_as_string("kago", "tangorin"),
            },
        },
        "expected_output": {
            '兎': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "「どうかしたの？」と小さい白いウサギが聞きました。",
                            "en": "\"What's the matter?\" asked the little white rabbit.",
                        },
                        {
                            "ja": "母ウサギは、赤ん坊たちを自分のからだで暖かくしている。",
                            "en": "A mother rabbit keeps her babies warm with her own body.",
                        },
                        {
                            "ja": "彼は手品を使って帽子からウサギをとりだした。",
                            "en": "He produced a rabbit out of his hat by magic.",
                        },
                        {
                            "ja": "彼はウサギとりのわなにえさをつけた。",
                            "en": "He baited the trap for rabbits.",
                        },
                        {
                            "ja": "白いウサギと黒いウサギの二匹のウサギがおおきな森の中に住んでいました。",
                            "en": "Two rabbits, a white rabbit and a black rabbit, lived in a large forest.",
                        },
                        {
                            "ja": "突然小さな黒いウサギはすわりこんで、とても悲しそうにみえた。",
                            "en": "Suddenly the little black rabbit sat down, and looked very sad.",
                        },
                        {
                            "ja": "雪の中で、その白兎の姿は見えなかった。",
                            "en": "Against the snow, the white rabbit was invisible.",
                        },
                        {
                            "ja": "次の兎の飼育当番は彼らです。",
                            "en": "They are the next to be on duty for taking care of the rabbits.",
                        },
                        {
                            "ja": "私はウサギの世話をしなければならない。",
                            "en": "I must look after the rabbits.",
                        },
                        {
                            "ja": "私の特製うさぎシチューです。",
                            "en": "It's my special recipe, rabbit stew.",
                        },
                    ],
                },
            },
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "行くよ。",
                            "en": "I will go.",
                        },
                        {
                            "ja": "いつかフランスに行くことは避けられない、それがいつかは分からないけれど。",
                            "en": "It is inevitable that I go to France someday, I just don't know when.",
                        },
                        {
                            "ja": "私たちがそこへ行くかどうかを決めるのは君の責任だ。",
                            "en": "It's up to you to decide whether we'll go there or not.",
                        },
                        {
                            "ja": "「どうして行かないの？」「行きたくないからだよ。」",
                            "en": "\"Why aren't you going?\" \"Because I don't want to.\"",
                        },
                        {
                            "ja": "学校まで１０分で歩いて行ける。",
                            "en": "I can walk to school in ten minutes.",
                        },
                        {
                            "ja": "買い物に行かなければならない。一時間で戻るよ。",
                            "en": "I have to go shopping. I'll be back in an hour.",
                        },
                        {
                            "ja": "最後に家族でディズニーランドへに行ってからもう随分になる。",
                            "en": "It has been so long since I last went to Disneyland with my family.",
                        },
                        {
                            "ja": "今夜教会に行くよ。",
                            "en": "I'm going to church tonight.",
                        },
                        {
                            "ja": "なぜ人々は映画を見に行くのか？",
                            "en": "Why do people go to the movies?",
                        },
                        {
                            "ja": "学校へ行きたくない。",
                            "en": "I don't want to go to school.",
                        },
                    ],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "籠の鳥に水とえさをまいにちやるようにしてください。",
                            "en": "Please see that the birds in the cage get water and food every day.",
                        },
                        {
                            "ja": "籠の中のリンゴの数を数えなさい。",
                            "en": "Count the apples in the basket.",
                        },
                        {
                            "ja": "籠の中で鳥が鳴いていますね。",
                            "en": "There are birds singing in the cage, aren't there?",
                        },
                        {
                            "ja": "卵をすべて一つのかごに入れるな。",
                            "en": "Don't put all your eggs in one basket.",
                        },
                        {
                            "ja": "彼女は草を編んで籠を作った。",
                            "en": "She wove the grass into a basket.",
                        },
                        {
                            "ja": "彼女は花がいっぱい入ったかごを提げていた。",
                            "en": "She was carrying a basket full of flowers.",
                        },
                        {
                            "ja": "彼女はりんごのいっぱい入った籠を持っていた。",
                            "en": "She had a basket full of apples.",
                        },
                        {
                            "ja": "彼女はリンゴでいっぱいのかごをもっていた。",
                            "en": "She had a basket full of apples.",
                        },
                        {
                            "ja": "彼女はりんごがいっぱい入ったかごを持っていた。",
                            "en": "She had a basket full of apples.",
                        },
                        {
                            "ja": "彼女はすばやく子猫を籠の中に閉じ込めた。",
                            "en": "She quickly shut the kitten into a basket.",
                        },
                    ],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=兎,行く,籠"),
        "api_response": wanikani_api_responses.USAGI_IKU_KAGO,
        "result_dict": {
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/i6eq7alp4yn38qsxvlh51ur9sl41"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 9469,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/9wwn90yd3wpl8s9fn3vzf643fm62"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 26344,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "I'm about to go shopping. ",
                            "ja": "今から、かいものに行きます。"
                        },
                        {
                            "en": "Something came up, so I'm not able to make it.",
                            "ja": "ようじができて、行けなくなってしまいました。"
                        },
                        {
                            "en": "I wouldn\u2019t want to go to Mars because they don\u2019t have Taco Bell there.",
                            "ja": "タコベルが無いので火星には行きたくない。"
                        },
                    ],
                },
            },
        },
        "expected_output": {
            '兎': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
            '行く': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/i6eq7alp4yn38qsxvlh51ur9sl41"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 9469,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/9wwn90yd3wpl8s9fn3vzf643fm62"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 26344,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "I'm about to go shopping. ",
                            "ja": "今から、かいものに行きます。"
                        },
                        {
                            "en": "Something came up, so I'm not able to make it.",
                            "ja": "ようじができて、行けなくなってしまいました。"
                        },
                        {
                            "en": "I wouldn\u2019t want to go to Mars because they don\u2019t have Taco Bell there.",
                            "ja": "タコベルが無いので火星には行きたくない。"
                        },
                    ],
                },
            },
            '籠': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "兎",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["兎"],
                    "extra": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["兎"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("うさぎ")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("うさぎ")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("うさぎ"), Yomi("う")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/233q3d1n1g3n1h243f3d2i3q24333i2o373d21341h293i2p1j3g3k3p2d2c3i2k2n25382b1g2f2c3g221n1n2i2p2h253636372h262p2c2924352b3e3839331m3722253p3a3k282k333h2g3g3o3q3g381b2e29282i2n2h1t1t_1f2i373c311p2l3q32342g2e1j2q293g2n232e223f2h1t1t"),
                            "username": "akitomo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1n2h391n31323i2f3g3o3q3o3m323k1p3p3328242o3n2g3a3h2j34373q2e2o1j3d2j1m3a282i393932263p3m3a2n3e3b1o391g2k1n3d1n1m2e1b243f3g3l1h37312n32233f1k2h1l1b2q1n2o3d2c2q3m392g1o1j2f371t1t_1m2q332d3c2a3e3q323p1k342g2d222a3235271h2i211t1t"),
                            "username": "molio",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/332m3j3e3l2l333o292b2n2q1o2g1h3n3l3p1l3631223q3c2e313q251j3g2c3f353c251n3d2b3k3i311g1f31242a1g292j2q1i381g1k2f2a3j3k3c3d2k2e3k2k373j3734222o2c371g2a35381n3l3h2n2l2o281n332h1t1t_3h3g2f1b3m313b3e3j2i2n2d3m312i353e1i39342m371t1t"),
                            "username": "naotokyo",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "「どうかしたの？」と小さい白いウサギが聞きました。",
                            "en": "\"What's the matter?\" asked the little white rabbit.",
                        },
                        {
                            "ja": "母ウサギは、赤ん坊たちを自分のからだで暖かくしている。",
                            "en": "A mother rabbit keeps her babies warm with her own body.",
                        },
                        {
                            "ja": "彼は手品を使って帽子からウサギをとりだした。",
                            "en": "He produced a rabbit out of his hat by magic.",
                        },
                        {
                            "ja": "彼はウサギとりのわなにえさをつけた。",
                            "en": "He baited the trap for rabbits.",
                        },
                        {
                            "ja": "白いウサギと黒いウサギの二匹のウサギがおおきな森の中に住んでいました。",
                            "en": "Two rabbits, a white rabbit and a black rabbit, lived in a large forest.",
                        },
                        {
                            "ja": "突然小さな黒いウサギはすわりこんで、とても悲しそうにみえた。",
                            "en": "Suddenly the little black rabbit sat down, and looked very sad.",
                        },
                        {
                            "ja": "雪の中で、その白兎の姿は見えなかった。",
                            "en": "Against the snow, the white rabbit was invisible.",
                        },
                        {
                            "ja": "次の兎の飼育当番は彼らです。",
                            "en": "They are the next to be on duty for taking care of the rabbits.",
                        },
                        {
                            "ja": "私はウサギの世話をしなければならない。",
                            "en": "I must look after the rabbits.",
                        },
                        {
                            "ja": "私の特製うさぎシチューです。",
                            "en": "It's my special recipe, rabbit stew.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
        {
            "word": "行く",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["行く"],
                    "extra": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["行く"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("いく")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("いく")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("ゆく"), Yomi("いく")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/323p3b253h3d1j2d2l21362o39223k1k2f1j37343n332m3533242q2e2d33253i2529211i1f3q2o1l2k3q1j2828391k3d2g3k1j263o2n393k2g3e2q321k3n2j3p1l3n3q2d3j1k3j3a3h1g2j33363o2f251o2b2p3b2a211t1t_3q1h3h1f383m2c39272e1b2c382f3k372n2i3o3i3j211t1t"),
                            "username": "sorechaude",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3o313m1f292q2l262225283h3f313i1f3e34362m2k2k1n223a2f231f3b3f1b2f1p1g2q28321n3m2k1k2i2e332o2f1l2l3q3a1i211i2k3a3k3l3j3h3g243b3b1b291l273f1l3o2j293c3m212e3f2c2l1j2e2c232c2e371t1t_292d37232g2g393d36282b3p3d263e2j24342k3d3h3n1t1t"),
                            "username": "Emmacaron",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/331j2d3j32333h321g363f28393p2l3o2b2c2l3a1m3k3j3k2l3e1b2m3n3p1o213j1f2g3l222f353q3n2b3o3g2i1m2c1i321n3a2l3j1h3g1l1h2n3e291k3d1m243f253m3o3p2a2q2j293f281g3p363837282m2e21253n1t1t_3527233f3j3q1f353j212g3c233f2m3q2m3l3j2q37371t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3p3d353i3k2e2p2m251n3n1l1l2o1m3i1l232k2l281k3l1i333h3k353p3c3o283a1p32332m2c1i3q2b1m1n383f3g3f2a2n362q2f312n342h292a1p212n31361l2b3n3n2l3b2a283e1m371n2a1b371h1i271i242f323n1t1t_1m3b1b2p3p2e2p1k29232c1k2h2o241h2n3d2q3m1l371t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/37281i1n2f311m2b2k3d1i3p3e3q2b1p2n35241p3o3f3b241j362l1b342k3q2h3f2j241m2h381n2h1b292d2p2l262h3o3g2b3p1i1m341m2128362n1k2h2p1j1g2839383g312i1l21362a3e2o2a2e261h1f3d2e3p2p211t1t_3i263l2k372822241l3h2q3j3i2p2m2a3k252k2p3m371t1t"),
                            "username": "le_temps_perdu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3h242h2e3c3a1j3g2c2g243832332n2n272h1m3k3l3l3i3938321g3q3i2o2j3h321i333g1l2o311h2h353q33242o1f352g2n383l3422353b3a3p2i271j332l3m2l3i1j253q252e3g3j3q1k3h3g3m2l243l36233f3m371t1t_1j213138243c3c27353k3a2m2e3m213l3p252b3e36371t1t"),
                            "username": "usako_usagiclub",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "行くよ。",
                            "en": "I will go.",
                        },
                        {
                            "ja": "いつかフランスに行くことは避けられない、それがいつかは分からないけれど。",
                            "en": "It is inevitable that I go to France someday, I just don't know when.",
                        },
                        {
                            "ja": "私たちがそこへ行くかどうかを決めるのは君の責任だ。",
                            "en": "It's up to you to decide whether we'll go there or not.",
                        },
                        {
                            "ja": "「どうして行かないの？」「行きたくないからだよ。」",
                            "en": "\"Why aren't you going?\" \"Because I don't want to.\"",
                        },
                        {
                            "ja": "学校まで１０分で歩いて行ける。",
                            "en": "I can walk to school in ten minutes.",
                        },
                        {
                            "ja": "買い物に行かなければならない。一時間で戻るよ。",
                            "en": "I have to go shopping. I'll be back in an hour.",
                        },
                        {
                            "ja": "最後に家族でディズニーランドへに行ってからもう随分になる。",
                            "en": "It has been so long since I last went to Disneyland with my family.",
                        },
                        {
                            "ja": "今夜教会に行くよ。",
                            "en": "I'm going to church tonight.",
                        },
                        {
                            "ja": "なぜ人々は映画を見に行くのか？",
                            "en": "Why do people go to the movies?",
                        },
                        {
                            "ja": "学校へ行きたくない。",
                            "en": "I don't want to go to school.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/i6eq7alp4yn38qsxvlh51ur9sl41"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 9469,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/9wwn90yd3wpl8s9fn3vzf643fm62"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 26344,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "I'm about to go shopping. ",
                            "ja": "今から、かいものに行きます。"
                        },
                        {
                            "en": "Something came up, so I'm not able to make it.",
                            "ja": "ようじができて、行けなくなってしまいました。"
                        },
                        {
                            "en": "I wouldn\u2019t want to go to Mars because they don\u2019t have Taco Bell there.",
                            "ja": "タコベルが無いので火星には行きたくない。"
                        },
                    ],
                },
            },
        },
        {
            "word": "籠",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.USAGI_IKU_KAGO_FILTERED_ITEMS["籠"],
                    "extra": jisho_api_responses.USAGI_IKU_KAGO_EXTRA_ITEMS["籠"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かご")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かご")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("かご"), Yomi("こ'")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/2d3p3j2i262i3l2g3b371n3g3q2f222o2f341f1j2f3c392j2p1m253f3433232k2g1g2f3q1n281g2i3d1j322q2d2h1k1i2l1p3m233c233j2p39282q3f3g3f3l2o392e2o1b3n3b3a1k2n3l261k371o2d213e1p2m383i371t1t_1m3d1g2m38213h1h2b363f39282c263d283n2c3k2g3n1t1t"),
                            "username": "lemmone",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/232g3i3a291m331m1h24321o1n2o231g252l261h2h1p2e2q2d2m272e1l353d1n35251i1j321g3p31253k3825313h3p24392c3o3c1g1g1b2j3o3n32212d2g1m3d263g2928213b1f3i3o2l3k1p2k2p393i3c3d2c2135371t1t_1l2g371i1k371n283q29391p261h1n221p25252h3a2h1t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2c3838233d1o2h2b1p393434271g3q1f3c223g262g1k272k34351j3a1h2934383g1g3c2e3835391k3q36273g2i242j1l2c2b3234253121343g1f253i1n3i262n2p1f2g3d1n2b27392h2321393i1i1m382931371m2b371t1t_2j1j1h2h233g342o1g1n2e29242f2n1f2k331l3839371t1t"),
                            "username": "usako_usagiclub",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "籠の鳥に水とえさをまいにちやるようにしてください。",
                            "en": "Please see that the birds in the cage get water and food every day.",
                        },
                        {
                            "ja": "籠の中のリンゴの数を数えなさい。",
                            "en": "Count the apples in the basket.",
                        },
                        {
                            "ja": "籠の中で鳥が鳴いていますね。",
                            "en": "There are birds singing in the cage, aren't there?",
                        },
                        {
                            "ja": "卵をすべて一つのかごに入れるな。",
                            "en": "Don't put all your eggs in one basket.",
                        },
                        {
                            "ja": "彼女は草を編んで籠を作った。",
                            "en": "She wove the grass into a basket.",
                        },
                        {
                            "ja": "彼女は花がいっぱい入ったかごを提げていた。",
                            "en": "She was carrying a basket full of flowers.",
                        },
                        {
                            "ja": "彼女はりんごのいっぱい入った籠を持っていた。",
                            "en": "She had a basket full of apples.",
                        },
                        {
                            "ja": "彼女はリンゴでいっぱいのかごをもっていた。",
                            "en": "She had a basket full of apples.",
                        },
                        {
                            "ja": "彼女はりんごがいっぱい入ったかごを持っていた。",
                            "en": "She had a basket full of apples.",
                        },
                        {
                            "ja": "彼女はすばやく子猫を籠の中に閉じ込めた。",
                            "en": "She quickly shut the kitten into a basket.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    ],
}


SHIZUKA: FullTestDict = {
    "id": "SHIZUKA",
    "input": ['静か'],
    "japanesepod": {
        "expected_sections": {
            "静か": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ静か"),
                "html": get_file_as_string("shizuka", "japanesepod"),
            },
        },
        "expected_output": {
            "静か": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            '静か': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=静か"),
                "api_response": jisho_api_responses.SHIZUKA["静か"],
                "filtered_items": jisho_api_responses.SHIZUKA_FILTERED_ITEMS["静か"],
                "extra_items": jisho_api_responses.SHIZUKA_EXTRA_ITEMS["静か"],
            },
        },
        "expected_output": {
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.SHIZUKA_FILTERED_ITEMS["静か"],
                    "extra": jisho_api_responses.SHIZUKA_EXTRA_ITEMS["静か"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("shizuka"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:静か/page:%s"),
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
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("し' ずか")],
                },
            },
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
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("し' ずか")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("shizuka", "wadoku"),
        "url": URL("https://www.wadoku.de/search/静か"),
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
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("し' ずか")],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            '静か': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/静か/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes":{"total":5},"items":[{"id":159793,"word":"\\u9759\\u304b","original":"\\u9759\\u304b","addtime":"2009-04-28 01:56:29","hits":2272,"username":"nohunohu","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/2n352q1f2n3a333a3j223i3d1o2c1p3h1k212g3k3f1l3p2b38232n2l2f1k27263j243432372f3b2q2h39213l1g282c311h263b3j2b3q2m362j3a2n1h1l363j331j2b3a37213c2j212j2e2b1o3b3i1p2k2o1m2c353i211t1t_3b1i2m373c1l242i1k373o2o362l212m3o3l2k2p3p371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/3q271h3d3p2m3d2m3j1p342n1k233g373l2n3q33212g323k3c2m3o3l3o1g322l1o3i1m38322c1b2d3c352i2q262e352l2m2g1l2a1k2k3f2d1l3p372d33292f33292722232m2e3j333j3p3g3k22211f3p3i3m1l3a1m2h1t1t_273l2g1j2k3e2b3q1n2m24342g36321g1f2i2e3h323n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":1775342,"word":"\\u9759\\u304b","original":"\\u9759\\u304b","addtime":"2012-10-09 11:52:56","hits":3875,"username":"JunkoHanabi","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/3i1i352d342d2g24212b3p1k2k2c232l25262f3i3m313j3e2f2a1m1b1j222i1g1f333a1p2g2n2m32352a1n2p1f2a2d2o2j2f3e222i3i1m26281l2b1m232q3m1m1k2e263b263g3n2e2o391p1f1b2c3i1l22393434262h1t1t_1k3d1k2e333k3d3e253b292n2g1h1k2b1l1b24291g2h1t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/33393o1j1l2c3f3i3g331p331j3i34252g2c3l2q253k2f2m343i2i3n212g1j271i262l2o2e1p323p3q271g361k1b3m341l2e2h373q383d33373f223q2n3k2j1m3m2p28211g383b3l28223e262l1m3l353i292e1o2g2h1t1t_3p3e33381p1h1g1p21211n2b2j3o1p1l3235272335211t1t","rate":1,"num_votes":1,"num_positive_votes":1},{"id":3563204,"word":"\\u9759\\u304b","original":"\\u9759\\u304b","addtime":"2015-04-22 00:07:47","hits":4009,"username":"strawberrybrown","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/232c1l28231l3n2b3q232h2b323n2q263i2i3b383d1g2n3c1m3a273e3p3q241f231b3g391i3k3q2c1j2j3k353i2g1g391i221m1b262l3h1g3f2p3g1g3b3j2g223d342c3m2c38281i33311g353j281g1g2o2b1f3n1m371t1t_2f2m3g253n28362l3j3n2k1l242g271j1p2c2a2p1m371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/1k281f2k363q3l391g243n3j2n242n313f3o2m1h3h2f373h383e243i3h243m3d1m3c2i393h1f321p2n332l2k3a3g361m1o383k2c2a1m252e283i1h1j362o3c3f291l312f1f28212j1p3c1i223a3n2i3e322o363p2q3n1t1t_2m1n2q21311b3m292j3m2e3h242g2a332h31331o3o371t1t","rate":3,"num_votes":3,"num_positive_votes":3},{"id":5235281,"word":"\\u9759\\u304b","original":"\\u9759\\u304b","addtime":"2017-09-28 02:18:46","hits":646,"username":"straycat88","sex":"f","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/1m3f3h3m363b2l242737211h34281f1o2b37362m3b2g2k3d1j2f3n3a2o1m1g1l1i3k272k323i2k3i3139342f1h3m332i2e243m1l3c1g293232283p1g1b291p1f1k223l273b382l3c212i211l1p313m2h1l3g2g1g2b211t1t_2c21373q2q2d1j2o29211h372j1h38332l253o3g3d211t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/2o1p2k2e3e2b3c3e3q3f2l282j1h293f2c2i37373h3m292i1j1m3b2g2k212f3f3q282e312e1k3c3g1p34223q3b3e252q3f3e1l382e2d213p2i1i3e2o3a3j2o2i25292c1g26211o1k2h1o1n3q2a1n3q312f253p332a211t1t_1i2p3b1o2h242725212d2n2o2e1j3h3a3p1i1m3m323n1t1t","rate":0,"num_votes":0,"num_positive_votes":0},{"id":5236567,"word":"\\u9759\\u304b","original":"\\u9759\\u304b","addtime":"2017-09-28 20:36:26","hits":409,"username":"skent","sex":"m","country":"Japan","code":"ja","langname":"Japanese","pathmp3":"https:\\/\\/apifree.forvo.com\\/audio\\/362534211m1j372l1m242g243o31241n293l1p2f2a2l3l1g363428233j2a1f1l3a23352p3i2b3335263d241g36333c1k261g382l1o2e38371n1m1n23292n1g3n2p2f1f1n2d2232391l1j273j3e1i343e3j3d3i3j293n1t1t_1k233b2l332g3n2c2g2q331o2q282p3m213p3m2m3g371t1t","pathogg":"https:\\/\\/apifree.forvo.com\\/audio\\/391p3j1i2p3i1f31373b2b351f1n2p3p281i1j1h3h3f2f3l2c3c2n3d3b3g39281l1k2m1o323h3h26321j3q1k1n2k1p2p2h331k2m3l2f3c3c2b3b3d2b1p3d383f3j39292m3d3d1h1f1b2m3b3k3221261p3m1n3b2d1k371t1t_3137272l3n3p332c383l2o2p21352h2k312b3p2o3o211t1t","rate":0,"num_votes":0,"num_positive_votes":0}]}',
                "total_items": 5,
            },
        },
        "expected_output": {
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/2n352q1f2n3a333a3j223i3d1o2c1p3h1k212g3k3f1l3p2b38232n2l2f1k27263j243432372f3b2q2h39213l1g282c311h263b3j2b3q2m362j3a2n1h1l363j331j2b3a37213c2j212j2e2b1o3b3i1p2k2o1m2c353i211t1t_3b1i2m373c1l242i1k373o2o362l212m3o3l2k2p3p371t1t"),
                            "username": "nohunohu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3i1i352d342d2g24212b3p1k2k2c232l25262f3i3m313j3e2f2a1m1b1j222i1g1f333a1p2g2n2m32352a1n2p1f2a2d2o2j2f3e222i3i1m26281l2b1m232q3m1m1k2e263b263g3n2e2o391p1f1b2c3i1l22393434262h1t1t_1k3d1k2e333k3d3e253b292n2g1h1k2b1l1b24291g2h1t1t"),
                            "username": "JunkoHanabi",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/232c1l28231l3n2b3q232h2b323n2q263i2i3b383d1g2n3c1m3a273e3p3q241f231b3g391i3k3q2c1j2j3k353i2g1g391i221m1b262l3h1g3f2p3g1g3b3j2g223d342c3m2c38281i33311g353j281g1g2o2b1f3n1m371t1t_2f2m3g253n28362l3j3n2k1l242g271j1p2c2a2p1m371t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1m3f3h3m363b2l242737211h34281f1o2b37362m3b2g2k3d1j2f3n3a2o1m1g1l1i3k272k323i2k3i3139342f1h3m332i2e243m1l3c1g293232283p1g1b291p1f1k223l273b382l3c212i211l1p313m2h1l3g2g1g2b211t1t_2c21373q2q2d1j2o29211h372j1h38332l253o3g3d211t1t"),
                            "username": "straycat88",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/362534211m1j372l1m242g243o31241n293l1p2f2a2l3l1g363428233j2a1f1l3a23352p3i2b3335263d241g36333c1k261g382l1o2e38371n1m1n23292n1g3n2p2f1f1n2d2232391l1j273j3e1i343e3j3d3i3j293n1t1t_1k233b2l332g3n2c2g2q331o2q282p3m213p3m2m3g371t1t"),
                            "username": "skent",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            '静か': {
                "url": URL("https://tangorin.com/sentences?search=静か",),
                "html": get_file_as_string("shizuka", "tangorin"),
            },
        },
        "expected_output": {
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "奈良は静かで、きれいな町です。",
                            "en": "Nara is a quiet and beautiful city.",
                        },
                        {
                            "ja": "シックで上品な制服と歴史ある静かな雰囲気が特徴の女子高なのだという。",
                            "en": "It's said to be a girls' high school characterised by its quiet and traditional feel and a chic, high-class uniform.",
                        },
                        {
                            "ja": "授業の終わり近くになると、教師が一言も「静かにしなさい」「座りなさい！」と言わないにもかかわらず、自然と子どもたちは自分の席に戻り静かになる。",
                            "en": "As the lesson comes to an end, even if the teacher doesn't say a word of \"be quiet\", \"sit down!,\" the children naturally return to their seats and quieten down.",
                        },
                        {
                            "ja": "今はフレッドの錯乱が治まって静かに眠っています。",
                            "en": "Fred's agitation has now subsided, and he's sleeping peacefully.",
                        },
                        {
                            "ja": "花火の弾ける音が止むと、急に辺りが静かになる。後に残った火薬の匂いが、なんだか俺をセンチメンタルな気分にさせた。",
                            "en": "As the popping sound of the fireworks stopped, it suddenly became quiet around me. The smell of gunpowder somehow put me in a sentimental mood.",
                        },
                        {
                            "ja": "流れの静かな川は水が深い。",
                            "en": "Still waters run deep.",
                        },
                        {
                            "ja": "嵐のあとは静かだった。",
                            "en": "After the storm, it was calm.",
                        },
                        {
                            "ja": "頼むから静かにしてよ。",
                            "en": "Do be quiet, please!",
                        },
                        {
                            "ja": "役に立つ面会の最も大切な条件は、医師と親がくつろいで、他人に邪魔されずに当事者だけで座ることのできる静かな部屋だ。",
                            "en": "An essential condition for a helpful interview is a quiet room in which doctor and parents can sit comfortably and in private without being interrupted.",
                        },
                        {
                            "ja": "母親は子供たちに静かにするように言った。",
                            "en": "The mother told the children to be quiet.",
                        },
                    ],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=静か"),
        "api_response": wanikani_api_responses.SHIZUKA,
        "result_dict": {
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/awv61bmcmf9w4m7p057jqubhu3f1"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 4367,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/pkutc4gv3nxpmuo1dba6iv6p5luh"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 22694,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "We'd prefer a house on a quiet street.",
                            "ja": "静かな通りにある家の方がいいです。"
                        },
                        {
                            "en": "I know you have diarrhea, but could you keep it down a bit more, please?",
                            "ja": "下りなのは分かりますが、もう少し静かにしていただけますか？"
                        },
                        {
                            "en": "When Koichi and Viet got in, the taxi quietly started to move.",
                            "ja": "コウイチとビエトが乗り込むと、そのタクシーは静かに動き出した。"
                        },
                    ],
                },
            },
        },
        "expected_output": {
            '静か': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/awv61bmcmf9w4m7p057jqubhu3f1"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 4367,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/pkutc4gv3nxpmuo1dba6iv6p5luh"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 22694,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "We'd prefer a house on a quiet street.",
                            "ja": "静かな通りにある家の方がいいです。"
                        },
                        {
                            "en": "I know you have diarrhea, but could you keep it down a bit more, please?",
                            "ja": "下りなのは分かりますが、もう少し静かにしていただけますか？"
                        },
                        {
                            "en": "When Koichi and Viet got in, the taxi quietly started to move.",
                            "ja": "コウイチとビエトが乗り込むと、そのタクシーは静かに動き出した。"
                        },
                    ],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "静か",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.SHIZUKA_FILTERED_ITEMS["静か"],
                    "extra": jisho_api_responses.SHIZUKA_EXTRA_ITEMS["静か"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("し' ずか")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("し' ずか")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("し' ずか")],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/2n352q1f2n3a333a3j223i3d1o2c1p3h1k212g3k3f1l3p2b38232n2l2f1k27263j243432372f3b2q2h39213l1g282c311h263b3j2b3q2m362j3a2n1h1l363j331j2b3a37213c2j212j2e2b1o3b3i1p2k2o1m2c353i211t1t_3b1i2m373c1l242i1k373o2o362l212m3o3l2k2p3p371t1t"),
                            "username": "nohunohu",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/3i1i352d342d2g24212b3p1k2k2c232l25262f3i3m313j3e2f2a1m1b1j222i1g1f333a1p2g2n2m32352a1n2p1f2a2d2o2j2f3e222i3i1m26281l2b1m232q3m1m1k2e263b263g3n2e2o391p1f1b2c3i1l22393434262h1t1t_1k3d1k2e333k3d3e253b292n2g1h1k2b1l1b24291g2h1t1t"),
                            "username": "JunkoHanabi",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/232c1l28231l3n2b3q232h2b323n2q263i2i3b383d1g2n3c1m3a273e3p3q241f231b3g391i3k3q2c1j2j3k353i2g1g391i221m1b262l3h1g3f2p3g1g3b3j2g223d342c3m2c38281i33311g353j281g1g2o2b1f3n1m371t1t_2f2m3g253n28362l3j3n2k1l242g271j1p2c2a2p1m371t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/1m3f3h3m363b2l242737211h34281f1o2b37362m3b2g2k3d1j2f3n3a2o1m1g1l1i3k272k323i2k3i3139342f1h3m332i2e243m1l3c1g293232283p1g1b291p1f1k223l273b382l3c212i211l1p313m2h1l3g2g1g2b211t1t_2c21373q2q2d1j2o29211h372j1h38332l253o3g3d211t1t"),
                            "username": "straycat88",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/362534211m1j372l1m242g243o31241n293l1p2f2a2l3l1g363428233j2a1f1l3a23352p3i2b3335263d241g36333c1k261g382l1o2e38371n1m1n23292n1g3n2p2f1f1n2d2232391l1j273j3e1i343e3j3d3i3j293n1t1t_1k233b2l332g3n2c2g2q331o2q282p3m213p3m2m3g371t1t"),
                            "username": "skent",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "奈良は静かで、きれいな町です。",
                            "en": "Nara is a quiet and beautiful city.",
                        },
                        {
                            "ja": "シックで上品な制服と歴史ある静かな雰囲気が特徴の女子高なのだという。",
                            "en": "It's said to be a girls' high school characterised by its quiet and traditional feel and a chic, high-class uniform.",
                        },
                        {
                            "ja": "授業の終わり近くになると、教師が一言も「静かにしなさい」「座りなさい！」と言わないにもかかわらず、自然と子どもたちは自分の席に戻り静かになる。",
                            "en": "As the lesson comes to an end, even if the teacher doesn't say a word of \"be quiet\", \"sit down!,\" the children naturally return to their seats and quieten down.",
                        },
                        {
                            "ja": "今はフレッドの錯乱が治まって静かに眠っています。",
                            "en": "Fred's agitation has now subsided, and he's sleeping peacefully.",
                        },
                        {
                            "ja": "花火の弾ける音が止むと、急に辺りが静かになる。後に残った火薬の匂いが、なんだか俺をセンチメンタルな気分にさせた。",
                            "en": "As the popping sound of the fireworks stopped, it suddenly became quiet around me. The smell of gunpowder somehow put me in a sentimental mood.",
                        },
                        {
                            "ja": "流れの静かな川は水が深い。",
                            "en": "Still waters run deep.",
                        },
                        {
                            "ja": "嵐のあとは静かだった。",
                            "en": "After the storm, it was calm.",
                        },
                        {
                            "ja": "頼むから静かにしてよ。",
                            "en": "Do be quiet, please!",
                        },
                        {
                            "ja": "役に立つ面会の最も大切な条件は、医師と親がくつろいで、他人に邪魔されずに当事者だけで座ることのできる静かな部屋だ。",
                            "en": "An essential condition for a helpful interview is a quiet room in which doctor and parents can sit comfortably and in private without being interrupted.",
                        },
                        {
                            "ja": "母親は子供たちに静かにするように言った。",
                            "en": "The mother told the children to be quiet.",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://files.wanikani.com/awv61bmcmf9w4m7p057jqubhu3f1"),
                            "metadata": {
                                "gender": "male",
                                "source_id": 4367,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                        {
                            "url": URL("https://files.wanikani.com/pkutc4gv3nxpmuo1dba6iv6p5luh"),
                            "metadata": {
                                "gender": "female",
                                "source_id": 22694,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent"
                            },
                            "content_type": "audio/mpeg"
                        },
                    ],
                    "sentences": [
                        {
                            "en": "We'd prefer a house on a quiet street.",
                            "ja": "静かな通りにある家の方がいいです。"
                        },
                        {
                            "en": "I know you have diarrhea, but could you keep it down a bit more, please?",
                            "ja": "下りなのは分かりますが、もう少し静かにしていただけますか？"
                        },
                        {
                            "en": "When Koichi and Viet got in, the taxi quietly started to move.",
                            "ja": "コウイチとビエトが乗り込むと、そのタクシーは静かに動き出した。"
                        },
                    ],
                },
            },
        },
    ],
}


NARU: FullTestDict = {
    "id": "NARU",
    "input": ['なる'],
    "japanesepod": {
        "expected_sections": {
            "なる": {
                "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJなる"),
                "html": get_file_as_string("naru", "japanesepod"),
            },
        },
        "expected_output": {
            "なる": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
        },
    },
    "jisho": {
        "expected_sections": {
            'なる': {
                "url": URL(f"https://jisho.org/api/v1/search/words?keyword=なる"),
                "api_response": jisho_api_responses.NARU["なる"],
                "filtered_items": jisho_api_responses.NARU_FILTERED_ITEMS["なる"],
                "extra_items": jisho_api_responses.NARU_EXTRA_ITEMS["なる"],
            },
        },
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.NARU_FILTERED_ITEMS["なる"],
                    "extra": jisho_api_responses.NARU_EXTRA_ITEMS["なる"],
                },
            },
        },
    },
    "ojad": {
        "htmls": get_ojad_html_files("naru"),
        "url": URL("http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:なる/page:%s"),
        "expected_sections": [
            {
                'na_adj': False,
                'writing_section': Soup("""<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch('word','499','female');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch('word','499','male');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">鳴る・鳴ります</p></div></td>""", "html.parser"),
                'writings': ["鳴る", "鳴ります"],
                'reading_sections': [Soup("""<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class="mola_-2"><span class="inner"><span class="char">な</span></span></span><span class=" accent_plain mola_-1"><span class="inner"><span class="char">る</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="499_1_1_female" href="#" onclick="pronounce_play('499_1_1_female');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="499_1_1_male" href="#" onclick="pronounce_play('499_1_1_male');return false;"></a></div></div>""", "html.parser")],
                'readings': ["なる"],
            },
            {
                'na_adj': False,
                'writing_section': Soup("""<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch('word','497','female');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch('word','497','male');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">なる・なります</p></div></td>""", "html.parser"),
                'writings': ["なる", "なります"],
                'reading_sections': [Soup("""<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class=" accent_top mola_-2"><span class="inner"><span class="char">な</span></span></span><span class="mola_-1"><span class="inner"><span class="char">る</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="497_1_1_female" href="#" onclick="pronounce_play('497_1_1_female');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="497_1_1_male" href="#" onclick="pronounce_play('497_1_1_male');return false;"></a></div></div>""", "html.parser")],
                'readings': ["な' る"],
            },
            {
                'na_adj': False,
                'writing_section': Soup("""<td class="midashi"><div class="proc_batch_button_word"><a class="katsuyo_proc_batch_word_female_button" href="#" onclick="pronounce_play_batch('word','498','female');return false;"></a><a class="katsuyo_proc_batch_word_male_button" href="#" onclick="pronounce_play_batch('word','498','male');return false;"></a></div><div class="midashi_wrapper"><p class="midashi_word">生る・生ります</p></div></td>""", "html.parser"),
                'writings': ["生る", "生ります"],
                'reading_sections': [Soup("""<div class="katsuyo_proc"><p><span class="katsuyo_accent"><span class="accented_word"><span class=" accent_top mola_-2"><span class="inner"><span class="char">な</span></span></span><span class="mola_-1"><span class="inner"><span class="char">る</span></span></span></span></span></p><div class="katsuyo_proc_button clearfix"><a class="katsuyo_proc_female_button js_proc_female_button" id="498_1_1_female" href="#" onclick="pronounce_play('498_1_1_female');return false;"></a><a class="katsuyo_proc_male_button js_proc_male_button" id="498_1_1_male" href="#" onclick="pronounce_play('498_1_1_male');return false;"></a></div></div>""", "html.parser")],
                'readings': ["な' る"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '鳴る': ["なる"],
            '鳴ります': ["なる"],
            'なる': ["な' る"],
            'なります': ["な' る"],
            '生る': ["な' る"],
            '生ります': ["な' る"],
        }),
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("な' る")],
                },
            },
        },
    },
    "suzuki": {
        "html": get_file_as_string("naru", "suzuki"),
        "formdata": build_suzuki_formdata("なるは"),
        "expected_sections": [
            {
                'writing_section': Soup("""<div class="phrasing_subscript"><span>なるは</span><span class="inner endspace"><span class="char"></span></span></div>""", "html.parser"),
                'writing': 'なる',
                'reading_section': Soup("""<div class="phrasing_text"><span class="accent_top mola_0"><span class="inner"><span class="char">な</span></span></span><span class="mola_1"><span class="inner"><span class="char">る</span></span></span><span class="mola_2"><span class="inner"><span class="char">は</span></span></span><span class="inner endspace"><span class="char"></span></span></div>""","html.parser"),
                'accent_section': Soup("""<script type="text/javascript">$(function () {set_accent_curve_phrase("#phrase_0_0",3,[1, 0, 0],1,0,0);});</script>""", "html.parser"),
                'reading': "な' る",
            },
        ],
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("な' る")],
                },
            },
        },
    },
    "wadoku": {
        "html": get_file_as_string("naru", "wadoku"),
        "url": URL("https://www.wadoku.de/search/なる"),
        "expected_sections": [
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/346531"><span class="orth" lang="ja" xml:lang="ja">鳴る</span></a></div>""", "html.parser"),
                'writings': ['鳴る'],
                'reading_sections': [Soup("""<span class="pron accent" data-accent-id="1"><span class="b">な~</span><span class="t l">る</span></span>""", "html.parser")],
                'readings': ["なる"],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/5295051"><span class="orth" lang="ja" xml:lang="ja">成る<span class="divider">；</span><span class="njok">為</span>る</span></a></div>""", "html.parser"),
                'writings': ['成る', '為る'],
                'reading_sections': [Soup("""<span class="pron accent" data-accent-id="1"><span class="t r">な~</span><span class="b">る</span></span>""", "html.parser")],
                'readings': ["な' る"],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/7948044"><span class="orth" lang="ja" xml:lang="ja"><span class="njok">生</span>る</span></a></div>""", "html.parser"),
                'writings': ['生る'],
                'reading_sections': [Soup("""<span class="pron accent" data-accent-id="1"><span class="t r">な~</span><span class="b">る</span></span>""", "html.parser")],
                'readings': ["な' る"],
            },
            {
                'writing_section': Soup("""<div class="japanese"><a href="/entry/view/10063467"><span class="orth" lang="ja" xml:lang="ja">ナル</span></a></div>""", "html.parser"),
                'writings': ['ナル'],
                'reading_sections': [Soup("""<span class="pron accent" data-accent-id="1"><span class="t r">な</span><span class="b">る</span></span>""", "html.parser")],
                'readings': ["な' る"],
            },
        ],
        "full_accent_dict" : defaultdict(list, {
            '鳴る': ["なる"],
            '成る': ["な' る"],
            '為る': ["な' る"],
            '生る': ["な' る"],
            'ナル': ["な' る"],
        }),
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
        },
    },
    "forvo": {
        "expected_sections": {
            'なる': {
                "url": URL(f"https://apifree.forvo.com/action/word-pronunciations/format/json/word/なる/language/ja/id_lang_speak/76/key/{API_KEY}"),
                "api_response": '{"attributes": {"total": 4}, "items": [{"id": 1896193, "word": "\\u306a\\u308b", "original": "\\u306a\\u308b", "addtime": "2012-12-07 03:13:14", "hits": 1740, "username": "akitomo", "sex": "m", "country": "Japan", "code": "ja", "langname": "Japanese", "pathmp3": "https://apifree.forvo.com/audio/1l3d2l283h3m2g1p213l3p3f352k291g1p3g373j2l3a1i331l392m1h232c3f3f2l1j34373b263a2q2a2p2i3j353m22382q2q1h3q243d3j3l2l3o1j1g3p1o3l3e2m373k2l381g3k1f2k3l2j2n3a2m332j2m2b3a312j211t1t_1j2g2q342g1m3d2a2a282q21282i1k3h361j1m1i293n1t1t", "pathogg": "https://apifree.forvo.com/audio/1i2i2m2p3o3g3f2e1o3o3o3i2c2e392a3o3b2k37342e1b3i243c1f2g2l3o1i211m3f211m223p3a352h2f321m2c393d3c3j2h3d392m27331j3l3h2f1j3q3m361m1m1m1f3j2a25343d291h2b2i2k2k1j282p3d3i3q2p211t1t_1l382c3l3n3e2g3237392i3a3d2a261b25242j2l2k371t1t", "rate": 0, "num_votes": 0, "num_positive_votes": 0}, {"id": 3772185, "word": "\\u306a\\u308b", "original": "\\u306a\\u308b", "addtime": "2015-07-31 08:04:19", "hits": 1704, "username": "skent", "sex": "m", "country": "Japan", "code": "ja", "langname": "Japanese", "pathmp3": "https://apifree.forvo.com/audio/33222p382c2432363a313e2o3739383f3i2g3p1f1o1j1i1n1n3k271p1h1i312b2d2f1l333n1j3d231p393j2836333f343e212c2j232a351o243j223b3g22392b292c392l2i3121343j36352n2h3l1j1f3m3b311j2e371t1t_2j3332281b353a2h3d1m3b3d253f2j3m1g27352i3g371t1t", "pathogg": "https://apifree.forvo.com/audio/2a2f3p3j3p1k3e3k382d3i1i2k3g2i292e323p2i3f2q1o3p3h1o1k2i371g222f2i3i321p3i2q2m2b3n2f331h342d2b3h342m29253i2e1g1p393j2h3h212b253q1n2a2a27272j34362b3q2p3a2q1l1n3e2m221l3n3a3n1t1t_3j3p251k24243f3d282o313o2h362b2e1j263i1n2o2h1t1t", "rate": 0, "num_votes": 0, "num_positive_votes": 0}, {"id": 3784428, "word": "\\u306a\\u308b", "original": "\\u306a\\u308b", "addtime": "2015-08-07 00:08:30", "hits": 3037, "username": "strawberrybrown", "sex": "f", "country": "Japan", "code": "ja", "langname": "Japanese", "pathmp3": "https://apifree.forvo.com/audio/2i3d263j1m3d3f36243l212a3p2g2c3l2c1l2l2o2c3k383m3m3f1o1o2p1l1g33283f252j2d2n2h3d2e2539322k1g3a3d3o2i383j1f1p2o2f323j371g1g1o342k2m3c2l393l2a323e1m361o2f3l1g392m2i3b1g3f3h371t1t_3d2o383g2f3p1m39333q2j1k3f2q332f351k2j2a3p371t1t", "pathogg": "https://apifree.forvo.com/audio/3f353n3g2b3227273o221j2m3e313o1p241j2o2j2e2a1f3h1k273g383l3h1l1h2k3c3f223n3b283h3l3q262c1o243c353i2n3a3d342n3j21341b2h37382b2c2c34383i351g1b2o371h2m2k1f1h3k34273n2m3g29263n1t1t_1g2a312q223l2a1j3q2e2l1p3g3236271o1j322j2q2h1t1t", "rate": 1, "num_votes": 1, "num_positive_votes": 1}, {"id": 5260109, "word": "\\u306a\\u308b", "original": "\\u306a\\u308b", "addtime": "2017-10-10 14:24:18", "hits": 190, "username": "poyotan", "sex": "f", "country": "Japan", "code": "ja", "langname": "Japanese", "pathmp3": "https://apifree.forvo.com/audio/343l2h2g3j1l1b3e2q35233f2b3j2p322n1l2m272h292q2k3b2c1o3p3a272n2m352n1g2q3p21342i392e253p2p3q3m2i1p1o1l333n2h2h3m3e3321291o3b243q1l1o252g2e1h3b282d292229341n2h3j3o2k312l2o371t1t_2o3a392g1p1l1k2o3a3d2c3e1m3l1m3q2d3b3n33293n1t1t", "pathogg": "https://apifree.forvo.com/audio/1h253b1o313a262a3i281m352a212k1n1k2h281k2h3m212l2q3f3f2b212a3a27233h1i253q1n3b211g1f1i2h3o2p3g25271k213h2d372q293n1k2j2e25383f3k1g1b313k2h2d1m2c1k3f3c2a393n29253j3i1m323o211t1t_3e2q1i1j35333n381j1o2l1p2q1f383e2b3c2b3m2p3n1t1t", "rate": 0, "num_votes": 0, "num_positive_votes": 0}]}',
                "total_items": 4,
            },
        },
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/1l3d2l283h3m2g1p213l3p3f352k291g1p3g373j2l3a1i331l392m1h232c3f3f2l1j34373b263a2q2a2p2i3j353m22382q2q1h3q243d3j3l2l3o1j1g3p1o3l3e2m373k2l381g3k1f2k3l2j2n3a2m332j2m2b3a312j211t1t_1j2g2q342g1m3d2a2a282q21282i1k3h361j1m1i293n1t1t"),
                            "username": "akitomo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/33222p382c2432363a313e2o3739383f3i2g3p1f1o1j1i1n1n3k271p1h1i312b2d2f1l333n1j3d231p393j2836333f343e212c2j232a351o243j223b3g22392b292c392l2i3121343j36352n2h3l1j1f3m3b311j2e371t1t_2j3332281b353a2h3d1m3b3d253f2j3m1g27352i3g371t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2i3d263j1m3d3f36243l212a3p2g2c3l2c1l2l2o2c3k383m3m3f1o1o2p1l1g33283f252j2d2n2h3d2e2539322k1g3a3d3o2i383j1f1p2o2f323j371g1g1o342k2m3c2l393l2a323e1m361o2f3l1g392m2i3b1g3f3h371t1t_3d2o383g2f3p1m39333q2j1k3f2q332f351k2j2a3p371t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/343l2h2g3j1l1b3e2q35233f2b3j2p322n1l2m272h292q2k3b2c1o3p3a272n2m352n1g2q3p21342i392e253p2p3q3m2i1p1o1l333n2h2h3m3e3321291o3b243q1l1o252g2e1h3b282d292229341n2h3j3o2k312l2o371t1t_2o3a392g1p1l1k2o3a3d2c3e1m3l1m3q2d3b3n33293n1t1t"),
                            "username": "poyotan",
                        },
                    ],
                },
            },
        },
    },
    "tangorin": {
        "expected_sections": {
            'なる': {
                "url": URL("https://tangorin.com/sentences?search=なる",),
                "html": get_file_as_string("naru", "tangorin"),
            },
        },
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "のろまにはなりたくない。かっこ良くなりたい！！",
                            "en": "I don't want to be lame; I want to be cool!!",
                        },
                        {
                            "ja": "大きくなったら王様になりたい。",
                            "en": "When I grow up, I want to be a king.",
                        },
                        {
                            "ja": "これは代わりになるものをみつけたい単語だ。",
                            "en": "It's a word I'd like to find a substitute for.",
                        },
                        {
                            "ja": "それをするためには危険を冒さなければならない。",
                            "en": "In order to do that, you have to take risks.",
                        },
                        {
                            "ja": "私は寝なければなりません。",
                            "en": "I have to go to bed.",
                        },
                        {
                            "ja": "こんなことにはなって欲しくなかった。",
                            "en": "I didn't want this to happen.",
                        },
                        {
                            "ja": "ロボットなんかに私がなるわけないでしょう？ロボットは夢を見ないんだから。",
                            "en": "How could I be a robot? Robots don't dream.",
                        },
                        {
                            "ja": "私達がしなければならないことそれぞれの背後には自分たちがしたい何かがあると思うんだ。",
                            "en": "I suppose that behind each thing we have to do, there's something we want to do...",
                        },
                        {
                            "ja": "私たちは兄弟として共に生きることを知らなければならない。さもなくば、愚か者として共に滅びるであろう。",
                            "en": "We must learn to live together as brothers, or we will perish together as fools.",
                        },
                        {
                            "ja": "はぁ・・・（汗）、それでコンタクトは取れるようになったのかしら・・・？",
                            "en": "Uh... How's that working?",
                        },
                    ],
                },
            },
        },
    },
    "wanikani": {
        "url": URL("https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs=なる"),
        "api_response": wanikani_api_responses.NARU,
        "result_dict": {},
        "expected_output": {
            'なる': {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
            },
        },
    },
    "expected_result": [
        {
            "word": "なる",
            "japanesepod": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                },
            },
            "jisho": {
                "success": True,
                "error": None,
                "main_data": {
                    "results": jisho_api_responses.NARU_FILTERED_ITEMS["なる"],
                    "extra": jisho_api_responses.NARU_EXTRA_ITEMS["なる"],
                },
            },
            "ojad": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("な' る")],
                },
            },
            "suzuki": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [Yomi("な' る")],
                },
            },
            "wadoku": {
                "success": True,
                "error": None,
                "main_data": {
                    "accent": [],
                },
            },
            "forvo": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [
                        {
                            "url": URL("https://apifree.forvo.com/audio/1l3d2l283h3m2g1p213l3p3f352k291g1p3g373j2l3a1i331l392m1h232c3f3f2l1j34373b263a2q2a2p2i3j353m22382q2q1h3q243d3j3l2l3o1j1g3p1o3l3e2m373k2l381g3k1f2k3l2j2n3a2m332j2m2b3a312j211t1t_1j2g2q342g1m3d2a2a282q21282i1k3h361j1m1i293n1t1t"),
                            "username": "akitomo",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/33222p382c2432363a313e2o3739383f3i2g3p1f1o1j1i1n1n3k271p1h1i312b2d2f1l333n1j3d231p393j2836333f343e212c2j232a351o243j223b3g22392b292c392l2i3121343j36352n2h3l1j1f3m3b311j2e371t1t_2j3332281b353a2h3d1m3b3d253f2j3m1g27352i3g371t1t"),
                            "username": "skent",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/2i3d263j1m3d3f36243l212a3p2g2c3l2c1l2l2o2c3k383m3m3f1o1o2p1l1g33283f252j2d2n2h3d2e2539322k1g3a3d3o2i383j1f1p2o2f323j371g1g1o342k2m3c2l393l2a323e1m361o2f3l1g392m2i3b1g3f3h371t1t_3d2o383g2f3p1m39333q2j1k3f2q332f351k2j2a3p371t1t"),
                            "username": "strawberrybrown",
                        },
                        {
                            "url": URL("https://apifree.forvo.com/audio/343l2h2g3j1l1b3e2q35233f2b3j2p322n1l2m272h292q2k3b2c1o3p3a272n2m352n1g2q3p21342i392e253p2p3q3m2i1p1o1l333n2h2h3m3e3321291o3b243q1l1o252g2e1h3b282d292229341n2h3j3o2k312l2o371t1t_2o3a392g1p1l1k2o3a3d2c3e1m3l1m3q2d3b3n33293n1t1t"),
                            "username": "poyotan",
                        },
                    ],
                },
            },
            "tangorin": {
                "success": True,
                "error": None,
                "main_data": {
                    "sentences": [
                        {
                            "ja": "のろまにはなりたくない。かっこ良くなりたい！！",
                            "en": "I don't want to be lame; I want to be cool!!",
                        },
                        {
                            "ja": "大きくなったら王様になりたい。",
                            "en": "When I grow up, I want to be a king.",
                        },
                        {
                            "ja": "これは代わりになるものをみつけたい単語だ。",
                            "en": "It's a word I'd like to find a substitute for.",
                        },
                        {
                            "ja": "それをするためには危険を冒さなければならない。",
                            "en": "In order to do that, you have to take risks.",
                        },
                        {
                            "ja": "私は寝なければなりません。",
                            "en": "I have to go to bed.",
                        },
                        {
                            "ja": "こんなことにはなって欲しくなかった。",
                            "en": "I didn't want this to happen.",
                        },
                        {
                            "ja": "ロボットなんかに私がなるわけないでしょう？ロボットは夢を見ないんだから。",
                            "en": "How could I be a robot? Robots don't dream.",
                        },
                        {
                            "ja": "私達がしなければならないことそれぞれの背後には自分たちがしたい何かがあると思うんだ。",
                            "en": "I suppose that behind each thing we have to do, there's something we want to do...",
                        },
                        {
                            "ja": "私たちは兄弟として共に生きることを知らなければならない。さもなくば、愚か者として共に滅びるであろう。",
                            "en": "We must learn to live together as brothers, or we will perish together as fools.",
                        },
                        {
                            "ja": "はぁ・・・（汗）、それでコンタクトは取れるようになったのかしら・・・？",
                            "en": "Uh... How's that working?",
                        },
                    ],
                },
            },
            "wanikani": {
                "success": True,
                "error": None,
                "main_data": {
                    "audio": [],
                    "sentences": [],
                },
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
    NARU,
]


# TEMPLATE: FullTestDict = {
#     "id": "",
#     "input": [''],
#     "forvo": {
#         "expected_sections": [
#             {
#                 "url": "https://apifree.forvo.com/action/word-pronunciations/format/json/word//language/ja/id_lang_speak/76/key/{API_KEY}",
#                 "api_response": '{"attributes": 0, "items": []}',
#                 "total_items":  "items,
#             },
#         ],
#         "expected_output": {
#             '': [],
#         },
#     },
#     "jisho": {
#                 "success": True,
#                 "error": None,
#                 "main_data": {
#                 },
#             },
#     "ojad": {
#         "htmls": get_ojad_html_files(""),
#         "url": "http://www.gavo.t.u-tokyo.ac.jp/ojad/search/index/limit:100/word:/page:%s",
#         "expected_sections": [
#             {
#                 'na_adj': False,
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
#             "ojad": [],
#             "suzuki": {
#                 "success": True,
#                 "error": None,
#                 "main_data": {
#                     "accent": [Yomi(],
#             "wadoku": [],
#             "forvo": {
#                 "success": True,
#                 "error": None,
#                 "main_data": {
#                     "audio": [],
#                 },
#             },
#             "wanikani": [],
#         },
#     ],
# }
