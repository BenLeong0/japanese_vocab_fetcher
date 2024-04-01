from api.custom_types.wanikani_api_types import WanikaniAPIResponse

MEGANE = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E7%9C%BC%E9%8F%A1",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 1,
        "data_updated_at": "2021-09-01T18:29:07.199772Z",
        "data": [
            {
                "id": 7473,
                "object": "vocabulary",
                "url": "https://api.wanikani.com/v2/subjects/7473",
                "data_updated_at": "2021-09-01T18:29:07.199772Z",
                "data": {
                    "created_at": "2014-01-15T18:54:07.400519Z",
                    "level": 34,
                    "slug": "\u773c\u93e1",
                    "hidden_at": None,
                    "document_url": "https://www.wanikani.com/vocabulary/%E7%9C%BC%E9%8F%A1",
                    "characters": "\u773c\u93e1",
                    "meanings": [
                        {
                            "meaning": "Glasses",
                            "primary": True,
                            "accepted_answer": True,
                        },
                        {
                            "meaning": "Eyeglasses",
                            "primary": False,
                            "accepted_answer": True,
                        },
                    ],
                    "auxiliary_meanings": [],
                    "readings": [
                        {
                            "primary": True,
                            "reading": "\u3081\u304c\u306d",
                            "accepted_answer": True,
                        },
                        {
                            "primary": False,
                            "reading": "\u304c\u3093\u304d\u3087\u3046",
                            "accepted_answer": True,
                        },
                    ],
                    "parts_of_speech": ["noun"],
                    "component_subject_ids": [1488, 887],
                    "meaning_mnemonic": "An <kanji>eyeball</kanji> <kanji>mirror</kanji> is something that refracts and focuses light into your eyeball in a different way so you can see better. Really, these things are glasses, not eye mirrors, but same sort of things when you get down to it. Just imagine someone wearing mirrors on their eyes, and when you ask them what those are for, they just say they're <vocabulary>glasses</vocabulary>.",
                    "reading_mnemonic": "The reading for <ja>\u773c</ja> is the same as the vocab <ja>\u773c</ja>. The reading for <ja>\u93e1</ja> is an exception, totally different. It shares a reading with <ja>\u91d1</ja> (gold), though, so think of the mirrors on the person's eyes being made of gold. What nice glasses!\r\n\r\nThis word can also be read as <ja>\u304c\u3093\u304d\u3087\u3046</ja>, but usually only on official/written documents. If you're speaking and not reading a government document, you should say <ja>\u3081\u304c\u306d</ja>!",
                    "context_sentences": [
                        {
                            "en": "You should wipe your glasses.",
                            "ja": "\u773c\u93e1\u3092\u62ed\u3044\u305f\u65b9\u304c\u3044\u3044\u3067\u3059\u3088\u3002",
                        }
                    ],
                    "pronunciation_audios": [
                        {
                            "url": "https://files.wanikani.com/ygcfayxwdm196h77g0cltvcs45nz",
                            "metadata": {
                                "gender": "male",
                                "source_id": 7771,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/11v648aiw4875mqspzrpn98ly07e",
                            "metadata": {
                                "gender": "male",
                                "source_id": 7771,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                        {
                            "url": "https://files.wanikani.com/hoiygkrxyq7a43jujw1skqzla3mx",
                            "metadata": {
                                "gender": "female",
                                "source_id": 24645,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                        {
                            "url": "https://files.wanikani.com/0ocjnicpw3r8i0qnur5g9vkgcqdt",
                            "metadata": {
                                "gender": "female",
                                "source_id": 24645,
                                "pronunciation": "\u3081\u304c\u306d",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                    ],
                    "lesson_position": 152,
                    "spaced_repetition_system_id": 1,
                },
            }
        ],
    }
)
COMEBACK = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E3%82%AB%E3%83%A0%E3%83%90%E3%83%83%E3%82%AF",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 0,
        "data_updated_at": None,
        "data": [],
    }
)
TABERU_GAKUSEI = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E9%A3%9F%E3%81%B9%E3%82%8B%2C%E5%AD%A6%E7%94%9F",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 2,
        "data_updated_at": "2021-09-10T15:38:03.085842Z",
        "data": [
            {
                "id": 2788,
                "object": "vocabulary",
                "url": "https://api.wanikani.com/v2/subjects/2788",
                "data_updated_at": "2021-09-01T18:23:08.222451Z",
                "data": {
                    "created_at": "2012-03-06T08:23:37.000000Z",
                    "level": 5,
                    "slug": "\u5b66\u751f",
                    "hidden_at": None,
                    "document_url": "https://www.wanikani.com/vocabulary/%E5%AD%A6%E7%94%9F",
                    "characters": "\u5b66\u751f",
                    "meanings": [
                        {"meaning": "Student", "primary": True, "accepted_answer": True}
                    ],
                    "auxiliary_meanings": [],
                    "readings": [
                        {
                            "primary": True,
                            "reading": "\u304c\u304f\u305b\u3044",
                            "accepted_answer": True,
                        }
                    ],
                    "parts_of_speech": ["noun"],
                    "component_subject_ids": [599, 850],
                    "meaning_mnemonic": "Who has a <kanji>study</kanji> <kanji>life</kanji>? Only one person that I know of, and that's a <vocabulary>student</vocabulary>.",
                    "reading_mnemonic": "This is a jukugo word, which usually means on'yomi readings from the kanji. If you know the readings of your kanji you'll know how to read this as well.",
                    "context_sentences": [
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
                    "pronunciation_audios": [
                        {
                            "url": "https://files.wanikani.com/9j93ot0hyg1jxvtjskyc9y4l9tbt",
                            "metadata": {
                                "gender": "male",
                                "source_id": 9511,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/1jl4g2it86iwc9h5z31ver21gj65",
                            "metadata": {
                                "gender": "female",
                                "source_id": 26386,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/webm",
                        },
                        {
                            "url": "https://files.wanikani.com/3vmxruxi6z97jbj6fg20rolb8vn5",
                            "metadata": {
                                "gender": "male",
                                "source_id": 9511,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/webm",
                        },
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
                        {
                            "url": "https://files.wanikani.com/0hl7aqs7ltyfr961e2iqef54ptpt",
                            "metadata": {
                                "gender": "female",
                                "source_id": 26386,
                                "pronunciation": "\u304c\u304f\u305b\u3044",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                    ],
                    "lesson_position": 117,
                    "spaced_repetition_system_id": 1,
                },
            },
            {
                "id": 2923,
                "object": "vocabulary",
                "url": "https://api.wanikani.com/v2/subjects/2923",
                "data_updated_at": "2021-09-10T15:38:03.085842Z",
                "data": {
                    "created_at": "2012-03-09T00:55:33.000000Z",
                    "level": 6,
                    "slug": "\u98df\u3079\u308b",
                    "hidden_at": None,
                    "document_url": "https://www.wanikani.com/vocabulary/%E9%A3%9F%E3%81%B9%E3%82%8B",
                    "characters": "\u98df\u3079\u308b",
                    "meanings": [
                        {"meaning": "To Eat", "primary": True, "accepted_answer": True}
                    ],
                    "auxiliary_meanings": [
                        {"type": "whitelist", "meaning": "To Eat Something"}
                    ],
                    "readings": [
                        {
                            "primary": True,
                            "reading": "\u305f\u3079\u308b",
                            "accepted_answer": True,
                        }
                    ],
                    "parts_of_speech": ["transitive verb", "ichidan verb"],
                    "component_subject_ids": [644],
                    "meaning_mnemonic": "This word consists of kanji with hiragana attached. Because the hiragana ends with an <ja>\u3046</ja> sound, you know this word is a verb. The kanji itself means <kanji>eat</kanji> so the verb version is <vocabulary>to eat</vocabulary>.",
                    "reading_mnemonic": "You have to remember the <ja>\u305f</ja> portion if you want to be able to read this word, which uses the kun'yomi reading. Think about yourself <vocabulary>eat</vocabulary>ing some <reading>ta</reading>cos (<ja>\u305f</ja>). Imagine yourself eating it, that raw beef taste in your mouth (either like it or hate it).",
                    "context_sentences": [
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
                    "pronunciation_audios": [
                        {
                            "url": "https://files.wanikani.com/nzwdishihsa9bhbrbis5sdw5y910",
                            "metadata": {
                                "gender": "female",
                                "source_id": 27468,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
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
                            "url": "https://files.wanikani.com/0tvy97ky5i4swyudop7y0k1e47kp",
                            "metadata": {
                                "gender": "male",
                                "source_id": 10592,
                                "pronunciation": "\u305f\u3079\u308b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
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
                    "lesson_position": 0,
                    "spaced_repetition_system_id": 1,
                },
            },
        ],
    }
)
KOTOBA = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E8%A8%80%E8%91%89",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 1,
        "data_updated_at": "2021-09-01T18:29:08.596245Z",
        "data": [
            {
                "id": 7492,
                "object": "vocabulary",
                "url": "https://api.wanikani.com/v2/subjects/7492",
                "data_updated_at": "2021-09-01T18:29:08.596245Z",
                "data": {
                    "created_at": "2014-02-11T00:38:00.298590Z",
                    "level": 12,
                    "slug": "\u8a00\u8449",
                    "hidden_at": None,
                    "document_url": "https://www.wanikani.com/vocabulary/%E8%A8%80%E8%91%89",
                    "characters": "\u8a00\u8449",
                    "meanings": [
                        {"meaning": "Word", "primary": True, "accepted_answer": True},
                        {
                            "meaning": "Language",
                            "primary": False,
                            "accepted_answer": True,
                        },
                        {
                            "meaning": "Manner Of Speech",
                            "primary": False,
                            "accepted_answer": True,
                        },
                    ],
                    "auxiliary_meanings": [],
                    "readings": [
                        {
                            "primary": True,
                            "reading": "\u3053\u3068\u3070",
                            "accepted_answer": True,
                        }
                    ],
                    "parts_of_speech": ["noun"],
                    "component_subject_ids": [593, 750],
                    "meaning_mnemonic": "A <kanji>leaf</kanji> of the things you <kanji>say</kanji> is like a leaf from a tree of speaking. That leaf is a part of the whole language, it is a single <vocabulary>word</vocabulary>, though it can add up to be a <vocabulary>language</vocabulary> or <vocabulary>manner of speech</vocabulary>.",
                    "reading_mnemonic": "The reading for <ja>\u8a00</ja> is one you haven't learned. It's kind of an exception, in fact, though you might see it from time to time. You'll want to imagine yourself playing a <reading>koto</reading> (<ja>\u3053\u3068</ja>). Each strum of the instrument sends forth several <vocabulary>word</vocabulary>s from its strings, flying at the person you're talking to. You speak your <vocabulary>word</vocabulary>s via music, specifically the koto (so think about using other instruments as well to communicate... they just don't work).",
                    "context_sentences": [
                        {
                            "en": "I'd like to hire elves if I could, but It's difficult because of the language barrier.",
                            "ja": "\u30a8\u30eb\u30d5\u3092\u3084\u3068\u3044\u305f\u3044\u306e\u306f\u5c71\u3005\u306a\u3093\u3067\u3059\u304c\u3001\u8a00\u8449\u306e\u304b\u3079\u304c\u3042\u308b\u306e\u3067\u3080\u305a\u304b\u3057\u3044\u3093\u3067\u3059\u3088\u3002",
                        },
                        {
                            "en": "It's hard to put into words, but Koichi is a very special person to me.",
                            "ja": "\u3046\u307e\u304f\u8a00\u8449\u306b\u3067\u304d\u306a\u3044\u3051\u3069\u3001\u30b3\u30a6\u30a4\u30c1\u306f\u308f\u305f\u3057\u306b\u3068\u3063\u3066\u3059\u3054\u304f\u7279\u5225\u306a\u4eba\u306a\u306e\u3002",
                        },
                        {
                            "en": "I was at a loss for words.",
                            "ja": "\u79c1\u306f\u8a00\u8449\u306b\u8a70\u307e\u3063\u305f\u3002",
                        },
                    ],
                    "pronunciation_audios": [
                        {
                            "url": "https://files.wanikani.com/li1f7xje2r4aj3fckuledg0ur1yu",
                            "metadata": {
                                "gender": "male",
                                "source_id": 3170,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/n7d4o8yizz9oni6whnw5m5ormof7",
                            "metadata": {
                                "gender": "male",
                                "source_id": 3170,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                        {
                            "url": "https://files.wanikani.com/07386jhwg98fqg3z9prvdf7n7xr6",
                            "metadata": {
                                "gender": "female",
                                "source_id": 22011,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                        {
                            "url": "https://files.wanikani.com/n4segh47y31wg1k4rpemplsg50q8",
                            "metadata": {
                                "gender": "female",
                                "source_id": 22011,
                                "pronunciation": "\u3053\u3068\u3070",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                    ],
                    "lesson_position": 165,
                    "spaced_repetition_system_id": 1,
                },
            }
        ],
    }
)
BADINPUT = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=BADINPUT",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 0,
        "data_updated_at": None,
        "data": [],
    }
)
USAGI_IKU_KAGO = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E5%85%8E%2C%E8%A1%8C%E3%81%8F%2C%E7%B1%A0",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 1,
        "data_updated_at": "2021-09-01T18:23:07.158937Z",
        "data": [
            {
                "id": 2775,
                "object": "vocabulary",
                "url": "https://api.wanikani.com/v2/subjects/2775",
                "data_updated_at": "2021-09-01T18:23:07.158937Z",
                "data": {
                    "created_at": "2012-03-06T08:21:22.000000Z",
                    "level": 5,
                    "slug": "\u884c\u304f",
                    "hidden_at": None,
                    "document_url": "https://www.wanikani.com/vocabulary/%E8%A1%8C%E3%81%8F",
                    "characters": "\u884c\u304f",
                    "meanings": [
                        {"meaning": "To Go", "primary": True, "accepted_answer": True}
                    ],
                    "auxiliary_meanings": [],
                    "readings": [
                        {
                            "primary": True,
                            "reading": "\u3044\u304f",
                            "accepted_answer": True,
                        }
                    ],
                    "parts_of_speech": ["intransitive verb", "godan verb"],
                    "component_subject_ids": [580],
                    "meaning_mnemonic": "This word consists of kanji with hiragana attached. Because the hiragana ends with an <ja>\u3046</ja> sound, you know this word is a verb. The kanji itself means <kanji>go</kanji> so the verb form of this is <vocabulary>to go</vocabulary>.",
                    "reading_mnemonic": "Since this word consists of a kanji with hiragana attached, you can bet that it will use the kun'yomi reading. You didn't learn that reading with this kanji, so here's a mnemonic to help you: \r\n\r\nYou have to remember the <ja>\u3044</ja> portion. To remember <ja>\u3044</ja> we use the word \"eagle.\" \r\n\r\nYou want <vocabulary>to go</vocabulary> somewhere (anywhere!) but you can't. An <reading>ea</reading>gle (<ja>\u3044</ja>) blocks your path. You try to go forward and it opens its wings and bites at you. You try to go back and it jumps at you. There's nowhere for you to go with this eagle standing there.",
                    "context_sentences": [
                        {
                            "en": "I'm about to go shopping. ",
                            "ja": "\u4eca\u304b\u3089\u3001\u304b\u3044\u3082\u306e\u306b\u884c\u304d\u307e\u3059\u3002",
                        },
                        {
                            "en": "Something came up, so I'm not able to make it.",
                            "ja": "\u3088\u3046\u3058\u304c\u3067\u304d\u3066\u3001\u884c\u3051\u306a\u304f\u306a\u3063\u3066\u3057\u307e\u3044\u307e\u3057\u305f\u3002",
                        },
                        {
                            "en": "I wouldn\u2019t want to go to Mars because they don\u2019t have Taco Bell there.",
                            "ja": "\u30bf\u30b3\u30d9\u30eb\u304c\u7121\u3044\u306e\u3067\u706b\u661f\u306b\u306f\u884c\u304d\u305f\u304f\u306a\u3044\u3002",
                        },
                    ],
                    "pronunciation_audios": [
                        {
                            "url": "https://files.wanikani.com/97jii1wcxrcejphvlgcf5l4ftb7t",
                            "metadata": {
                                "gender": "female",
                                "source_id": 26344,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/webm",
                        },
                        {
                            "url": "https://files.wanikani.com/j5tv5z01h9nzywtes41wxyd8jcyn",
                            "metadata": {
                                "gender": "male",
                                "source_id": 9469,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/webm",
                        },
                        {
                            "url": "https://files.wanikani.com/i6eq7alp4yn38qsxvlh51ur9sl41",
                            "metadata": {
                                "gender": "male",
                                "source_id": 9469,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                        {
                            "url": "https://files.wanikani.com/x1hzhorchfu9u6qo6h468k9x25cm",
                            "metadata": {
                                "gender": "male",
                                "source_id": 9469,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/uwpun79j5c1fmcogip1ltddlrc69",
                            "metadata": {
                                "gender": "female",
                                "source_id": 26344,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/9wwn90yd3wpl8s9fn3vzf643fm62",
                            "metadata": {
                                "gender": "female",
                                "source_id": 26344,
                                "pronunciation": "\u3044\u304f",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                    ],
                    "lesson_position": 104,
                    "spaced_repetition_system_id": 1,
                },
            }
        ],
    }
)
SHIZUKA = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E9%9D%99%E3%81%8B",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 1,
        "data_updated_at": "2021-09-01T18:25:04.520228Z",
        "data": [
            {
                "id": 4155,
                "object": "vocabulary",
                "url": "https://api.wanikani.com/v2/subjects/4155",
                "data_updated_at": "2021-09-01T18:25:04.520228Z",
                "data": {
                    "created_at": "2012-11-01T00:29:55.227214Z",
                    "level": 18,
                    "slug": "\u9759\u304b",
                    "hidden_at": None,
                    "document_url": "https://www.wanikani.com/vocabulary/%E9%9D%99%E3%81%8B",
                    "characters": "\u9759\u304b",
                    "meanings": [
                        {"meaning": "Quiet", "primary": True, "accepted_answer": True}
                    ],
                    "auxiliary_meanings": [],
                    "readings": [
                        {
                            "primary": True,
                            "reading": "\u3057\u305a\u304b",
                            "accepted_answer": True,
                        }
                    ],
                    "parts_of_speech": ["\u306a adjective"],
                    "component_subject_ids": [1052],
                    "meaning_mnemonic": "This is the <ja>\u306a</ja> adjective form of <kanji>quiet</kanji>, which is kind of just like the noun, anyways. What is the adjective version of quiet? It's also <vocabulary>quiet</vocabulary>.",
                    "reading_mnemonic": "Since this word consists of a kanji with hiragana attached, you can bet that it will use the kun'yomi reading. You didn't learn that reading with this kanji, so here's a mnemonic to help you: You need to be <vocabulary>quiet</vocabulary>. <reading>She's</reading> (<ja>\u3057\u305a</ja>) being nice and quiet, unlike you!",
                    "context_sentences": [
                        {
                            "en": "We'd prefer a house on a quiet street.",
                            "ja": "\u9759\u304b\u306a\u901a\u308a\u306b\u3042\u308b\u5bb6\u306e\u65b9\u304c\u3044\u3044\u3067\u3059\u3002",
                        },
                        {
                            "en": "I know you have diarrhea, but could you keep it down a bit more, please?",
                            "ja": "\u4e0b\u308a\u306a\u306e\u306f\u5206\u304b\u308a\u307e\u3059\u304c\u3001\u3082\u3046\u5c11\u3057\u9759\u304b\u306b\u3057\u3066\u3044\u305f\u3060\u3051\u307e\u3059\u304b\uff1f",
                        },
                        {
                            "en": "When Koichi and Viet got in, the taxi quietly started to move.",
                            "ja": "\u30b3\u30a6\u30a4\u30c1\u3068\u30d3\u30a8\u30c8\u304c\u4e57\u308a\u8fbc\u3080\u3068\u3001\u305d\u306e\u30bf\u30af\u30b7\u30fc\u306f\u9759\u304b\u306b\u52d5\u304d\u51fa\u3057\u305f\u3002",
                        },
                    ],
                    "pronunciation_audios": [
                        {
                            "url": "https://files.wanikani.com/i36tvzolpod2ha84cv8yz62karzv",
                            "metadata": {
                                "gender": "male",
                                "source_id": 4367,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/awv61bmcmf9w4m7p057jqubhu3f1",
                            "metadata": {
                                "gender": "male",
                                "source_id": 4367,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 2,
                                "voice_actor_name": "Kenichi",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                        {
                            "url": "https://files.wanikani.com/l6u3b9trefpzvyfd04ja42zvwehv",
                            "metadata": {
                                "gender": "female",
                                "source_id": 22694,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/ogg",
                        },
                        {
                            "url": "https://files.wanikani.com/pkutc4gv3nxpmuo1dba6iv6p5luh",
                            "metadata": {
                                "gender": "female",
                                "source_id": 22694,
                                "pronunciation": "\u3057\u305a\u304b",
                                "voice_actor_id": 1,
                                "voice_actor_name": "Kyoko",
                                "voice_description": "Tokyo accent",
                            },
                            "content_type": "audio/mpeg",
                        },
                    ],
                    "lesson_position": 134,
                    "spaced_repetition_system_id": 1,
                },
            }
        ],
    }
)
NARU = WanikaniAPIResponse.model_validate(
    {
        "object": "collection",
        "url": "https://api.wanikani.com/v2/subjects?slugs=%E3%81%AA%E3%82%8B&types=vocabulary",
        "pages": {"per_page": 1000, "next_url": None, "previous_url": None},
        "total_count": 0,
        "data_updated_at": None,
        "data": [],
    }
)
