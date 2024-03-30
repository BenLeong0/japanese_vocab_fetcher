from api.custom_types.jisho_api_types import JishoAPIItem, JishoAPIResponse
from api.custom_types.response_types import JishoExtraItem


MEGANE: dict[str, JishoAPIResponse] = {
    "眼鏡": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "眼鏡",
                "is_common": True,
                "tags": ["wanikani34"],
                "jlpt": ["jlpt-n1", "jlpt-n5"],
                "japanese": [
                    {"word": "眼鏡", "reading": "めがね"},
                    {"word": "眼鏡", "reading": "がんきょう"},
                    {"reading": "メガネ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["glasses", "eyeglasses", "spectacles"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "judgment",
                            "judgement",
                            "discrimination",
                            "discernment",
                            "insight",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": ["めがね", "メガネ"],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Megane"],
                        "parts_of_speech": ["Place"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Glasses"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Glasses” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Glasses?oldid=494388060",
                            },
                            {
                                "text": "Read “眼鏡” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/眼鏡?oldid=42599911",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": True,
                    "dbpedia": "http://dbpedia.org/resource/Glasses",
                },
            },
            {
                "slug": "眼鏡橋",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "眼鏡橋", "reading": "めがねばし"}],
                "senses": [
                    {
                        "english_definitions": ["arched bridge"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Meganebashi"],
                        "parts_of_speech": ["Place"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": True, "dbpedia": False},
            },
            {
                "slug": "眼鏡を掛ける",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "メガネを掛ける", "reading": "メガネをかける"},
                    {"word": "眼鏡をかける", "reading": "めがねをかける"},
                    {"word": "眼鏡を掛ける", "reading": "めがねをかける"},
                    {"word": "めがねを掛ける", "reading": "めがねをかける"},
                ],
                "senses": [
                    {
                        "english_definitions": ["to wear glasses", "to put on glasses"],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Ichidan verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "眼鏡にかなう",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "眼鏡にかなう", "reading": "めがねにかなう"},
                    {"word": "眼鏡に適う", "reading": "めがねにかなう"},
                    {"word": "眼鏡に叶う", "reading": "めがねにかなう"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "to win the favour of (favor)",
                            "to be acknowledged (e.g. by a superior)",
                            "to measure up to",
                        ],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Godan verb with u ending",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "眼鏡猿",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "眼鏡猿", "reading": "めがねざる"},
                    {"reading": "メガネザル"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "tarsier (Tarsius syrichta)",
                            "specter lemur",
                            "spectre lemur",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Tarsier"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Tarsier” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Tarsier?oldid=493289405",
                            },
                            {
                                "text": "Read “メガネザル” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/メガネザル?oldid=42564577",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Tarsier",
                },
            },
            {
                "slug": "眼鏡黐之魚",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "眼鏡黐之魚", "reading": "めがねもちのうお"},
                    {"reading": "メガネモチノウオ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "humphead wrasse (Cheilinus undulatus)",
                            "Napoleon wrasse",
                            "Napoleonfish",
                            "Maori wrasse",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Humphead wrasse"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Humphead wrasse” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Humphead_wrasse?oldid=492695124",
                            },
                            {
                                "text": "Read “メガネモチノウオ” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/メガネモチノウオ?oldid=40496900",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Humphead_wrasse",
                },
            },
            {
                "slug": "眼鏡熊",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "眼鏡熊", "reading": "めがねぐま"},
                    {"reading": "メガネグマ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["spectacled bear (Tremarctos ornatus)"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Spectacled bear"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Spectacled bear” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Spectacled_bear?oldid=493872138",
                            },
                            {
                                "text": "Read “メガネグマ” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/メガネグマ?oldid=42463862",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Spectacled_bear",
                },
            },
            {
                "slug": "眼鏡屋",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "眼鏡屋", "reading": "めがねや"}],
                "senses": [
                    {
                        "english_definitions": ["optician"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "眼鏡っ娘",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "眼鏡っ娘", "reading": "めがねっこ"},
                    {"word": "眼鏡っ子", "reading": "めがねっこ"},
                    {"word": "めがねっ娘", "reading": "めがねっこ"},
                    {"word": "眼鏡娘", "reading": "めがねっこ"},
                    {"word": "メガネっ娘", "reading": "メガネっこ"},
                    {"word": "メガネっ子", "reading": "メガネっこ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "girl (usu. attractive) with glasses",
                            "glasses-wearing girl",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Manga slang"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "眼鏡海豚",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "眼鏡海豚", "reading": "めがねいるか"},
                    {"reading": "メガネイルカ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "spectacled porpoise (Phocoena dioptrica)"
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    },
}


MEGANE_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "眼鏡": [
        {
            "slug": "眼鏡",
            "is_common": True,
            "tags": ["wanikani34"],
            "jlpt": ["jlpt-n1", "jlpt-n5"],
            "japanese": [
                {"word": "眼鏡", "reading": "めがね"},
                {"word": "眼鏡", "reading": "がんきょう"},
                {"reading": "メガネ"},
            ],
            "senses": [
                {
                    "english_definitions": ["glasses", "eyeglasses", "spectacles"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Usually written using kana alone"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": [
                        "judgment",
                        "judgement",
                        "discrimination",
                        "discernment",
                        "insight",
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Usually written using kana alone"],
                    "restrictions": ["めがね", "メガネ"],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["Megane"],
                    "parts_of_speech": ["Place"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["Glasses"],
                    "parts_of_speech": ["Wikipedia definition"],
                    "links": [
                        {
                            "text": "Read “Glasses” on English Wikipedia",
                            "url": "http://en.wikipedia.org/wiki/Glasses?oldid=494388060",
                        },
                        {
                            "text": "Read “眼鏡” on Japanese Wikipedia",
                            "url": "http://ja.wikipedia.org/wiki/眼鏡?oldid=42599911",
                        },
                    ],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                    "sentences": [],
                },
            ],
            "attribution": {
                "jmdict": True,
                "jmnedict": True,
                "dbpedia": "http://dbpedia.org/resource/Glasses",
            },
        },
    ],
}


MEGANE_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "眼鏡": [
        {
            "slug": "眼鏡橋",
            "japanese": [{"word": "眼鏡橋", "reading": "めがねばし"}],
        },
        {
            "slug": "眼鏡を掛ける",
            "japanese": [
                {"word": "メガネを掛ける", "reading": "メガネをかける"},
                {"word": "眼鏡をかける", "reading": "めがねをかける"},
                {"word": "眼鏡を掛ける", "reading": "めがねをかける"},
                {"word": "めがねを掛ける", "reading": "めがねをかける"},
            ],
        },
        {
            "slug": "眼鏡にかなう",
            "japanese": [
                {"word": "眼鏡にかなう", "reading": "めがねにかなう"},
                {"word": "眼鏡に適う", "reading": "めがねにかなう"},
                {"word": "眼鏡に叶う", "reading": "めがねにかなう"},
            ],
        },
        {
            "slug": "眼鏡猿",
            "japanese": [
                {"word": "眼鏡猿", "reading": "めがねざる"},
                {"reading": "メガネザル"},
            ],
        },
        {
            "slug": "眼鏡黐之魚",
            "japanese": [
                {"word": "眼鏡黐之魚", "reading": "めがねもちのうお"},
                {"reading": "メガネモチノウオ"},
            ],
        },
        {
            "slug": "眼鏡熊",
            "japanese": [
                {"word": "眼鏡熊", "reading": "めがねぐま"},
                {"reading": "メガネグマ"},
            ],
        },
        {"slug": "眼鏡屋", "japanese": [{"word": "眼鏡屋", "reading": "めがねや"}]},
        {
            "slug": "眼鏡っ娘",
            "japanese": [
                {"word": "眼鏡っ娘", "reading": "めがねっこ"},
                {"word": "眼鏡っ子", "reading": "めがねっこ"},
                {"word": "めがねっ娘", "reading": "めがねっこ"},
                {"word": "眼鏡娘", "reading": "めがねっこ"},
                {"word": "メガネっ娘", "reading": "メガネっこ"},
                {"word": "メガネっ子", "reading": "メガネっこ"},
            ],
        },
        {
            "slug": "眼鏡海豚",
            "japanese": [
                {"word": "眼鏡海豚", "reading": "めがねいるか"},
                {"reading": "メガネイルカ"},
            ],
        },
    ]
}


COMEBACK: dict[str, JishoAPIResponse] = {
    "カムバック": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "カムバック",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n1"],
                "japanese": [{"reading": "カムバック"}],
                "senses": [
                    {
                        "english_definitions": ["comeback"],
                        "parts_of_speech": ["Noun", "Suru verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "51869cf2d5dda7b2c6074156",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "カムバック賞 (NFL)"}],
                "senses": [
                    {
                        "english_definitions": [
                            "National Football League Comeback Player of the Year Award"
                        ],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “National Football League Comeback Player of the Year Award” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/National_Football_League_Comeback_Player_of_the_Year_Award?oldid=475125217",
                            },
                            {
                                "text": "Read “カムバック賞 (NFL)” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/カムバック賞_(NFL)?oldid=41115243",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/National_Football_League_Comeback_Player_of_the_Year_Award",
                },
            },
            {
                "slug": "5186a020d5dda7b2c608c40c",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "カムバック賞 (日本プロ野球)"}],
                "senses": [
                    {
                        "english_definitions": [
                            "Nippon Professional Baseball Comeback Player of the Year Award"
                        ],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Nippon Professional Baseball Comeback Player of the Year Award” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Nippon_Professional_Baseball_Comeback_Player_of_the_Year_Award?oldid=442329183",
                            },
                            {
                                "text": "Read “カムバック賞 (日本プロ野球)” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/カムバック賞_(日本プロ野球)?oldid=40433478",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Nippon_Professional_Baseball_Comeback_Player_of_the_Year_Award",
                },
            },
            {
                "slug": "51869dc2d5dda7b2c607a433",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "カムバック賞 (MLB)"}],
                "senses": [
                    {
                        "english_definitions": [
                            "Major League Baseball Comeback Player of the Year Award"
                        ],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Major League Baseball Comeback Player of the Year Award” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Major_League_Baseball_Comeback_Player_of_the_Year_Award?oldid=486027670",
                            },
                            {
                                "text": "Read “カムバック賞 (MLB)” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/カムバック賞_(MLB)?oldid=40028177",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Major_League_Baseball_Comeback_Player_of_the_Year_Award",
                },
            },
        ],
    },
}


COMEBACK_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "カムバック": [
        {
            "slug": "カムバック",
            "is_common": True,
            "tags": [],
            "jlpt": ["jlpt-n1"],
            "japanese": [{"reading": "カムバック"}],
            "senses": [
                {
                    "english_definitions": ["comeback"],
                    "parts_of_speech": ["Noun", "Suru verb"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                }
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ],
}


COMEBACK_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "カムバック": [
        {
            "slug": "51869cf2d5dda7b2c6074156",
            "japanese": [{"word": "カムバック賞 (NFL)"}],
        },
        {
            "slug": "5186a020d5dda7b2c608c40c",
            "japanese": [{"word": "カムバック賞 (日本プロ野球)"}],
        },
        {
            "slug": "51869dc2d5dda7b2c607a433",
            "japanese": [{"word": "カムバック賞 (MLB)"}],
        },
    ],
}


TABERU_GAKUSEI: dict[str, JishoAPIResponse] = {
    "食べる": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "食べる",
                "is_common": True,
                "tags": ["wanikani6"],
                "jlpt": ["jlpt-n5"],
                "japanese": [
                    {"word": "食べる", "reading": "たべる"},
                    {"word": "喰べる", "reading": "たべる"},
                ],
                "senses": [
                    {
                        "english_definitions": ["to eat"],
                        "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to live on (e.g. a salary)",
                            "to live off",
                            "to subsist on",
                        ],
                        "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "食べるラー油",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "食べるラー油", "reading": "たべるラーゆ"},
                    {"word": "食べる辣油", "reading": "たべるラーゆ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "chili oil mixed with chopped garlic, onions, etc."
                        ],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Noun",
                        ],
                        "links": [],
                        "tags": ["Food, cooking"],
                        "restrictions": [],
                        "see_also": ["辣油"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    },
    "学生": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "学生",
                "is_common": True,
                "tags": ["wanikani5"],
                "jlpt": ["jlpt-n5"],
                "japanese": [{"word": "学生", "reading": "がくせい"}],
                "senses": [
                    {
                        "english_definitions": ["student (esp. a university student)"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生-1",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "学生", "reading": "がくしょう"},
                    {"word": "学生", "reading": "がくそう"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "Heian-period student of government administration"
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Archaism"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "Buddhist scholar",
                            "researcher at a Buddhist temple",
                            "person studying Buddhism",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Archaism"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["learning", "scholarship"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Archaism"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生時代",
                "is_common": True,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生時代", "reading": "がくせいじだい"}],
                "senses": [
                    {
                        "english_definitions": ["student days"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生運動",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生運動", "reading": "がくせいうんどう"}],
                "senses": [
                    {
                        "english_definitions": ["student movement"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Student activism"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Student activism” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Student_activism?oldid=493780672",
                            },
                            {
                                "text": "Read “学生運動” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/学生運動?oldid=40609526",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Student_activism",
                },
            },
            {
                "slug": "学生生活",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生生活", "reading": "がくせいせいかつ"}],
                "senses": [
                    {
                        "english_definitions": ["student (college) life"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生会",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生会", "reading": "がくせいかい"}],
                "senses": [
                    {
                        "english_definitions": [
                            "student council (details vary widely but a body of students that takes part in overseeing student behaviour or student activities)"
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生服",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生服", "reading": "がくせいふく"}],
                "senses": [
                    {
                        "english_definitions": ["school uniform"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生証",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生証", "reading": "がくせいしょう"}],
                "senses": [
                    {
                        "english_definitions": ["student card", "student ID"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生会館",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "学生会館", "reading": "がくせいかいかん"}],
                "senses": [
                    {
                        "english_definitions": [
                            "student union",
                            "student center",
                            "students' hall",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "学生割引",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "学生割引", "reading": "がくせいわりびき"},
                    {"word": "学生割引き", "reading": "がくせいわりびき"},
                    {"word": "学生割り引き", "reading": "がくせいわりびき"},
                ],
                "senses": [
                    {
                        "english_definitions": ["student discount"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    },
}


TABERU_GAKUSEI_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "食べる": [
        {
            "slug": "食べる",
            "is_common": True,
            "tags": ["wanikani6"],
            "jlpt": ["jlpt-n5"],
            "japanese": [
                {"word": "食べる", "reading": "たべる"},
                {"word": "喰べる", "reading": "たべる"},
            ],
            "senses": [
                {
                    "english_definitions": ["to eat"],
                    "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": [
                        "to live on (e.g. a salary)",
                        "to live off",
                        "to subsist on",
                    ],
                    "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ],
    "学生": [
        {
            "slug": "学生",
            "is_common": True,
            "tags": ["wanikani5"],
            "jlpt": ["jlpt-n5"],
            "japanese": [{"word": "学生", "reading": "がくせい"}],
            "senses": [
                {
                    "english_definitions": ["student (esp. a university student)"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                }
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
        {
            "slug": "学生-1",
            "is_common": False,
            "tags": [],
            "jlpt": [],
            "japanese": [
                {"word": "学生", "reading": "がくしょう"},
                {"word": "学生", "reading": "がくそう"},
            ],
            "senses": [
                {
                    "english_definitions": [
                        "Heian-period student of government administration"
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Archaism"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": [
                        "Buddhist scholar",
                        "researcher at a Buddhist temple",
                        "person studying Buddhism",
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Archaism"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["learning", "scholarship"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Archaism"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ],
}


TABERU_GAKUSEI_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "食べる": [
        {
            "slug": "食べるラー油",
            "japanese": [
                {"word": "食べるラー油", "reading": "たべるラーゆ"},
                {"word": "食べる辣油", "reading": "たべるラーゆ"},
            ],
        },
    ],
    "学生": [
        {
            "slug": "学生時代",
            "japanese": [{"word": "学生時代", "reading": "がくせいじだい"}],
        },
        {
            "slug": "学生運動",
            "japanese": [{"word": "学生運動", "reading": "がくせいうんどう"}],
        },
        {
            "slug": "学生生活",
            "japanese": [{"word": "学生生活", "reading": "がくせいせいかつ"}],
        },
        {"slug": "学生会", "japanese": [{"word": "学生会", "reading": "がくせいかい"}]},
        {"slug": "学生服", "japanese": [{"word": "学生服", "reading": "がくせいふく"}]},
        {
            "slug": "学生証",
            "japanese": [{"word": "学生証", "reading": "がくせいしょう"}],
        },
        {
            "slug": "学生会館",
            "japanese": [{"word": "学生会館", "reading": "がくせいかいかん"}],
        },
        {
            "slug": "学生割引",
            "japanese": [
                {"word": "学生割引", "reading": "がくせいわりびき"},
                {"word": "学生割引き", "reading": "がくせいわりびき"},
                {"word": "学生割り引き", "reading": "がくせいわりびき"},
            ],
        },
    ],
}


KOTOBA: dict[str, JishoAPIResponse] = {
    "言葉": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "言葉",
                "is_common": True,
                "tags": ["wanikani12"],
                "jlpt": ["jlpt-n5"],
                "japanese": [
                    {"word": "言葉", "reading": "ことば"},
                    {"word": "詞", "reading": "ことば"},
                    {"word": "辞", "reading": "ことば"},
                    {"word": "言葉", "reading": "けとば"},
                ],
                "senses": [
                    {
                        "english_definitions": ["language", "dialect"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["言語"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["word", "phrase", "expression", "term"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "speech",
                            "(manner of) speaking",
                            "(use of) language",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "words",
                            "remark",
                            "statement",
                            "comment",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "learning to speak",
                            "language acquisition",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Ci (poetry)"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Ci (poetry)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Ci_(poetry)?oldid=492971177",
                            },
                            {
                                "text": "Read “詞” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/詞?oldid=42783998",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Ci_(poetry)",
                },
            },
            {
                "slug": "辞典",
                "is_common": True,
                "tags": ["wanikani16"],
                "jlpt": ["jlpt-n4"],
                "japanese": [
                    {"word": "辞典", "reading": "じてん"},
                    {"word": "辭典", "reading": "じてん"},
                    {"word": "辞典", "reading": "ことばてん"},
                    {"word": "辭典", "reading": "ことばてん"},
                    {"word": "ことば典", "reading": "ことばてん"},
                    {"word": "言葉典", "reading": "ことばてん"},
                ],
                "senses": [
                    {
                        "english_definitions": ["dictionary", "lexicon"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Dictionary"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Dictionary” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Dictionary?oldid=495507120",
                            },
                            {
                                "text": "Read “辞典” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/辞典?oldid=42126318",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Dictionary",
                },
            },
            {
                "slug": "言葉遣い",
                "is_common": True,
                "tags": ["wanikani39"],
                "jlpt": ["jlpt-n2"],
                "japanese": [
                    {"word": "言葉遣い", "reading": "ことばづかい"},
                    {"word": "言葉使い", "reading": "ことばづかい"},
                    {"word": "言葉づかい", "reading": "ことばづかい"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "speech",
                            "expression",
                            "wording",
                            "language",
                        ],
                        "parts_of_speech": ["Noun", "Suru verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉のあや",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "言葉のあや", "reading": "ことばのあや"},
                    {"word": "言葉の綾", "reading": "ことばのあや"},
                ],
                "senses": [
                    {
                        "english_definitions": ["figure of speech"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉数",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "言葉数", "reading": "ことばかず"}],
                "senses": [
                    {
                        "english_definitions": ["number of words"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["vocality"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉通り",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "言葉通り", "reading": "ことばどおり"},
                    {"word": "言葉どおり", "reading": "ことばどおり"},
                ],
                "senses": [
                    {
                        "english_definitions": ["exactly as stated", "verbatim"],
                        "parts_of_speech": [
                            "Noun",
                            "Noun which may take the genitive case particle 'no'",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉に表せない",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "言葉に表せない", "reading": "ことばにあらわせない"}
                ],
                "senses": [
                    {
                        "english_definitions": ["ineffable", "inexpressible"],
                        "parts_of_speech": ["I-adjective (keiyoushi)"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉に詰まる",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "言葉に詰まる", "reading": "ことばにつまる"}],
                "senses": [
                    {
                        "english_definitions": ["to be at a loss for words"],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Godan verb with ru ending",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉に窮する",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "言葉に窮する", "reading": "ことばにきゅうする"}],
                "senses": [
                    {
                        "english_definitions": ["to be at a loss for words"],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Suru verb - special class",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["言葉に詰まる"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "言葉を交わす",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "言葉を交わす", "reading": "ことばをかわす"}],
                "senses": [
                    {
                        "english_definitions": ["to exchange words"],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Godan verb with su ending",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["言葉を交える"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    }
}


KOTOBA_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "言葉": [
        {
            "slug": "言葉",
            "is_common": True,
            "tags": ["wanikani12"],
            "jlpt": ["jlpt-n5"],
            "japanese": [
                {"word": "言葉", "reading": "ことば"},
                {"word": "詞", "reading": "ことば"},
                {"word": "辞", "reading": "ことば"},
                {"word": "言葉", "reading": "けとば"},
            ],
            "senses": [
                {
                    "english_definitions": ["language", "dialect"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": ["言語"],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["word", "phrase", "expression", "term"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": [
                        "speech",
                        "(manner of) speaking",
                        "(use of) language",
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["words", "remark", "statement", "comment"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": [
                        "learning to speak",
                        "language acquisition",
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["Ci (poetry)"],
                    "parts_of_speech": ["Wikipedia definition"],
                    "links": [
                        {
                            "text": "Read “Ci (poetry)” on English Wikipedia",
                            "url": "http://en.wikipedia.org/wiki/Ci_(poetry)?oldid=492971177",
                        },
                        {
                            "text": "Read “詞” on Japanese Wikipedia",
                            "url": "http://ja.wikipedia.org/wiki/詞?oldid=42783998",
                        },
                    ],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                    "sentences": [],
                },
            ],
            "attribution": {
                "jmdict": True,
                "jmnedict": False,
                "dbpedia": "http://dbpedia.org/resource/Ci_(poetry)",
            },
        },
    ],
}


KOTOBA_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "言葉": [
        {
            "slug": "辞典",
            "japanese": [
                {"word": "辞典", "reading": "じてん"},
                {"word": "辭典", "reading": "じてん"},
                {"word": "辞典", "reading": "ことばてん"},
                {"word": "辭典", "reading": "ことばてん"},
                {"word": "ことば典", "reading": "ことばてん"},
                {"word": "言葉典", "reading": "ことばてん"},
            ],
        },
        {
            "slug": "言葉遣い",
            "japanese": [
                {"word": "言葉遣い", "reading": "ことばづかい"},
                {"word": "言葉使い", "reading": "ことばづかい"},
                {"word": "言葉づかい", "reading": "ことばづかい"},
            ],
        },
        {
            "slug": "言葉のあや",
            "japanese": [
                {"word": "言葉のあや", "reading": "ことばのあや"},
                {"word": "言葉の綾", "reading": "ことばのあや"},
            ],
        },
        {"slug": "言葉数", "japanese": [{"word": "言葉数", "reading": "ことばかず"}]},
        {
            "slug": "言葉通り",
            "japanese": [
                {"word": "言葉通り", "reading": "ことばどおり"},
                {"word": "言葉どおり", "reading": "ことばどおり"},
            ],
        },
        {
            "slug": "言葉に表せない",
            "japanese": [{"word": "言葉に表せない", "reading": "ことばにあらわせない"}],
        },
        {
            "slug": "言葉に詰まる",
            "japanese": [{"word": "言葉に詰まる", "reading": "ことばにつまる"}],
        },
        {
            "slug": "言葉に窮する",
            "japanese": [{"word": "言葉に窮する", "reading": "ことばにきゅうする"}],
        },
        {
            "slug": "言葉を交わす",
            "japanese": [{"word": "言葉を交わす", "reading": "ことばをかわす"}],
        },
    ],
}


BADINPUT: dict[str, JishoAPIResponse] = {
    "BADINPUT": {"meta": {"status": 200}, "data": []}
}


BADINPUT_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "BADINPUT": [],
}


BADINPUT_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "BADINPUT": [],
}


USAGI_IKU_KAGO: dict[str, JishoAPIResponse] = {
    "兎": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "兎",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n3"],
                "japanese": [
                    {"word": "兎", "reading": "うさぎ"},
                    {"word": "兔", "reading": "うさぎ"},
                    {"word": "菟", "reading": "うさぎ"},
                    {"word": "兎", "reading": "う"},
                    {"reading": "ウサギ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "rabbit",
                            "hare",
                            "coney",
                            "cony",
                            "lagomorph (esp. leporids)",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Rabbit"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Rabbit” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Rabbit?oldid=495524916",
                            },
                            {
                                "text": "Read “ウサギ” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/ウサギ?oldid=42544671",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Rabbit",
                },
            },
            {
                "slug": "兎に角",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n3", "jlpt-n1"],
                "japanese": [{"word": "兎に角", "reading": "とにかく"}],
                "senses": [
                    {
                        "english_definitions": [
                            "anyhow",
                            "at any rate",
                            "anyway",
                            "somehow or other",
                            "generally speaking",
                            "in any case",
                            "at least",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "兎も角",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n2", "jlpt-n1"],
                "japanese": [{"word": "兎も角", "reading": "ともかく"}],
                "senses": [
                    {
                        "english_definitions": [
                            "anyhow",
                            "anyway",
                            "somehow or other",
                            "generally speaking",
                            "in any case",
                            "be that as it may",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["apart from ...", "setting ... aside"],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["often as …はともかく"],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "兎角",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n1"],
                "japanese": [
                    {"word": "兎角", "reading": "とかく"},
                    {"word": "左右", "reading": "とかく"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "(doing) various things",
                            "(doing) this and that",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)", "Suru verb"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "being apt to",
                            "being prone to",
                            "tending to",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["at any rate", "anyhow", "anyway"],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "all sorts of (negative things)",
                            "various",
                        ],
                        "parts_of_speech": [
                            "Noun which may take the genitive case particle 'no'"
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "things that do not exist",
                            "rabbit horns",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Buddhism", "Idiomatic expression"],
                        "restrictions": ["兎角"],
                        "see_also": ["亀毛兎角"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "兎もあれ",
                "is_common": True,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "兎もあれ", "reading": "ともあれ"},
                    {"word": "とも有れ", "reading": "ともあれ"},
                    {"word": "兎も有れ", "reading": "ともあれ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["anyhow", "in any case"],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "兎や角",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "兎や角", "reading": "とやかく"}],
                "senses": [
                    {
                        "english_definitions": [
                            "anyhow",
                            "anyway",
                            "somehow or other",
                            "generally speaking",
                            "in any case",
                            "all kinds of this",
                            "this and that",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "うさぎ小屋",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "うさぎ小屋", "reading": "うさぎごや"},
                    {"word": "兎小屋", "reading": "うさぎごや"},
                ],
                "senses": [
                    {
                        "english_definitions": ["rabbit hutch"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "small Japanese houses",
                            "cramped Japanese housing",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["used in 1979 EC report"],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "兎にも角にも",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "兎にも角にも", "reading": "とにもかくにも"}],
                "senses": [
                    {
                        "english_definitions": [
                            "anyhow",
                            "anyway",
                            "somehow or other",
                            "generally speaking",
                            "in any case",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "とやかく言う",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "とやかく言う", "reading": "とやかくいう"},
                    {"word": "兎や角言う", "reading": "とやかくいう"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "to say all kinds of things",
                            "to complain",
                            "to find fault (with)",
                        ],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Godan verb with u ending",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "兎座",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "兎座", "reading": "うさぎざ"},
                    {"word": "うさぎ座", "reading": "うさぎざ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["Lepus (constellation)", "the Hare"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Lepus (constellation)"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Lepus (constellation)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Lepus_(constellation)?oldid=493472936",
                            },
                            {
                                "text": "Read “うさぎ座” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/うさぎ座?oldid=42585708",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Lepus_(constellation)",
                },
            },
        ],
    },
    "行く": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "行く",
                "is_common": True,
                "tags": ["wanikani5"],
                "jlpt": ["jlpt-n1", "jlpt-n5"],
                "japanese": [
                    {"word": "行く", "reading": "いく"},
                    {"word": "行く", "reading": "ゆく"},
                    {"word": "逝く", "reading": "いく"},
                    {"word": "逝く", "reading": "ゆく"},
                    {"word": "往く", "reading": "いく"},
                    {"word": "往く", "reading": "ゆく"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "to go",
                            "to move (in a direction or towards a specific location)",
                            "to head (towards)",
                            "to be transported (towards)",
                            "to reach",
                        ],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["来る くる"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to proceed", "to take place"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["旨く行く"],
                        "antonyms": [],
                        "source": [],
                        "info": ["い sometimes omitted in auxiliary use"],
                    },
                    {
                        "english_definitions": ["to pass through", "to come and go"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to walk"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to die", "to pass away"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": ["逝く"],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to do (in a specific way)"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to stream", "to flow"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to continue"],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Auxiliary verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["after the -te form of a verb"],
                    },
                    {
                        "english_definitions": [
                            "to have an orgasm",
                            "to come",
                            "to cum",
                        ],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to trip",
                            "to get high",
                            "to have a drug-induced hallucination",
                        ],
                        "parts_of_speech": [
                            "Godan verb - Iku/Yuku special class",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone", "Slang"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行方",
                "is_common": True,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "行方", "reading": "ゆくえ"},
                    {"word": "行くえ", "reading": "ゆくえ"},
                    {"word": "行衛", "reading": "ゆくえ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["(one's) whereabouts"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["destination", "where one is headed"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "outcome",
                            "course (of events)",
                            "development",
                            "direction",
                            "tide",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["future", "journey ahead"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行く手",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "行く手", "reading": "ゆくて"}],
                "senses": [
                    {
                        "english_definitions": ["one's way", "one's path"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行末",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "行く末", "reading": "ゆくすえ"},
                    {"word": "行末", "reading": "ゆくすえ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["one's future", "one's fate"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["one's way", "one's path"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行く先",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "行く先", "reading": "ゆくさき"},
                    {"word": "行く先", "reading": "いくさき"},
                ],
                "senses": [
                    {
                        "english_definitions": ["destination"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["whereabouts"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["future", "prospects"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行くあて",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "行くあて", "reading": "いくあて"},
                    {"word": "行く当て", "reading": "いくあて"},
                ],
                "senses": [
                    {
                        "english_definitions": ["somewhere to go", "place to go"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行く春",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "行く春", "reading": "ゆくはる"}],
                "senses": [
                    {
                        "english_definitions": ["the fading of spring"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行く行く",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "行く行く", "reading": "ゆくゆく"}],
                "senses": [
                    {
                        "english_definitions": ["on the way", "someday"],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行く先先",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "行く先々", "reading": "ゆくさきざき"},
                    {"word": "行く先々", "reading": "いくさきざき"},
                    {"word": "行く先先", "reading": "ゆくさきざき"},
                    {"word": "行く先先", "reading": "いくさきざき"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "everywhere",
                            "everywhere one goes",
                            "wherever one goes",
                        ],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Noun",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "行く年",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "行く年", "reading": "ゆくとし"},
                    {"word": "行く年", "reading": "いくとし"},
                ],
                "senses": [
                    {
                        "english_definitions": ["the passing year", "the old year"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    },
    "籠": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "籠",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n3"],
                "japanese": [
                    {"word": "籠", "reading": "かご"},
                    {"word": "篭", "reading": "かご"},
                    {"reading": "カゴ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "basket (shopping, etc.)",
                            "hamper",
                            "cage",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Basket"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Basket” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Basket?oldid=493462729",
                            },
                            {
                                "text": "Read “籠” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/籠?oldid=42584108",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Basket",
                },
            },
            {
                "slug": "牢",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "牢", "reading": "ろう"},
                    {"word": "籠", "reading": "ろう"},
                    {"word": "篭", "reading": "ろう"},
                ],
                "senses": [
                    {
                        "english_definitions": ["prison", "jail", "gaol"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["firm", "solid", "strong"],
                        "parts_of_speech": ["'taru' adjective"],
                        "links": [],
                        "tags": ["Obsolete term"],
                        "restrictions": [],
                        "see_also": ["牢として"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "込む",
                "is_common": True,
                "tags": ["wanikani21", "wanikani32"],
                "jlpt": ["jlpt-n4", "jlpt-n1"],
                "japanese": [{"word": "込む", "reading": "こむ"}],
                "senses": [
                    {
                        "english_definitions": [
                            "to be crowded",
                            "to be packed",
                            "to be congested",
                            "to be thronged (with)",
                        ],
                        "parts_of_speech": [
                            "Godan verb with mu ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["混む"],
                        "antonyms": [],
                        "source": [],
                        "info": ["usu. 混む"],
                    },
                    {
                        "english_definitions": ["to be complex", "to be intricate"],
                        "parts_of_speech": [
                            "Godan verb with mu ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["手の込んだ"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to go into",
                            "to go in",
                            "to put into",
                        ],
                        "parts_of_speech": ["Suffix"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["after -masu stem of verb"],
                    },
                    {
                        "english_definitions": ["to become (completely)"],
                        "parts_of_speech": ["Suffix"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["after -masu stem of verb"],
                    },
                    {
                        "english_definitions": [
                            "to do thoroughly",
                            "to do sufficiently",
                        ],
                        "parts_of_speech": ["Suffix"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["after -masu stem of verb"],
                    },
                    {
                        "english_definitions": [
                            "to remain (silent, seated, etc.)",
                            "to stay ...",
                        ],
                        "parts_of_speech": ["Suffix"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["after -masu stem of verb"],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "込める",
                "is_common": True,
                "tags": ["wanikani34"],
                "jlpt": ["jlpt-n1"],
                "japanese": [
                    {"word": "込める", "reading": "こめる"},
                    {"word": "籠める", "reading": "こめる"},
                    {"word": "篭める", "reading": "こめる"},
                    {"word": "罩める", "reading": "こめる"},
                ],
                "senses": [
                    {
                        "english_definitions": ["to load (a gun, etc.)", "to charge"],
                        "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to put into (e.g. emotion, effort)"],
                        "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to include (e.g. tax in a sales price)"
                        ],
                        "parts_of_speech": ["Ichidan verb", "Transitive verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to hang over",
                            "to shroud",
                            "to enshroud",
                            "to envelop",
                            "to screen",
                        ],
                        "parts_of_speech": ["Ichidan verb", "Intransitive verb"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": ["立ち込める"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "籠もる",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n1"],
                "japanese": [
                    {"word": "篭る", "reading": "こもる"},
                    {"word": "籠もる", "reading": "こもる"},
                    {"word": "篭もる", "reading": "こもる"},
                    {"word": "籠る", "reading": "こもる"},
                    {"word": "隠る", "reading": "こもる"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "to shut oneself in (e.g. one's room)",
                            "to be confined in",
                            "to seclude oneself",
                            "to hide away",
                            "to stay inside (one's shell)",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to be filled with (emotion, enthusiasm, etc.)"
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to fill the room (of a gas, smell, etc.)",
                            "to be heavy with (e.g. smoke)",
                            "to be stuffy",
                            "to be dense",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to be muffled (e.g. voice)"],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to hold (a castle, fortress, etc.)"],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to confine oneself in a temple to pray"
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "籠手",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "籠手", "reading": "こて"},
                    {"word": "篭手", "reading": "こて"},
                    {"word": "小手", "reading": "こて"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "gauntlet (used in Kendo)",
                            "bracer",
                            "fencing glove",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Gauntlet (glove)"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Gauntlet (glove)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Gauntlet_(glove)?oldid=493677597",
                            },
                            {
                                "text": "Read “籠手” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/籠手?oldid=42359927",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Gauntlet_(glove)",
                },
            },
            {
                "slug": "籠目",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "籠目", "reading": "かごめ"}],
                "senses": [
                    {
                        "english_definitions": ["woven-bamboo pattern"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Kagome lattice"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Kagome lattice” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Kagome_lattice?oldid=493069364",
                            },
                            {
                                "text": "Read “籠目” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/籠目?oldid=40417642",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Kagome_lattice",
                },
            },
            {
                "slug": "籠屋",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "籠屋", "reading": "かごや"}],
                "senses": [
                    {
                        "english_definitions": ["basket maker"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Kagoya"],
                        "parts_of_speech": ["Place"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": True, "dbpedia": False},
            },
            {
                "slug": "籠の垂れ",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "籠の垂れ", "reading": "かごのたれ"}],
                "senses": [
                    {
                        "english_definitions": ["hanging of a palanquin"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "籠もった声",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "こもった声", "reading": "こもったこえ"},
                    {"word": "籠もった声", "reading": "こもったこえ"},
                ],
                "senses": [
                    {
                        "english_definitions": ["thick voice"],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Noun",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    },
}


USAGI_IKU_KAGO_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "兎": [
        {
            "slug": "兎",
            "is_common": True,
            "tags": [],
            "jlpt": ["jlpt-n3"],
            "japanese": [
                {"word": "兎", "reading": "うさぎ"},
                {"word": "兔", "reading": "うさぎ"},
                {"word": "菟", "reading": "うさぎ"},
                {"word": "兎", "reading": "う"},
                {"reading": "ウサギ"},
            ],
            "senses": [
                {
                    "english_definitions": [
                        "rabbit",
                        "hare",
                        "coney",
                        "cony",
                        "lagomorph (esp. leporids)",
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Usually written using kana alone"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["Rabbit"],
                    "parts_of_speech": ["Wikipedia definition"],
                    "links": [
                        {
                            "text": "Read “Rabbit” on English Wikipedia",
                            "url": "http://en.wikipedia.org/wiki/Rabbit?oldid=495524916",
                        },
                        {
                            "text": "Read “ウサギ” on Japanese Wikipedia",
                            "url": "http://ja.wikipedia.org/wiki/ウサギ?oldid=42544671",
                        },
                    ],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                    "sentences": [],
                },
            ],
            "attribution": {
                "jmdict": True,
                "jmnedict": False,
                "dbpedia": "http://dbpedia.org/resource/Rabbit",
            },
        },
    ],
    "行く": [
        {
            "slug": "行く",
            "is_common": True,
            "tags": ["wanikani5"],
            "jlpt": ["jlpt-n1", "jlpt-n5"],
            "japanese": [
                {"word": "行く", "reading": "いく"},
                {"word": "行く", "reading": "ゆく"},
                {"word": "逝く", "reading": "いく"},
                {"word": "逝く", "reading": "ゆく"},
                {"word": "往く", "reading": "いく"},
                {"word": "往く", "reading": "ゆく"},
            ],
            "senses": [
                {
                    "english_definitions": [
                        "to go",
                        "to move (in a direction or towards a specific location)",
                        "to head (towards)",
                        "to be transported (towards)",
                        "to reach",
                    ],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": ["来る くる"],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["to proceed", "to take place"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": ["旨く行く"],
                    "antonyms": [],
                    "source": [],
                    "info": ["い sometimes omitted in auxiliary use"],
                },
                {
                    "english_definitions": ["to pass through", "to come and go"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["to walk"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["to die", "to pass away"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": ["逝く"],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["to do (in a specific way)"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["to stream", "to flow"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["to continue"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Auxiliary verb",
                    ],
                    "links": [],
                    "tags": ["Usually written using kana alone"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": ["after the -te form of a verb"],
                },
                {
                    "english_definitions": ["to have an orgasm", "to come", "to cum"],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": ["Usually written using kana alone"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": [
                        "to trip",
                        "to get high",
                        "to have a drug-induced hallucination",
                    ],
                    "parts_of_speech": [
                        "Godan verb - Iku/Yuku special class",
                        "Intransitive verb",
                    ],
                    "links": [],
                    "tags": ["Usually written using kana alone", "Slang"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ],
    "籠": [
        {
            "slug": "籠",
            "is_common": True,
            "tags": [],
            "jlpt": ["jlpt-n3"],
            "japanese": [
                {"word": "籠", "reading": "かご"},
                {"word": "篭", "reading": "かご"},
                {"reading": "カゴ"},
            ],
            "senses": [
                {
                    "english_definitions": [
                        "basket (shopping, etc.)",
                        "hamper",
                        "cage",
                    ],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": ["Usually written using kana alone"],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["Basket"],
                    "parts_of_speech": ["Wikipedia definition"],
                    "links": [
                        {
                            "text": "Read “Basket” on English Wikipedia",
                            "url": "http://en.wikipedia.org/wiki/Basket?oldid=493462729",
                        },
                        {
                            "text": "Read “籠” on Japanese Wikipedia",
                            "url": "http://ja.wikipedia.org/wiki/籠?oldid=42584108",
                        },
                    ],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                    "sentences": [],
                },
            ],
            "attribution": {
                "jmdict": True,
                "jmnedict": False,
                "dbpedia": "http://dbpedia.org/resource/Basket",
            },
        },
        {
            "slug": "牢",
            "is_common": False,
            "tags": [],
            "jlpt": [],
            "japanese": [
                {"word": "牢", "reading": "ろう"},
                {"word": "籠", "reading": "ろう"},
                {"word": "篭", "reading": "ろう"},
            ],
            "senses": [
                {
                    "english_definitions": ["prison", "jail", "gaol"],
                    "parts_of_speech": ["Noun"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["firm", "solid", "strong"],
                    "parts_of_speech": ["'taru' adjective"],
                    "links": [],
                    "tags": ["Obsolete term"],
                    "restrictions": [],
                    "see_also": ["牢として"],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ],
}


USAGI_IKU_KAGO_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "兎": [
        {"slug": "兎に角", "japanese": [{"word": "兎に角", "reading": "とにかく"}]},
        {"slug": "兎も角", "japanese": [{"word": "兎も角", "reading": "ともかく"}]},
        {
            "slug": "兎角",
            "japanese": [
                {"word": "兎角", "reading": "とかく"},
                {"word": "左右", "reading": "とかく"},
            ],
        },
        {
            "slug": "兎もあれ",
            "japanese": [
                {"word": "兎もあれ", "reading": "ともあれ"},
                {"word": "とも有れ", "reading": "ともあれ"},
                {"word": "兎も有れ", "reading": "ともあれ"},
            ],
        },
        {"slug": "兎や角", "japanese": [{"word": "兎や角", "reading": "とやかく"}]},
        {
            "slug": "うさぎ小屋",
            "japanese": [
                {"word": "うさぎ小屋", "reading": "うさぎごや"},
                {"word": "兎小屋", "reading": "うさぎごや"},
            ],
        },
        {
            "slug": "兎にも角にも",
            "japanese": [{"word": "兎にも角にも", "reading": "とにもかくにも"}],
        },
        {
            "slug": "とやかく言う",
            "japanese": [
                {"word": "とやかく言う", "reading": "とやかくいう"},
                {"word": "兎や角言う", "reading": "とやかくいう"},
            ],
        },
        {
            "slug": "兎座",
            "japanese": [
                {"word": "兎座", "reading": "うさぎざ"},
                {"word": "うさぎ座", "reading": "うさぎざ"},
            ],
        },
    ],
    "行く": [
        {
            "slug": "行方",
            "japanese": [
                {"word": "行方", "reading": "ゆくえ"},
                {"word": "行くえ", "reading": "ゆくえ"},
                {"word": "行衛", "reading": "ゆくえ"},
            ],
        },
        {"slug": "行く手", "japanese": [{"word": "行く手", "reading": "ゆくて"}]},
        {
            "slug": "行末",
            "japanese": [
                {"word": "行く末", "reading": "ゆくすえ"},
                {"word": "行末", "reading": "ゆくすえ"},
            ],
        },
        {
            "slug": "行く先",
            "japanese": [
                {"word": "行く先", "reading": "ゆくさき"},
                {"word": "行く先", "reading": "いくさき"},
            ],
        },
        {
            "slug": "行くあて",
            "japanese": [
                {"word": "行くあて", "reading": "いくあて"},
                {"word": "行く当て", "reading": "いくあて"},
            ],
        },
        {"slug": "行く春", "japanese": [{"word": "行く春", "reading": "ゆくはる"}]},
        {"slug": "行く行く", "japanese": [{"word": "行く行く", "reading": "ゆくゆく"}]},
        {
            "slug": "行く先先",
            "japanese": [
                {"word": "行く先々", "reading": "ゆくさきざき"},
                {"word": "行く先々", "reading": "いくさきざき"},
                {"word": "行く先先", "reading": "ゆくさきざき"},
                {"word": "行く先先", "reading": "いくさきざき"},
            ],
        },
        {
            "slug": "行く年",
            "japanese": [
                {"word": "行く年", "reading": "ゆくとし"},
                {"word": "行く年", "reading": "いくとし"},
            ],
        },
    ],
    "籠": [
        {"slug": "込む", "japanese": [{"word": "込む", "reading": "こむ"}]},
        {
            "slug": "込める",
            "japanese": [
                {"word": "込める", "reading": "こめる"},
                {"word": "籠める", "reading": "こめる"},
                {"word": "篭める", "reading": "こめる"},
                {"word": "罩める", "reading": "こめる"},
            ],
        },
        {
            "slug": "籠もる",
            "japanese": [
                {"word": "篭る", "reading": "こもる"},
                {"word": "籠もる", "reading": "こもる"},
                {"word": "篭もる", "reading": "こもる"},
                {"word": "籠る", "reading": "こもる"},
                {"word": "隠る", "reading": "こもる"},
            ],
        },
        {
            "slug": "籠手",
            "japanese": [
                {"word": "籠手", "reading": "こて"},
                {"word": "篭手", "reading": "こて"},
                {"word": "小手", "reading": "こて"},
            ],
        },
        {"slug": "籠目", "japanese": [{"word": "籠目", "reading": "かごめ"}]},
        {"slug": "籠屋", "japanese": [{"word": "籠屋", "reading": "かごや"}]},
        {
            "slug": "籠の垂れ",
            "japanese": [{"word": "籠の垂れ", "reading": "かごのたれ"}],
        },
        {
            "slug": "籠もった声",
            "japanese": [
                {"word": "こもった声", "reading": "こもったこえ"},
                {"word": "籠もった声", "reading": "こもったこえ"},
            ],
        },
    ],
}


SHIZUKA: dict[str, JishoAPIResponse] = {
    "静か": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "静か",
                "is_common": True,
                "tags": ["wanikani18"],
                "jlpt": ["jlpt-n5"],
                "japanese": [
                    {"word": "静か", "reading": "しずか"},
                    {"word": "閑か", "reading": "しずか"},
                ],
                "senses": [
                    {
                        "english_definitions": ["quiet", "silent"],
                        "parts_of_speech": ["Na-adjective (keiyodoshi)"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["slow", "unhurried"],
                        "parts_of_speech": ["Na-adjective (keiyodoshi)"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["calm", "peaceful"],
                        "parts_of_speech": ["Na-adjective (keiyodoshi)"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "静かに",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かに", "reading": "しずかに"}],
                "senses": [
                    {
                        "english_definitions": [
                            "calmly",
                            "quietly",
                            "gently",
                            "peacefully",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["be quiet!"],
                        "parts_of_speech": ["Expressions (phrases, clauses, etc.)"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "静かの海",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かの海", "reading": "しずかのうみ"}],
                "senses": [
                    {
                        "english_definitions": [
                            "Mare Tranquillitatis (lunar mare)",
                            "Sea of Tranquility",
                        ],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Noun",
                        ],
                        "links": [],
                        "tags": ["Astronomy"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Mare Tranquillitatis"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Mare Tranquillitatis” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Mare_Tranquillitatis?oldid=491642441",
                            },
                            {
                                "text": "Read “静かの海” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かの海?oldid=39495940",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Mare_Tranquillitatis",
                },
            },
            {
                "slug": "静かに流れる川は深い",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {
                        "word": "静かに流れる川は深い",
                        "reading": "しずかにながれるかわはふかい",
                    }
                ],
                "senses": [
                    {
                        "english_definitions": ["still waters run deep"],
                        "parts_of_speech": ["Expressions (phrases, clauses, etc.)"],
                        "links": [],
                        "tags": ["Proverb"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "51869194d5dda7b2c601eed0",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かなるドン"}],
                "senses": [
                    {
                        "english_definitions": ["Shizukanaru Don – Yakuza Side Story"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Shizukanaru Don – Yakuza Side Story” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Shizukanaru_Don_–_Yakuza_Side_Story?oldid=484756913",
                            },
                            {
                                "text": "Read “静かなるドン” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かなるドン?oldid=42702525",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Shizukanaru_Don_–_Yakuza_Side_Story",
                },
            },
            {
                "slug": "518698ead5dda7b2c60558f8",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かな海と楽しい航海 (ベートーヴェン)"}],
                "senses": [
                    {
                        "english_definitions": [
                            "Meeresstille und glückliche Fahrt (Beethoven)"
                        ],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Meeresstille und glückliche Fahrt (Beethoven)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Meeresstille_und_glückliche_Fahrt_(Beethoven)?oldid=479910186",
                            },
                            {
                                "text": "Read “静かな海と楽しい航海 (ベートーヴェン)” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かな海と楽しい航海_(ベートーヴェン)?oldid=42714534",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Meeresstille_und_glückliche_Fahrt_(Beethoven)",
                },
            },
            {
                "slug": "51869907d5dda7b2c60566de",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かな海と楽しい航海"}],
                "senses": [
                    {
                        "english_definitions": ["Meeresstille und glückliche Fahrt"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Meeresstille und glückliche Fahrt” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Meeresstille_und_glückliche_Fahrt?oldid=331143930",
                            },
                            {
                                "text": "Read “静かな海と楽しい航海” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かな海と楽しい航海?oldid=33012848",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Meeresstille_und_glückliche_Fahrt",
                },
            },
            {
                "slug": "51869460d5dda7b2c6033553",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かなる決闘"}],
                "senses": [
                    {
                        "english_definitions": ["The Quiet Duel"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “The Quiet Duel” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/The_Quiet_Duel?oldid=493806114",
                            },
                            {
                                "text": "Read “静かなる決闘” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かなる決闘?oldid=42083091",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/The_Quiet_Duel",
                },
            },
            {
                "slug": "51869908d5dda7b2c60566e2",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かな海と楽しい航海 (メンデルスゾーン)"}],
                "senses": [
                    {
                        "english_definitions": [
                            "Calm Sea and Prosperous Voyage (Mendelssohn)"
                        ],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Calm Sea and Prosperous Voyage (Mendelssohn)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Calm_Sea_and_Prosperous_Voyage_(Mendelssohn)?oldid=477650035",
                            },
                            {
                                "text": "Read “静かな海と楽しい航海 (メンデルスゾーン)” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かな海と楽しい航海_(メンデルスゾーン)?oldid=34559349",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Calm_Sea_and_Prosperous_Voyage_(Mendelssohn)",
                },
            },
            {
                "slug": "51869d05d5dda7b2c6074a12",
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "静かなアメリカ人"}],
                "senses": [
                    {
                        "english_definitions": ["The Quiet American (1958 film)"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “The Quiet American (1958 film)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/The_Quiet_American_(1958_film)?oldid=481847151",
                            },
                            {
                                "text": "Read “静かなアメリカ人” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/静かなアメリカ人?oldid=42237483",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    }
                ],
                "attribution": {
                    "jmdict": False,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/The_Quiet_American_(1958_film)",
                },
            },
        ],
    }
}


SHIZUKA_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "静か": [
        {
            "slug": "静か",
            "is_common": True,
            "tags": ["wanikani18"],
            "jlpt": ["jlpt-n5"],
            "japanese": [
                {"word": "静か", "reading": "しずか"},
                {"word": "閑か", "reading": "しずか"},
            ],
            "senses": [
                {
                    "english_definitions": ["quiet", "silent"],
                    "parts_of_speech": ["Na-adjective (keiyodoshi)"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["slow", "unhurried"],
                    "parts_of_speech": ["Na-adjective (keiyodoshi)"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["calm", "peaceful"],
                    "parts_of_speech": ["Na-adjective (keiyodoshi)"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ],
}


SHIZUKA_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "静か": [
        {"slug": "静かに", "japanese": [{"word": "静かに", "reading": "しずかに"}]},
        {
            "slug": "静かの海",
            "japanese": [{"word": "静かの海", "reading": "しずかのうみ"}],
        },
        {
            "slug": "静かに流れる川は深い",
            "japanese": [
                {
                    "word": "静かに流れる川は深い",
                    "reading": "しずかにながれるかわはふかい",
                }
            ],
        },
        {"slug": "51869194d5dda7b2c601eed0", "japanese": [{"word": "静かなるドン"}]},
        {
            "slug": "518698ead5dda7b2c60558f8",
            "japanese": [{"word": "静かな海と楽しい航海 (ベートーヴェン)"}],
        },
        {
            "slug": "51869907d5dda7b2c60566de",
            "japanese": [{"word": "静かな海と楽しい航海"}],
        },
        {"slug": "51869460d5dda7b2c6033553", "japanese": [{"word": "静かなる決闘"}]},
        {
            "slug": "51869908d5dda7b2c60566e2",
            "japanese": [{"word": "静かな海と楽しい航海 (メンデルスゾーン)"}],
        },
        {
            "slug": "51869d05d5dda7b2c6074a12",
            "japanese": [{"word": "静かなアメリカ人"}],
        },
    ],
}


NARU: dict[str, JishoAPIResponse] = {
    "なる": {
        "meta": {"status": 200},
        "data": [
            {
                "slug": "成る",
                "is_common": True,
                "tags": ["wanikani11"],
                "jlpt": ["jlpt-n3", "jlpt-n5"],
                "japanese": [
                    {"word": "成る", "reading": "なる"},
                    {"word": "為る", "reading": "なる"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "to become",
                            "to get",
                            "to grow",
                            "to turn",
                            "to reach",
                            "to attain",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to result in",
                            "to turn out",
                            "to end up",
                            "to prove (to be)",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to consist of",
                            "to be composed of",
                            "to be made up of",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["as ...からなる or ...よりなる"],
                    },
                    {
                        "english_definitions": [
                            "to be completed",
                            "to be realized",
                            "to succeed",
                            "to be attained",
                            "to be accomplished",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to change (into)",
                            "to turn (into)",
                            "to transform",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to come (to do)",
                            "to begin (to do)",
                            "to grow (to do)",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to come to",
                            "to amount to",
                            "to add up to",
                            "to make",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to play (the part of)", "to act as"],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "to be used for",
                            "to be useful for",
                            "to serve as",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to be promoted"],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Shogi"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["to do ..."],
                        "parts_of_speech": [
                            "Auxiliary verb",
                            "Godan verb with ru ending",
                        ],
                        "links": [],
                        "tags": [
                            "Honorific or respectful (sonkeigo) language",
                            "Usually written using kana alone",
                        ],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["as お + masu stem + になる or ご + noun+ になる"],
                    },
                    {
                        "english_definitions": ["Naru"],
                        "parts_of_speech": ["Place"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": True, "dbpedia": False},
            },
            {
                "slug": "鳴る",
                "is_common": True,
                "tags": ["wanikani12"],
                "jlpt": ["jlpt-n4"],
                "japanese": [{"word": "鳴る", "reading": "なる"}],
                "senses": [
                    {
                        "english_definitions": [
                            "to sound",
                            "to ring",
                            "to resound",
                            "to echo",
                            "to roar",
                            "to rumble",
                        ],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "生る",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n2"],
                "japanese": [{"word": "生る", "reading": "なる"}],
                "senses": [
                    {
                        "english_definitions": ["to bear fruit"],
                        "parts_of_speech": [
                            "Godan verb with ru ending",
                            "Intransitive verb",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "なる",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"reading": "なる"}],
                "senses": [
                    {
                        "english_definitions": ["that is in"],
                        "parts_of_speech": [
                            "Suffix",
                            "Noun or verb acting prenominally",
                        ],
                        "links": [],
                        "tags": ["Archaism"],
                        "restrictions": [],
                        "see_also": ["也 なり"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["who is called", "that is called"],
                        "parts_of_speech": [
                            "Suffix",
                            "Noun or verb acting prenominally",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["that is"],
                        "parts_of_speech": [
                            "Suffix",
                            "Noun or verb acting prenominally",
                        ],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["I see"],
                        "parts_of_speech": [],
                        "links": [],
                        "tags": ["Slang", "Abbreviation"],
                        "restrictions": [],
                        "see_also": ["なるほど"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "ナル",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"reading": "ナル"}],
                "senses": [
                    {
                        "english_definitions": ["narcissistic"],
                        "parts_of_speech": ["Noun", "Na-adjective (keiyodoshi)"],
                        "links": [],
                        "tags": ["Abbreviation", "Slang"],
                        "restrictions": [],
                        "see_also": ["ナルシシスト"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "成程",
                "is_common": True,
                "tags": ["wanikani30"],
                "jlpt": ["jlpt-n4"],
                "japanese": [
                    {"word": "なる程", "reading": "なるほど"},
                    {"word": "成る程", "reading": "なるほど"},
                    {"word": "成程", "reading": "なるほど"},
                    {"word": "成るほど", "reading": "なるほど"},
                    {"reading": "ナルホド"},
                ],
                "senses": [
                    {
                        "english_definitions": ["I see", "that's right", "indeed"],
                        "parts_of_speech": [
                            "Expressions (phrases, clauses, etc.)",
                            "Adverb (fukushi)",
                        ],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "成るべく",
                "is_common": True,
                "tags": [],
                "jlpt": ["jlpt-n4", "jlpt-n1"],
                "japanese": [
                    {"word": "成るべく", "reading": "なるべく"},
                    {"word": "成る可く", "reading": "なるべく"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "as (much) as possible",
                            "as (much) as one can",
                            "wherever practicable",
                            "if possible",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "鳴門",
                "is_common": True,
                "tags": [],
                "jlpt": [],
                "japanese": [
                    {"word": "鳴門", "reading": "なると"},
                    {"word": "鳴戸", "reading": "なると"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "strait with a roaring tidal ebb and flow",
                            "whirlpool",
                            "maelstrom",
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["from 鳴門海峡"],
                    },
                    {
                        "english_definitions": [
                            "kamaboko with a spiral whirlpool-like pattern"
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Abbreviation"],
                        "restrictions": [],
                        "see_also": ["鳴門巻き"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": [
                            "cooking technique where ingredients are cut in a spiral pattern"
                        ],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Food, cooking"],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Naruto (city in Tokushima)"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": ["鳴門"],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Naruto Strait"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Abbreviation"],
                        "restrictions": ["鳴門"],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": ["from 鳴門海峡"],
                    },
                    {
                        "english_definitions": ["Naruto wakame"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": ["Abbreviation"],
                        "restrictions": ["鳴門"],
                        "see_also": ["鳴門若布 なるとわかめ"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    },
                    {
                        "english_definitions": ["Naruto (toshiyori)"],
                        "parts_of_speech": ["Wikipedia definition"],
                        "links": [
                            {
                                "text": "Read “Naruto (toshiyori)” on English Wikipedia",
                                "url": "http://en.wikipedia.org/wiki/Naruto_(toshiyori)?oldid=331576324",
                            },
                            {
                                "text": "Read “鳴戸” on Japanese Wikipedia",
                                "url": "http://ja.wikipedia.org/wiki/鳴戸?oldid=40203711",
                            },
                        ],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                        "sentences": [],
                    },
                ],
                "attribution": {
                    "jmdict": True,
                    "jmnedict": False,
                    "dbpedia": "http://dbpedia.org/resource/Naruto_(toshiyori)",
                },
            },
            {
                "slug": "成る丈",
                "is_common": False,
                "tags": [],
                "jlpt": ["jlpt-n1"],
                "japanese": [
                    {"word": "成る丈", "reading": "なるたけ"},
                    {"word": "成るたけ", "reading": "なるたけ"},
                    {"word": "成る丈", "reading": "なるだけ"},
                ],
                "senses": [
                    {
                        "english_definitions": [
                            "as (much) as possible",
                            "as (much) as one can",
                            "wherever practicable",
                            "if possible",
                        ],
                        "parts_of_speech": ["Adverb (fukushi)"],
                        "links": [],
                        "tags": ["Usually written using kana alone"],
                        "restrictions": [],
                        "see_also": ["なるべく"],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
            {
                "slug": "鳴子",
                "is_common": False,
                "tags": [],
                "jlpt": [],
                "japanese": [{"word": "鳴子", "reading": "なるこ"}],
                "senses": [
                    {
                        "english_definitions": ["clapper"],
                        "parts_of_speech": ["Noun"],
                        "links": [],
                        "tags": [],
                        "restrictions": [],
                        "see_also": [],
                        "antonyms": [],
                        "source": [],
                        "info": [],
                    }
                ],
                "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
            },
        ],
    }
}


NARU_FILTERED_ITEMS: dict[str, list[JishoAPIItem]] = {
    "なる": [
        {
            "slug": "なる",
            "is_common": False,
            "tags": [],
            "jlpt": [],
            "japanese": [{"reading": "なる"}],
            "senses": [
                {
                    "english_definitions": ["that is in"],
                    "parts_of_speech": ["Suffix", "Noun or verb acting prenominally"],
                    "links": [],
                    "tags": ["Archaism"],
                    "restrictions": [],
                    "see_also": ["也 なり"],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["who is called", "that is called"],
                    "parts_of_speech": ["Suffix", "Noun or verb acting prenominally"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["that is"],
                    "parts_of_speech": ["Suffix", "Noun or verb acting prenominally"],
                    "links": [],
                    "tags": [],
                    "restrictions": [],
                    "see_also": [],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
                {
                    "english_definitions": ["I see"],
                    "parts_of_speech": [],
                    "links": [],
                    "tags": ["Slang", "Abbreviation"],
                    "restrictions": [],
                    "see_also": ["なるほど"],
                    "antonyms": [],
                    "source": [],
                    "info": [],
                },
            ],
            "attribution": {"jmdict": True, "jmnedict": False, "dbpedia": False},
        },
    ]
}


NARU_EXTRA_ITEMS: dict[str, list[JishoExtraItem]] = {
    "なる": [
        {
            "slug": "成る",
            "japanese": [
                {"word": "成る", "reading": "なる"},
                {"word": "為る", "reading": "なる"},
            ],
        },
        {"slug": "鳴る", "japanese": [{"word": "鳴る", "reading": "なる"}]},
        {"slug": "生る", "japanese": [{"word": "生る", "reading": "なる"}]},
        {"slug": "ナル", "japanese": [{"reading": "ナル"}]},
        {
            "slug": "成程",
            "japanese": [
                {"word": "なる程", "reading": "なるほど"},
                {"word": "成る程", "reading": "なるほど"},
                {"word": "成程", "reading": "なるほど"},
                {"word": "成るほど", "reading": "なるほど"},
                {"reading": "ナルホド"},
            ],
        },
        {
            "slug": "成るべく",
            "japanese": [
                {"word": "成るべく", "reading": "なるべく"},
                {"word": "成る可く", "reading": "なるべく"},
            ],
        },
        {
            "slug": "鳴門",
            "japanese": [
                {"word": "鳴門", "reading": "なると"},
                {"word": "鳴戸", "reading": "なると"},
            ],
        },
        {
            "slug": "成る丈",
            "japanese": [
                {"word": "成る丈", "reading": "なるたけ"},
                {"word": "成るたけ", "reading": "なるたけ"},
                {"word": "成る丈", "reading": "なるだけ"},
            ],
        },
        {"slug": "鳴子", "japanese": [{"word": "鳴子", "reading": "なるこ"}]},
    ]
}
