import json

import requests

API_URL = "http://3.8.95.26:5000/words"
payload = {"words": json.dumps(["食べる", "学生"])}
result = requests.get(API_URL, params=payload)
pretty_result = json.dumps(json.loads(result.text), indent=4)
print(pretty_result)

example_response = [
    {
        "word": "\u98df\u3079\u308b",
        "forvo": {
            "success": True,
            "main_data": {
                "audio": [
                    {
                        "url": "https://apifree.forvo.com/audio/1h1i3i1n2c2q3h3l1o232l1j3h1h1l2c1j1i3g313h2g2g1p213k3k2h2h3c3f213q2a2a381g2g1p2e3q332e2g1b2l1m311m321p281j2b2f1j1j36312n1b263d1n27273m3l3q273c222j2p1h321m3g343o221m3c1k24371t1t_3g25252p2q36222g1b3d2q3f2d3h2g3b2j3m1g3b36211t1t",
                        "username": "mi8NatsuKi",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2a2g2m263c2e1j1p2n1g362k2c3b362n3d2a1p2h223p2d1g251o273a3l2d2o2h2g322e1f253p2i3k1g3f1m2o3c2h2j2p1l283d3b22382a393d3d1m3f3e3o1b1m_2g2c3f2p3b2i322n35311f3b2b322i1b3n29282q1i371t1t",
                        "username": "kiiro",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/3h263q312o213138283a3i2o1m35332n2l1b2f1j1o3q3f3l2f25333p2n231g1b1k2o31282h1g2a213c3n1m1g2c283839363g1p3e2h3b1l24363n391m3k3m1i39_3n2c3a3436283j392p1b3b2c3a2822323g3b313c2b211t1t",
                        "username": "mutsusoken",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2c2g2b3k2m2o1k282j1j1g1f352q2j1m23362o252o341p3i3f1n362i2m3437392d2i29281n3d2i1i3f1n3n361o3b1j352j2p292l3f3g372q293m3g3p2g3i312m_251h1n352g1l3n3c2p2i1b3g2g3i3h1f2d3p1l2g1h371t1t",
                        "username": "strawberrybrown",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2f381l362a233c1n212q2j2c3i3727393q3g3b3k28321p243j293139233e3p1j3o3k1l2k1p1n2g1l241p1g3o3e3h3d3g2j2o1f2q3h2i282l1n2d1n1b2o3m3o33_3e2k3j3p3i23362j3q35331h3g1k2p2m1f2l34312g2h1t1t",
                        "username": "leona1",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2m1g1g223m35283e3g312j1f3b2e3h2c3o2f3q3o1b272h3j2a342g383q2c3f352a3q1p252q2m1g1j2m1i2h3q3e3b2o1f1k2o1h1g21372h361l2n231l2b2a322f_3g3g3q3m3q2g1m1g3d2m272d3o3f2b3b3b2e3f3535371t1t",
                        "username": "chiharu",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2c363f2d29343l3e2c3k2e2h3n2l2a1o1o2n25371p323q1i1i2h362a313f3a2l3528383i2h3o293d1h2k2b2h293h3j252a35283g3c2b222a25272q3d3n23383n_32222q2i3g1i1m3q3k1m273q213n3438342l24341g211t1t",
                        "username": "skent",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2q2g24263327393q1g3p3p1o3d2f351m3i362j2p1p3i371f3e2n362m3o3l1m1o3i3p3q3m3g3q291k2m2n3n2n2d3g2q3b1i3d3c35281n3p3m3b2b1j25252c2125_26321m1f3h3c2b3f2n2b3b1m3g2g272o1o2f1i2g3a371t1t",
                        "username": "straycat88",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/3q2j1f2f2j283l3p3n2m3g3q26211p3b2d21372m2i223i233h2m3p21231p233e3k3g363734291k2q2j3l2o2h3a351j2525383n1b1k35383a22322d3n2f323l1i_2p372g3736353n393m2l2c2f262f373c1i2l2d3q2h2h1t1t",
                        "username": "le_temps_perdu",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/3n363m1l2i2a3q3j3g231l1n1f3n2b2h3i2n3j3m1j212e293h1i1f1j352b2i312m2l3l1n1i25393f3n281h382f2m2o3l1j2b2l2a293c1g2i2b2m3q1g1i3m2m2g_3734211k3g2n1k1h3n1b1p283f2k29251g2i1k323i211t1t",
                        "username": "monekuson",
                    },
                ]
            },
        },
        "jisho": {
            "success": True,
            "main_data": {
                "results": [
                    {
                        "slug": "\u98df\u3079\u308b",
                        "is_common": True,
                        "tags": ["wanikani6"],
                        "jlpt": ["jlpt-n5"],
                        "japanese": [
                            {
                                "word": "\u98df\u3079\u308b",
                                "reading": "\u305f\u3079\u308b",
                            },
                            {
                                "word": "\u55b0\u3079\u308b",
                                "reading": "\u305f\u3079\u308b",
                            },
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
                        "attribution": {
                            "jmdict": True,
                            "jmnedict": False,
                            "dbpedia": False,
                        },
                    }
                ],
                "extra": [
                    {
                        "slug": "\u98df\u3079\u308b\u30e9\u30fc\u6cb9",
                        "japanese": [
                            {
                                "word": "\u98df\u3079\u308b\u30e9\u30fc\u6cb9",
                                "reading": "\u305f\u3079\u308b\u30e9\u30fc\u3086",
                            },
                            {
                                "word": "\u98df\u3079\u308b\u8fa3\u6cb9",
                                "reading": "\u305f\u3079\u308b\u30e9\u30fc\u3086",
                            },
                        ],
                    }
                ],
            },
        },
        "ojad": {"success": True, "main_data": {"accent": ["\u305f\u3079' \u308b"]}},
        "suzuki": {"success": True, "main_data": {"accent": ["\u305f\u3079' \u308b"]}},
        "wadoku": {"success": True, "main_data": {"accent": ["\u305f\u3079' \u308b"]}},
        "wanikani": {
            "success": True,
            "main_data": {
                "audio": [
                    {
                        "url": "https://files.wanikani.com/8e5vf9sc17iajyx2d3838oi6chnh",
                        "metadata": {
                            "gender": "female",
                            "source_id": 27468,
                            "pronunciation": "\u305f\u3079\u308b",
                            "voice_actor_id": 1,
                            "voice_actor_name": "Kyoko",
                            "voice_description": "Tokyo accent",
                        },
                        "content_type": "audio/mpeg",
                    },
                    {
                        "url": "https://files.wanikani.com/ng81br3v7kwq5ybljgadillfzqay",
                        "metadata": {
                            "gender": "male",
                            "source_id": 10592,
                            "pronunciation": "\u305f\u3079\u308b",
                            "voice_actor_id": 2,
                            "voice_actor_name": "Kenichi",
                            "voice_description": "Tokyo accent",
                        },
                        "content_type": "audio/mpeg",
                    },
                ],
                "sentences": [
                    {
                        "en": "I eat natto every morning.",
                        "ja": "\u6bce\u3042\u3055\u3001\u306a\u3063\u3068\u3046\u3092\u98df\u3079\u307e\u3059\u3002",
                    },
                    {
                        "en": "I never have enough time to eat healthy foods.",
                        "ja": "\u3044\u3064\u3082\u3001\u3051\u3093\u3053\u3046\u306b\u3044\u3044\u3082\u306e\u3092\u98df\u3079\u308b\u3058\u304b\u3093\u304c\u306a\u3044\u3093\u3067\u3059\u3002",
                    },
                    {
                        "en": "I like to eat while I\u2019m sleeping. It\u2019s just like sleepwalking, but it\u2019s called sleep-eating.",
                        "ja": "\u79c1\u306f\u3001\u5bdd\u306a\u304c\u3089\u98df\u3079\u308b\u306e\u304c\u597d\u304d\u3060\u3002\u5922\u904a\u75c5\u306e\u3088\u3046\u306a\u611f\u3058\u3067\u3001\u305d\u308c\u306f\u5922\u904a\u98df\u4e8b\u75c5\u3068\u547c\u3070\u308c\u308b\u3002",
                    },
                ],
            },
        },
    },
    {
        "word": "\u5b66\u751f",
        "forvo": {
            "success": True,
            "main_data": {
                "audio": [
                    {
                        "url": "https://apifree.forvo.com/audio/342q3o2f3f1k3n2a272l252m3631343l1k36253q3a1b2n2o1o261k322k36352g1f341b3f2p2b2p232n2m2q282c1f272l1b3e29391b3j2i3a381l313421381h3p1m1l1b1n1p1h3a3m31283h2g2b3o3q242n2q3l2m39371t1t_351f233i313l2l3b2h223k3q3d1o3d223p3d1k3i2h211t1t",
                        "username": "akiko",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/3i2g2h252q1l3h3j2c2o1f321i2l223a1k373n1f3h1l1o2c1i3g2l35393c3g2j293q2h3l3k3g252m212b1g2j212g3p373h382k3k263d2k27262j2h3m352n1f1b3b3b333a272i34362e3k372a2q2c3737383e1k1n3f2h1t1t_1p3g1m2a382j2f2p1i32353p3k2o312n2h343e2d3m3n1t1t",
                        "username": "Emmacaron",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/3c333e3g3g3l243f212o1k3a38222b1p1g311g3n3i2h262j2h1n212e2q2g3d2e2g3g3c2h3e2m1o2h3f332l3b1k373f1p3g271o26323l24372l1h252h1m353o253q3m233j2i373p3o3p3d1l2d1j1f271k38381n313c371t1t_3m3k3e3k273l262f3a1h3n3i1p2p2a3q2h3j3m1n3h371t1t",
                        "username": "yasuo",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/292p3b363h2o3i2b3i243e363l2k3725353e2p2a3q333l1j33292k3o1b1j233m2q2h3i2f3n323j372b393b2p2d341b37372i3d3p1k253l2o1m1o3n383l262239_2k32232a2f3m273m2j1p362d1f25383n1g262c3k2o2h1t1t",
                        "username": "strawberrybrown",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/2m2k1m1m3b2628291k2e2f3f331f1f291l3n1n333k1h2g2m1g1l292a2j242e2927352m1m1m2c221f2d1o352c3g2k2125253i362l3l263q3c2a1p3f2a2a2d3f3h_2j1b3g27252q1i2m383d2f391h38362b23383h233d211t1t",
                        "username": "chiharu",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/312a1l3o31233p2e3l2n2a3e1h3926223m1o3h1j3234312o2g253i3h2m2q2c1o3n263m2a2j2k3f2k2n2l3j1g3e1k3b1m3l2b2c3d272l3g2l2p2b3p3m2q333d2k_211k2b2o2b3q313i1k3p2l2f2k3g1i3g3h3j2n2i1j371t1t",
                        "username": "le_temps_perdu",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/242n331g243m37293q3a2p1o332e1k3h2c3i39382a2f2q2b1o312l2p2f2p333q3m242p1n3c3p3534383d293e29223d1h3a3h2h1p3m3p1o1n26393b2a3o251o2g_1g1k2f2c2929212a381h2o2j1i1j233j3q23292g293n1t1t",
                        "username": "Pantera3",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/323b2a2h3c393c3h311p2d331b391f3a2a2d39251g2g1k3k3g3l3g2235263n1j3e2c223e2g3j1l262g213k3o393e2m3m2b2d2l3j3f2h1b311h22383h271k1h32_2m2121361i233p322k213j322h3f2g26321m342l3n371t1t",
                        "username": "erika1993",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/3l1h392o1i262q213d3a2n1k2f1k3e242l2b3824343h1m3q242k233k3a3j381h221o3e3k1o24363k2d3p273g39322f3o283c2n1i273n1p3l3l321m3p3e3h3b23_2p3n39363m1n2b353e1p3c3p211k3o3d1l1g3e3829371t1t",
                        "username": "monekuson",
                    },
                    {
                        "url": "https://apifree.forvo.com/audio/351h2n2p3g2f2m2c222d2433282b2o1i3m3g392q2a2e2l1k3q2p2e3g373i2b3q3a3f3o1j3922243a3p3k1l3a1f3e342k2d28212o3m3h1g36291g3l1n1j2m2p1f_3m26211g2i353j3j3g233o1k223f3l353b1k372j2c211t1t",
                        "username": "poyotan",
                    },
                ]
            },
        },
        "jisho": {
            "success": True,
            "main_data": {
                "results": [
                    {
                        "slug": "\u5b66\u751f",
                        "is_common": True,
                        "tags": ["wanikani5"],
                        "jlpt": ["jlpt-n5"],
                        "japanese": [
                            {
                                "word": "\u5b66\u751f",
                                "reading": "\u304c\u304f\u305b\u3044",
                            }
                        ],
                        "senses": [
                            {
                                "english_definitions": [
                                    "student (esp. a university student)"
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
                        "attribution": {
                            "jmdict": True,
                            "jmnedict": False,
                            "dbpedia": False,
                        },
                    },
                    {
                        "slug": "\u5b66\u751f-1",
                        "is_common": False,
                        "tags": [],
                        "jlpt": [],
                        "japanese": [
                            {
                                "word": "\u5b66\u751f",
                                "reading": "\u304c\u304f\u3057\u3087\u3046",
                            },
                            {
                                "word": "\u5b66\u751f",
                                "reading": "\u304c\u304f\u305d\u3046",
                            },
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
                        "attribution": {
                            "jmdict": True,
                            "jmnedict": False,
                            "dbpedia": False,
                        },
                    },
                ],
                "extra": [
                    {
                        "slug": "\u5b66\u751f\u6642\u4ee3",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u6642\u4ee3",
                                "reading": "\u304c\u304f\u305b\u3044\u3058\u3060\u3044",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u904b\u52d5",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u904b\u52d5",
                                "reading": "\u304c\u304f\u305b\u3044\u3046\u3093\u3069\u3046",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u751f\u6d3b",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u751f\u6d3b",
                                "reading": "\u304c\u304f\u305b\u3044\u305b\u3044\u304b\u3064",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u4f1a",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u4f1a",
                                "reading": "\u304c\u304f\u305b\u3044\u304b\u3044",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u670d",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u670d",
                                "reading": "\u304c\u304f\u305b\u3044\u3075\u304f",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u8a3c",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u8a3c",
                                "reading": "\u304c\u304f\u305b\u3044\u3057\u3087\u3046",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u4f1a\u9928",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u4f1a\u9928",
                                "reading": "\u304c\u304f\u305b\u3044\u304b\u3044\u304b\u3093",
                            }
                        ],
                    },
                    {
                        "slug": "\u5b66\u751f\u5272\u5f15",
                        "japanese": [
                            {
                                "word": "\u5b66\u751f\u5272\u5f15",
                                "reading": "\u304c\u304f\u305b\u3044\u308f\u308a\u3073\u304d",
                            },
                            {
                                "word": "\u5b66\u751f\u5272\u5f15\u304d",
                                "reading": "\u304c\u304f\u305b\u3044\u308f\u308a\u3073\u304d",
                            },
                            {
                                "word": "\u5b66\u751f\u5272\u308a\u5f15\u304d",
                                "reading": "\u304c\u304f\u305b\u3044\u308f\u308a\u3073\u304d",
                            },
                        ],
                    },
                ],
            },
        },
        "ojad": {
            "success": True,
            "main_data": {"accent": ["\u304c\u304f\u305b\u3044"]},
        },
        "suzuki": {
            "success": True,
            "main_data": {"accent": ["\u304c\u304f\u305b\u3044"]},
        },
        "wadoku": {
            "success": True,
            "main_data": {"accent": ["\u304c\u304f\u305b\u3044"]},
        },
        "wanikani": {
            "success": True,
            "main_data": {
                "audio": [
                    {
                        "url": "https://files.wanikani.com/g2cqz8n0yfcy4n0d45sheojq064j",
                        "metadata": {
                            "gender": "male",
                            "source_id": 9511,
                            "pronunciation": "\u304c\u304f\u305b\u3044",
                            "voice_actor_id": 2,
                            "voice_actor_name": "Kenichi",
                            "voice_description": "Tokyo accent",
                        },
                        "content_type": "audio/mpeg",
                    },
                    {
                        "url": "https://files.wanikani.com/l6jqstgdee1l55fnt9906go7fmv1",
                        "metadata": {
                            "gender": "female",
                            "source_id": 26386,
                            "pronunciation": "\u304c\u304f\u305b\u3044",
                            "voice_actor_id": 1,
                            "voice_actor_name": "Kyoko",
                            "voice_description": "Tokyo accent",
                        },
                        "content_type": "audio/mpeg",
                    },
                ],
                "sentences": [
                    {
                        "en": "Which parts will students study at home today?",
                        "ja": "\u5b66\u751f\u306f\u4eca\u65e5\u3001\u3046\u3061\u3067\u3069\u3053\u3092\u3079\u3093\u304d\u3087\u3046\u3057\u307e\u3059\u304b\u3002",
                    },
                    {
                        "en": "Do you have student discount?",
                        "ja": "\u5b66\u751f\u308f\u308a\u5f15\u3063\u3066\u3042\u308a\u307e\u3059\u304b\uff1f",
                    },
                    {
                        "en": '"We are all students of life," my dad said while farting.',
                        "ja": "\u300c\u6211\u3005\u306f\u307f\u306a\u4eba\u751f\u306e\u5b66\u751f\u3060\u3002\u300d\u3068\u8a00\u3044\u306a\u304c\u3089\u3001\u7236\u306f\u304a\u306a\u3089\u3092\u3057\u305f\u3002",
                    },
                ],
            },
        },
    },
]
