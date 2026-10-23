"""Expected JDict (WWWJDIC) results for every word used in the test dicts"""

from api.custom_types.alternative_string_types import URL, HTMLString
from api.custom_types.response_types import JDictEntry, ResponseItemJDict
from testing.dict_typing import JDictExpectedSection, JDictTestDict


def get_file_as_string(filename: str) -> HTMLString:
    with open(f"testing/html_files/jdict_{filename}.html", encoding="utf8") as f:
        return HTMLString(f.read())


ENTRIES: dict[str, list[JDictEntry]] = {
    "眼鏡": [
        {
            "writings": ["眼鏡"],
            "readings": ["めがね", "がんきょう", "メガネ"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": ["uk"],
                    "definitions": ["glasses", "eyeglasses", "spectacles"],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": ["めがね, メガネ only", "uk"],
                    "definitions": [
                        "judgment",
                        "judgement",
                        "discrimination",
                        "discernment",
                        "insight",
                    ],
                },
            ],
        },
        {
            "writings": ["眼鏡カイマン"],
            "readings": ["めがねカイマン", "メガネカイマン"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": ["uk"],
                    "definitions": ["spectacled caiman (Caiman sclerops)"],
                }
            ],
        },
        {
            "writings": ["眼鏡にかなう", "眼鏡に適う", "眼鏡に叶う"],
            "readings": ["めがねにかなう"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["exp", "v5u"],
                    "tags": [],
                    "definitions": [
                        "to win the favour of (favor)",
                        "to be acknowledged (e.g. by a superior)",
                        "to measure up to",
                    ],
                }
            ],
        },
    ],
    "カムバック": [
        {
            "writings": [],
            "readings": ["カムバック"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n", "vs", "vi"],
                    "tags": [],
                    "definitions": ["comeback"],
                }
            ],
        }
    ],
    "食べる": [
        {
            "writings": ["食べる", "喰べる"],
            "readings": ["たべる"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["v1", "vt"],
                    "tags": [],
                    "definitions": ["to eat"],
                },
                {
                    "parts_of_speech": ["v1", "vt"],
                    "tags": [],
                    "definitions": [
                        "to live on (e.g. a salary)",
                        "to live off",
                        "to subsist on",
                    ],
                },
            ],
        },
        {
            "writings": ["食べるラー油", "食べる辣油"],
            "readings": ["たべるラーゆ"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["exp", "n"],
                    "tags": [],
                    "definitions": [
                        "{food} (See 辣油) chili oil mixed with chopped garlic, "
                        "onions, etc."
                    ],
                }
            ],
        },
    ],
    "学生": [
        {
            "writings": ["学生"],
            "readings": ["がくしょう", "がくそう"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": ["arch"],
                    "definitions": [
                        "Heian-period student of government administration"
                    ],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": ["arch"],
                    "definitions": [
                        "Buddhist scholar",
                        "researcher at a Buddhist temple",
                        "person studying Buddhism",
                    ],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": ["arch"],
                    "definitions": ["learning", "scholarship"],
                },
            ],
        },
        {
            "writings": ["学生"],
            "readings": ["がくせい"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["student (esp. a university student)"],
                }
            ],
        },
        {
            "writings": ["学生ローン"],
            "readings": ["がくせいローン"],
            "is_common": False,
            "senses": [
                {"parts_of_speech": ["n"], "tags": [], "definitions": ["student loan"]}
            ],
        },
        {
            "writings": ["学生運動"],
            "readings": ["がくせいうんどう"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["student movement"],
                }
            ],
        },
    ],
    "言葉": [
        {
            "writings": ["言葉", "詞", "辞"],
            "readings": ["ことば", "けとば"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": ["See 言語"],
                    "definitions": ["language", "dialect"],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["word", "phrase", "expression", "term"],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": [
                        "speech",
                        "(manner of) speaking",
                        "(use of) language",
                    ],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["words", "remark", "statement", "comment"],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["learning to speak", "language acquisition"],
                },
            ],
        },
        {
            "writings": ["言葉遊び", "ことば遊び", "言葉あそび"],
            "readings": ["ことばあそび"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["word game", "wordplay", "playing with words"],
                }
            ],
        },
        {
            "writings": [
                "言葉が見つからない",
                "言葉がみつからない",
                "言葉が見付からない",
            ],
            "readings": ["ことばがみつからない"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["exp", "adj-i"],
                    "tags": [],
                    "definitions": ["at a loss for words", "stumped for words"],
                }
            ],
        },
        {
            "writings": ["言葉が過ぎる"],
            "readings": ["ことばがすぎる"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["exp", "v1"],
                    "tags": [],
                    "definitions": ["to say too much", "to go too far"],
                }
            ],
        },
    ],
    "BADINPUT": [
        {
            "writings": [],
            "readings": ["ボディー", "ボディ", "ボデー"],
            "is_common": True,
            "senses": [
                {"parts_of_speech": ["n"], "tags": [], "definitions": ["body"]},
                {
                    "parts_of_speech": ["n"],
                    "tags": ["abbr"],
                    "definitions": [
                        "{sports} (See ボディーブロー) body blow (in boxing)"
                    ],
                },
            ],
        },
        {
            "writings": [],
            "readings": ["バディ", "バディー"],
            "is_common": False,
            "senses": [
                {"parts_of_speech": ["n"], "tags": [], "definitions": ["buddy"]}
            ],
        },
    ],
    "兎": [
        {
            "writings": ["兎", "兔", "菟"],
            "readings": ["うさぎ", "う", "ウサギ"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": ["uk"],
                    "definitions": [
                        "rabbit",
                        "hare",
                        "coney",
                        "cony",
                        "lagomorph (esp. leporids)",
                    ],
                }
            ],
        },
        {
            "writings": ["兎にも角にも"],
            "readings": ["とにもかくにも"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["adv"],
                    "tags": ["uk"],
                    "definitions": [
                        "anyhow",
                        "anyway",
                        "somehow or other",
                        "generally speaking",
                        "in any case",
                    ],
                }
            ],
        },
        {
            "writings": ["兎に角"],
            "readings": ["とにかく"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["adv"],
                    "tags": ["uk"],
                    "definitions": [
                        "anyhow",
                        "at any rate",
                        "anyway",
                        "somehow or other",
                        "generally speaking",
                        "in any case",
                        "at least",
                    ],
                }
            ],
        },
        {
            "writings": ["兎の毛"],
            "readings": ["うのけ"],
            "is_common": False,
            "senses": [
                {"parts_of_speech": ["n"], "tags": [], "definitions": ["just a hair"]}
            ],
        },
    ],
    "行く": [
        {
            "writings": ["行く", "逝く", "往く"],
            "readings": ["いく", "ゆく"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": ["See 来る・くる・1"],
                    "definitions": [
                        "to go",
                        "to move (in a direction or towards a specific location)",
                        "to head (towards)",
                        "to be transported (towards)",
                        "to reach",
                    ],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": [],
                    "definitions": [
                        "(い sometimes omitted in auxiliary use) (See 旨く行く) to "
                        "proceed",
                        "to take place",
                    ],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": [],
                    "definitions": ["to pass through", "to come and go"],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": [],
                    "definitions": ["to walk"],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": ["逝く only"],
                    "definitions": ["to die", "to pass away"],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": [],
                    "definitions": ["to do (in a specific way)"],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": [],
                    "definitions": ["to stream", "to flow"],
                },
                {
                    "parts_of_speech": ["v5k-s", "aux-v"],
                    "tags": ["uk", "after the -te form of a verb"],
                    "definitions": ["to continue"],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": ["uk"],
                    "definitions": ["to have an orgasm", "to come", "to cum"],
                },
                {
                    "parts_of_speech": ["v5k-s", "vi"],
                    "tags": ["uk", "sl"],
                    "definitions": [
                        "to trip",
                        "to get high",
                        "to have a drug-induced hallucination",
                    ],
                },
            ],
        },
        {
            "writings": ["行くあて", "行く当て"],
            "readings": ["いくあて"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["somewhere to go", "place to go"],
                }
            ],
        },
        {
            "writings": ["行方", "行くえ", "行衛"],
            "readings": ["ゆくえ"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["(one's) whereabouts"],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["destination", "where one is headed"],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": [
                        "outcome",
                        "course (of events)",
                        "development",
                        "direction",
                        "tide",
                    ],
                },
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["future", "journey ahead"],
                },
            ],
        },
        {
            "writings": ["行く手"],
            "readings": ["ゆくて"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["one's way", "one's path"],
                }
            ],
        },
    ],
    "籠": [
        {
            "writings": ["籠", "篭"],
            "readings": ["かご", "カゴ"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": ["uk"],
                    "definitions": ["basket (shopping, etc.)", "hamper", "cage"],
                }
            ],
        },
        {
            "writings": ["牢", "籠", "篭"],
            "readings": ["ろう"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["prison", "jail", "gaol"],
                },
                {
                    "parts_of_speech": ["adj-t"],
                    "tags": ["obs", "See 牢として"],
                    "definitions": ["firm", "solid", "strong"],
                },
            ],
        },
        {
            "writings": ["籠で水を汲む"],
            "readings": ["かごでみずをくむ"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["exp", "v5m"],
                    "tags": ["id"],
                    "definitions": [
                        "to bail out the ocean with a teaspoon",
                        "to scoop water with a basket",
                    ],
                }
            ],
        },
        {
            "writings": ["籠の垂れ"],
            "readings": ["かごのたれ"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n"],
                    "tags": [],
                    "definitions": ["hanging of a palanquin"],
                }
            ],
        },
    ],
    "静か": [
        {
            "writings": ["静か", "閑か"],
            "readings": ["しずか"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["adj-na"],
                    "tags": [],
                    "definitions": ["quiet", "silent"],
                },
                {
                    "parts_of_speech": ["adj-na"],
                    "tags": [],
                    "definitions": ["slow", "unhurried"],
                },
                {
                    "parts_of_speech": ["adj-na"],
                    "tags": [],
                    "definitions": ["calm", "peaceful"],
                },
            ],
        },
        {
            "writings": ["静かに"],
            "readings": ["しずかに"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["adv"],
                    "tags": [],
                    "definitions": ["calmly", "quietly", "gently", "peacefully"],
                },
                {"parts_of_speech": ["exp"], "tags": [], "definitions": ["be quiet!"]},
            ],
        },
        {
            "writings": ["静かに流れる川は深い"],
            "readings": ["しずかにながれるかわはふかい"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["exp"],
                    "tags": ["proverb"],
                    "definitions": ["still waters run deep"],
                }
            ],
        },
    ],
    "なる": [
        {
            "writings": ["成る", "為る"],
            "readings": ["なる"],
            "is_common": True,
            "senses": [
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to become",
                        "to get",
                        "to grow",
                        "to turn",
                        "to reach",
                        "to attain",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to result in",
                        "to turn out",
                        "to end up",
                        "to prove (to be)",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk", "as ...からなる or ...よりなる"],
                    "definitions": [
                        "to consist of",
                        "to be composed of",
                        "to be made up of",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to be completed",
                        "to be realized",
                        "to succeed",
                        "to be attained",
                        "to be accomplished",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to change (into)",
                        "to turn (into)",
                        "to transform",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to come (to do)",
                        "to begin (to do)",
                        "to grow (to do)",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to come to",
                        "to amount to",
                        "to add up to",
                        "to make",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": ["to play (the part of)", "to act as"],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": [
                        "to be used for",
                        "to be useful for",
                        "to serve as",
                    ],
                },
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": [],
                    "definitions": ["{shogi} to be promoted"],
                },
                {
                    "parts_of_speech": ["aux-v", "v5r"],
                    "tags": [
                        "hon",
                        "uk",
                        "as お + masu stem + になる, or ご + noun + になる",
                    ],
                    "definitions": ["to do ..."],
                },
            ],
        },
        {
            "writings": ["生る"],
            "readings": ["なる"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["v5r", "vi"],
                    "tags": ["uk"],
                    "definitions": ["to bear fruit"],
                }
            ],
        },
        {
            "writings": [],
            "readings": ["ナル"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["n", "adj-na"],
                    "tags": ["abbr", "sl", "See ナルシシスト"],
                    "definitions": ["narcissistic"],
                }
            ],
        },
        {
            "writings": [],
            "readings": ["なる"],
            "is_common": False,
            "senses": [
                {
                    "parts_of_speech": ["suf", "adj-f"],
                    "tags": ["arch", "See 也・なり・2"],
                    "definitions": ["that is in"],
                },
                {
                    "parts_of_speech": ["suf", "adj-f"],
                    "tags": [],
                    "definitions": ["who is called", "that is called"],
                },
                {
                    "parts_of_speech": ["suf", "adj-f"],
                    "tags": [],
                    "definitions": ["that is"],
                },
                {
                    "parts_of_speech": ["int"],
                    "tags": ["sl", "abbr", "See なるほど"],
                    "definitions": ["I see"],
                },
            ],
        },
    ],
}


