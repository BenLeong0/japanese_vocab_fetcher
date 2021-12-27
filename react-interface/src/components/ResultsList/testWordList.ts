import FullResponseItem from "../../types/FullResponseItem"
import { JishoAPIItem, JishoExtraItem } from "../../types/ResponseItemJisho"

const filteredItems: JishoAPIItem[] = [
    {
        "slug": "静か",
        "is_common": true,
        "tags": [
            "wanikani18"
        ],
        "jlpt": [
            "jlpt-n5"
        ],
        "japanese": [
            {
                "word": "静か",
                "reading": "しずか"
            },
            {
                "word": "閑か",
                "reading": "しずか"
            }
        ],
        "senses": [
            {
                "english_definitions": [
                    "quiet",
                    "silent"
                ],
                "parts_of_speech": [
                    "Na-adjective (keiyodoshi)"
                ],
                "links": [],
                "tags": [],
                "restrictions": [],
                "see_also": [],
                "antonyms": [],
                "source": [],
                "info": [],
                "sentences": [],
            },
            {
                "english_definitions": [
                    "slow",
                    "unhurried"
                ],
                "parts_of_speech": [
                    "Na-adjective (keiyodoshi)"
                ],
                "links": [],
                "tags": [],
                "restrictions": [],
                "see_also": [],
                "antonyms": [],
                "source": [],
                "info": [],
                "sentences": [],
            },
            {
                "english_definitions": [
                    "calm",
                    "peaceful"
                ],
                "parts_of_speech": [
                    "Na-adjective (keiyodoshi)"
                ],
                "links": [],
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
            "jmdict": true,
            "jmnedict": false,
            "dbpedia": false
        }
    },
]

const extraItems: JishoExtraItem[] = [
    {
        "slug": "静かに",
        "japanese": [
            {
                "word": "静かに",
                "reading": "しずかに"
            }
        ]
    },
    {
        "slug": "静かの海",
        "japanese": [
            {
                "word": "静かの海",
                "reading": "しずかのうみ"
            }
        ]
    },
    {
        "slug": "静かに流れる川は深い",
        "japanese": [
            {
                "word": "静かに流れる川は深い",
                "reading": "しずかにながれるかわはふかい"
            }
        ]
    },
    {
        "slug": "51869194d5dda7b2c601eed0",
        "japanese": [
            {
                "word": "静かなるドン",
                "reading": "",
            }
        ]
    },
    {
        "slug": "518698ead5dda7b2c60558f8",
        "japanese": [
            {
                "word": "静かな海と楽しい航海 (ベートーヴェン)",
                "reading": "",
            }
        ]
    },
    {
        "slug": "51869907d5dda7b2c60566de",
        "japanese": [
            {
                "word": "静かな海と楽しい航海",
                "reading": "",
            }
        ]
    },
    {
        "slug": "51869460d5dda7b2c6033553",
        "japanese": [
            {
                "word": "静かなる決闘",
                "reading": "",
            }
        ]
    },
    {
        "slug": "51869908d5dda7b2c60566e2",
        "japanese": [
            {
                "word": "静かな海と楽しい航海 (メンデルスゾーン)",
                "reading": "",
            }
        ]
    },
    {
        "slug": "51869d05d5dda7b2c6074a12",
        "japanese": [
            {
                "word": "静かなアメリカ人",
                "reading": "",
            }
        ]
    },
]

const testWordList: FullResponseItem[] = [
    {
        "word": "静か",
        "jisho": {
            "success": true,
            "error": null,
            "main_data": {
                "results": filteredItems,
                "extra": extraItems,
            },
        },
        "ojad": {
            "success": true,
            "error": null,
            "main_data": {
                "accent": ["し' ずか"],
            },
        },
        "suzuki": {
            "success": true,
            "error": null,
            "main_data": {
                "accent": ["し' ずか"],
            },
        },
        "wadoku": {
            "success": true,
            "error": null,
            "main_data": {
                "accent": ["し' ずか"],
            },
        },
        "forvo": {
            "success": true,
            "error": null,
            "main_data": {
                "audio": [
                    {
                        "url": ("https://apifree.forvo.com/audio/2n352q1f2n3a333a3j223i3d1o2c1p3h1k212g3k3f1l3p2b38232n2l2f1k27263j243432372f3b2q2h39213l1g282c311h263b3j2b3q2m362j3a2n1h1l363j331j2b3a37213c2j212j2e2b1o3b3i1p2k2o1m2c353i211t1t_3b1i2m373c1l242i1k373o2o362l212m3o3l2k2p3p371t1t"),
                        "username": "nohunohu",
                    },
                    {
                        "url": ("https://apifree.forvo.com/audio/3i1i352d342d2g24212b3p1k2k2c232l25262f3i3m313j3e2f2a1m1b1j222i1g1f333a1p2g2n2m32352a1n2p1f2a2d2o2j2f3e222i3i1m26281l2b1m232q3m1m1k2e263b263g3n2e2o391p1f1b2c3i1l22393434262h1t1t_1k3d1k2e333k3d3e253b292n2g1h1k2b1l1b24291g2h1t1t"),
                        "username": "JunkoHanabi",
                    },
                    {
                        "url": ("https://apifree.forvo.com/audio/232c1l28231l3n2b3q232h2b323n2q263i2i3b383d1g2n3c1m3a273e3p3q241f231b3g391i3k3q2c1j2j3k353i2g1g391i221m1b262l3h1g3f2p3g1g3b3j2g223d342c3m2c38281i33311g353j281g1g2o2b1f3n1m371t1t_2f2m3g253n28362l3j3n2k1l242g271j1p2c2a2p1m371t1t"),
                        "username": "strawberrybrown",
                    },
                    {
                        "url": ("https://apifree.forvo.com/audio/1m3f3h3m363b2l242737211h34281f1o2b37362m3b2g2k3d1j2f3n3a2o1m1g1l1i3k272k323i2k3i3139342f1h3m332i2e243m1l3c1g293232283p1g1b291p1f1k223l273b382l3c212i211l1p313m2h1l3g2g1g2b211t1t_2c21373q2q2d1j2o29211h372j1h38332l253o3g3d211t1t"),
                        "username": "straycat88",
                    },
                    {
                        "url": ("https://apifree.forvo.com/audio/362534211m1j372l1m242g243o31241n293l1p2f2a2l3l1g363428233j2a1f1l3a23352p3i2b3335263d241g36333c1k261g382l1o2e38371n1m1n23292n1g3n2p2f1f1n2d2232391l1j273j3e1i343e3j3d3i3j293n1t1t_1k233b2l332g3n2c2g2q331o2q282p3m213p3m2m3g371t1t"),
                        "username": "skent",
                    },
                ],
            },
        },
        "wanikani": {
            "success": true,
            "error": null,
            "main_data": {
                "audio": [
                    {
                        "url": ("https://files.wanikani.com/awv61bmcmf9w4m7p057jqubhu3f1"),
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
                        "url": ("https://files.wanikani.com/pkutc4gv3nxpmuo1dba6iv6p5luh"),
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
]


export default testWordList