SECTIONS: dict[str, JDictExpectedSection] = {
    "眼鏡": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ眼鏡"),
        "html": get_file_as_string("megane"),
        "expected_rows": [
            "眼鏡 [めがね(P);がんきょう;メガネ(P)] /(n) (1) (uk) glasses/eyeglasses/spectacles/(n) (2) (めがね, "
            "メガネ only) (uk) judgment/judgement/discrimination/discernment/insight/(P)/",
            "眼鏡カイマン [めがねカイマン;メガネカイマン] /(n) (uk) spectacled caiman (Caiman sclerops)/",
            "眼鏡にかなう;眼鏡に適う;眼鏡に叶う [めがねにかなう] /(exp,v5u) to win the favour of (favor)/to be "
            "acknowledged (e.g. by a superior)/to measure up to/",
        ],
        "expected_entries": ENTRIES["眼鏡"],
    },
    "カムバック": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJカムバック"),
        "html": get_file_as_string("comeback"),
        "expected_rows": ["カムバック /(n,vs,vi) comeback/(P)/"],
        "expected_entries": ENTRIES["カムバック"],
    },
    "食べる": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ食べる"),
        "html": get_file_as_string("taberu"),
        "expected_rows": [
            "食べる(P);喰べる(iK) [たべる] /(v1,vt) (1) to eat/(v1,vt) (2) to live on (e.g. a salary)/to "
            "live off/to subsist on/(P)/",
            "食べるラー油;食べる辣油 [たべるラーゆ] /(exp,n) {food} (See 辣油) chili oil mixed with chopped garlic, "
            "onions, etc./",
        ],
        "expected_entries": ENTRIES["食べる"],
    },
    "学生": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ学生"),
        "html": get_file_as_string("gakusei"),
        "expected_rows": [
            "学生 [がくしょう;がくそう] /(n) (1) (arch) Heian-period student of government "
            "administration/(n) (2) (arch) Buddhist scholar/researcher at a Buddhist "
            "temple/person studying Buddhism/(n) (3) (arch) learning/scholarship/",
            "学生 [がくせい] /(n) student (esp. a university student)/(P)/",
            "学生ローン [がくせいローン] /(n) student loan/",
            "学生運動 [がくせいうんどう] /(n) student movement/",
        ],
        "expected_entries": ENTRIES["学生"],
    },
    "言葉": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ言葉"),
        "html": get_file_as_string("kotoba"),
        "expected_rows": [
            "言葉(P);詞;辞 [ことば(P);けとば(言葉)(ok)] /(n) (1) (See 言語) language/dialect/(n) (2) "
            "word/phrase/expression/term/(n) (3) speech/(manner of) speaking/(use of) "
            "language/(n) (4) words/remark/statement/comment/(n) (5) learning to speak/language "
            "acquisition/(P)/",
            "言葉遊び;ことば遊び;言葉あそび [ことばあそび] /(n) word game/wordplay/playing with words/",
            "言葉が見つからない;言葉がみつからない;言葉が見付からない [ことばがみつからない] /(exp,adj-i) at a loss for words/stumped "
            "for words/",
            "言葉が過ぎる [ことばがすぎる] /(exp,v1) to say too much/to go too far/",
        ],
        "expected_entries": ENTRIES["言葉"],
    },
    "BADINPUT": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJBADINPUT"),
        "html": get_file_as_string("badinput"),
        "expected_rows": [
            "ボディー(P);ボディ(P);ボデー /(n) (1) body/(n) (2) (abbr) {sports} (See ボディーブロー) body blow (in "
            "boxing)/(P)/",
            "バディ;バディー /(n) buddy/",
        ],
        "expected_entries": ENTRIES["BADINPUT"],
    },
    "兎": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ兎"),
        "html": get_file_as_string("usagi"),
        "expected_rows": [
            "兎(P);兔;菟(iK) [うさぎ(P);う(兎)(ok);ウサギ] /(n) (uk) rabbit/hare/coney/cony/lagomorph (esp. "
            "leporids)/(P)/",
            "兎にも角にも [とにもかくにも] /(adv) (uk) anyhow/anyway/somehow or other/generally speaking/in "
            "any case/",
            "兎に角(ateji) [とにかく] /(adv) (uk) anyhow/at any rate/anyway/somehow or other/generally "
            "speaking/in any case/at least/(P)/",
            "兎の毛 [うのけ] /(n) just a hair/",
        ],
        "expected_entries": ENTRIES["兎"],
    },
    "行く": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ行く"),
        "html": get_file_as_string("iku"),
        "expected_rows": [
            "行く(P);逝く;往く(oK) [いく(P);ゆく(P)] /(v5k-s,vi) (1) (See 来る・くる・1) to go/to move (in a "
            "direction or towards a specific location)/to head (towards)/to be transported "
            "(towards)/to reach/(v5k-s,vi) (2) (い sometimes omitted in auxiliary use) (See 旨く行く) "
            "to proceed/to take place/(v5k-s,vi) (3) to pass through/to come and go/(v5k-s,vi) "
            "(4) to walk/(v5k-s,vi) (5) (逝く only) to die/to pass away/(v5k-s,vi) (6) to do (in a "
            "specific way)/(v5k-s,vi) (7) to stream/to flow/(v5k-s,aux-v) (8) (uk) (after the -te "
            "form of a verb) to continue/(v5k-s,vi) (9) (uk) to have an orgasm/to come/to "
            "cum/(v5k-s,vi) (10) (uk) (sl) to trip/to get high/to have a drug-induced "
            "hallucination/(P)/",
            "行くあて;行く当て [いくあて] /(n) somewhere to go/place to go/",
            "行方(P);行くえ;行衛(ateji) [ゆくえ] /(n) (1) (one's) whereabouts/(n) (2) destination/where one "
            "is headed/(n) (3) outcome/course (of events)/development/direction/tide/(n) (4) "
            "future/journey ahead/(P)/",
            "行く手 [ゆくて] /(n) one's way/one's path/",
        ],
        "expected_entries": ENTRIES["行く"],
    },
    "籠": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ籠"),
        "html": get_file_as_string("kago"),
        "expected_rows": [
            "籠(P);篭(P) [かご(P);カゴ(P)] /(n) (uk) basket (shopping, etc.)/hamper/cage/(P)/",
            "牢;籠;篭 [ろう] /(n) (1) prison/jail/gaol/(adj-t) (2) (obs) (See 牢として) firm/solid/strong/",
            "籠で水を汲む [かごでみずをくむ] /(exp,v5m) (id) to bail out the ocean with a teaspoon/to scoop "
            "water with a basket/",
            "籠の垂れ [かごのたれ] /(n) hanging of a palanquin/",
        ],
        "expected_entries": ENTRIES["籠"],
    },
    "静か": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ静か"),
        "html": get_file_as_string("shizuka"),
        "expected_rows": [
            "静か(P);閑か [しずか] /(adj-na) (1) quiet/silent/(adj-na) (2) slow/unhurried/(adj-na) (3) "
            "calm/peaceful/(P)/",
            "静かに [しずかに] /(adv) (1) calmly/quietly/gently/peacefully/(exp) (2) be quiet!/",
            "静かに流れる川は深い [しずかにながれるかわはふかい] /(exp) (proverb) still waters run deep/",
        ],
        "expected_entries": ENTRIES["静か"],
    },
    "なる": {
        "url": URL("https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJなる"),
        "html": get_file_as_string("naru"),
        "expected_rows": [
            "成る(P);為る [なる] /(v5r,vi) (1) (uk) to become/to get/to grow/to turn/to reach/to "
            "attain/(v5r,vi) (2) (uk) to result in/to turn out/to end up/to prove (to "
            "be)/(v5r,vi) (3) (uk) (as ...からなる or ...よりなる) to consist of/to be composed of/to be "
            "made up of/(v5r,vi) (4) (uk) to be completed/to be realized/to succeed/to be "
            "attained/to be accomplished/(v5r,vi) (5) (uk) to change (into)/to turn (into)/to "
            "transform/(v5r,vi) (6) (uk) to come (to do)/to begin (to do)/to grow (to "
            "do)/(v5r,vi) (7) (uk) to come to/to amount to/to add up to/to make/(v5r,vi) (8) (uk) "
            "to play (the part of)/to act as/(v5r,vi) (9) (uk) to be used for/to be useful for/to "
            "serve as/(v5r,vi) (10) {shogi} to be promoted/(aux-v,v5r) (11) (hon) (uk) (as お + "
            "masu stem + になる, or ご + noun + になる) to do .../(P)/",
            "生る [なる] /(v5r,vi) (uk) to bear fruit/(P)/",
            "ナル /(n,adj-na) (abbr) (sl) (See ナルシシスト) narcissistic/",
            "なる /(suf,adj-f) (1) (arch) (See 也・なり・2) that is in/(suf,adj-f) (2) who is "
            "called/that is called/(suf,adj-f) (3) that is/(int) (4) (sl) (abbr) (See なるほど) I "
            "see/",
        ],
        "expected_entries": ENTRIES["なる"],
    },
}


OUTPUTS: dict[str, ResponseItemJDict] = {
    "眼鏡": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["眼鏡"][0]],
            "extra": [
                {
                    "writings": ["眼鏡カイマン"],
                    "readings": ["めがねカイマン", "メガネカイマン"],
                },
                {
                    "writings": ["眼鏡にかなう", "眼鏡に適う", "眼鏡に叶う"],
                    "readings": ["めがねにかなう"],
                },
            ],
        },
    },
    "カムバック": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["カムバック"][0]],
            "extra": [],
        },
    },
    "食べる": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["食べる"][0]],
            "extra": [
                {
                    "writings": ["食べるラー油", "食べる辣油"],
                    "readings": ["たべるラーゆ"],
                }
            ],
        },
    },
    "学生": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["学生"][0], ENTRIES["学生"][1]],
            "extra": [
                {"writings": ["学生ローン"], "readings": ["がくせいローン"]},
                {"writings": ["学生運動"], "readings": ["がくせいうんどう"]},
            ],
        },
    },
    "言葉": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["言葉"][0]],
            "extra": [
                {
                    "writings": ["言葉遊び", "ことば遊び", "言葉あそび"],
                    "readings": ["ことばあそび"],
                },
                {
                    "writings": [
                        "言葉が見つからない",
                        "言葉がみつからない",
                        "言葉が見付からない",
                    ],
                    "readings": ["ことばがみつからない"],
                },
                {"writings": ["言葉が過ぎる"], "readings": ["ことばがすぎる"]},
            ],
        },
    },
    "BADINPUT": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [],
            "extra": [
                {"writings": [], "readings": ["ボディー", "ボディ", "ボデー"]},
                {"writings": [], "readings": ["バディ", "バディー"]},
            ],
        },
    },
    "兎": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["兎"][0]],
            "extra": [
                {"writings": ["兎にも角にも"], "readings": ["とにもかくにも"]},
                {"writings": ["兎に角"], "readings": ["とにかく"]},
                {"writings": ["兎の毛"], "readings": ["うのけ"]},
            ],
        },
    },
    "行く": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["行く"][0]],
            "extra": [
                {"writings": ["行くあて", "行く当て"], "readings": ["いくあて"]},
                {"writings": ["行方", "行くえ", "行衛"], "readings": ["ゆくえ"]},
                {"writings": ["行く手"], "readings": ["ゆくて"]},
            ],
        },
    },
    "籠": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["籠"][0], ENTRIES["籠"][1]],
            "extra": [
                {"writings": ["籠で水を汲む"], "readings": ["かごでみずをくむ"]},
                {"writings": ["籠の垂れ"], "readings": ["かごのたれ"]},
            ],
        },
    },
    "静か": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["静か"][0]],
            "extra": [
                {"writings": ["静かに"], "readings": ["しずかに"]},
                {
                    "writings": ["静かに流れる川は深い"],
                    "readings": ["しずかにながれるかわはふかい"],
                },
            ],
        },
    },
    "なる": {
        "success": True,
        "error": None,
        "main_data": {
            "results": [ENTRIES["なる"][0], ENTRIES["なる"][1], ENTRIES["なる"][3]],
            "extra": [{"writings": [], "readings": ["ナル"]}],
        },
    },
}


def build_test_dict(word_list: list[str]) -> JDictTestDict:
    return JDictTestDict(
        expected_sections={word: SECTIONS[word] for word in word_list},
        expected_output={word: OUTPUTS[word] for word in word_list},
    )
