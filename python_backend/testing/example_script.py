import json
import requests


API_URL = "http://localhost:5000/words"
payload = {'words': ["食べる", "学生"]}
result = requests.get(API_URL, data=json.dumps(payload))
pretty_result = json.dumps(json.loads(result.text), indent=4)
print(pretty_result)

example_response = [
    {
        "word": "\u98df\u3079\u308b",
        "jisho": {},
        "accent": {
            "ojad": [
                "\u305f\u3079' \u308b"
            ],
            "suzuki": [
                "\u305f\u3079' \u308b"
            ],
            "wadoku": [
                "\u305f\u3079' \u308b"
            ]
        },
        "audio": {
            "forvo": [
                "https://apifree.forvo.com/audio/2n1l2e2p1f2f3o392e323n342a392f352d1b333i2k392738243h3j2m2p1m1p241j361h3m333b1p2521212q2b371i1i2m3d2q1k2p253i2j3c233q2b3c2723242l2b28221k2k2n283i2n24242j29283e2c1m2e3q3f1b3n1t1t_1p1o312h251h3b34232q1g292d1o2831343k3m2p3m371t1t",
                "https://apifree.forvo.com/audio/3n3o333c2o3n2p38381m1i1n1j2a3b3l2f2h3h222h3n211p1h2k373831273a3g31272b331n3g352c3g1k2j2f1h361n3i2923363h383e3638221h1j3j2l3i3p1o_3a3e1l1n343f311g1l282a323o3d3d1o3m3a2o1l1k3n1t1t",
                "https://apifree.forvo.com/audio/3l1o1h293i2h1k323g2e1h2m2b353c1g2a1o2p393f1k39232i2a3o1g1i3p1b1k3b352l29383j36221i3d3m2j2e2n1g3k211l2b3q2f3i2k2m3i3p3d2c3k2e1i1f_333a221o271m241o3e3p3g1h1m2l2h233a3e1i2p1g2h1t1t",
                "https://apifree.forvo.com/audio/2n3n1l1f253421243g1o2d3b323k1j272c3b2f2q1f1h2f283h3f1m393a3e1i393k273h1n3g2j2q1g27322m1b333h3c363m29262c3m1j333a382c2l2i2m2a3f26_272n3g262o2g2p2m1j1p3g3q1k2k3k2a311h212631211t1t",
                "https://apifree.forvo.com/audio/332m341n1f1o1l3j3g322g3f222n3q3o3g3a2f2k1o2o1m2d2c2k3n2q1b1j2m3i1o3f2g3j1j3h1i3o26282j2g1n3p1p363o3q1n1j2j222f2a1f262h2b3j1k3b2f_1b2c353p332a1l292b1g262i262n261h3f281k1l2m3n1t1t",
                "https://apifree.forvo.com/audio/3h312i342o1h3k211h1j3l2h373q29263e1j223h3n3l2a1n27222q2d243b343637212d3j1h1o223g36253h1o3n372e281m272d223o1g2p2f2m2n3e363331353l_38283j3a1j3f263h2b3o242c1k3l2j2a3b331o3f273n1t1t",
                "https://apifree.forvo.com/audio/1j2o2q1i241b2g1n1f1k242l3a3a3c1j37343g2g3k3a25383b233j2p21393a3o1i2l32382h3o1i262p2h1p391p3c1o2c3h3k1h2l1f2h3i1l3e1g3h3d1h2e213q_21372a262q2o1j292h2q1h281h3e251i233f1l2h37211t1t",
                "https://apifree.forvo.com/audio/3j2j3g2n3c2l3k223j3f1o343q1i2j2q2f1i2j1m263c2j2a2m1k3f2f3d3k3n2b3e342g391o2b342k3g25352q3k293d3f3p343c212j1b3m1m213g2p2921221p2h_3p33251f2q3i1o1o292m3h1b2m3o3737241g273l1i211t1t",
                "https://apifree.forvo.com/audio/3p1j1p2j3i23381h2d242i262b1n222p1l2o3q1g3834262n1o2h3g232d2q38331m273m3f253j343d311m212h1p3n2p3a2m1k2h3c2i382i2922341o372a2n3b2j_2j3f3p2c3p3j2829391h3j292k3a3h3k3a1b272l32371t1t",
                "https://apifree.forvo.com/audio/1l1m3e2e1p382i3k3b381l2e2g2k3q331n1f2o331k2b2k2h33353e2734321k2f3a2j2g1k1o3p39372e3p382q3i232b2k1h2127381b1i2c24343d2n2p1b3o3725_1o1l223p322l323c1k2o3j3a272f1f28252b232e2p2h1t1t"
            ],
            "wanikani": {
                "audio": [
                    {
                        "url": "https://files.wanikani.com/8e5vf9sc17iajyx2d3838oi6chnh",
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
                        "url": "https://files.wanikani.com/ng81br3v7kwq5ybljgadillfzqay",
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
                        "ja": "\u6bce\u3042\u3055\u3001\u306a\u3063\u3068\u3046\u3092\u98df\u3079\u307e\u3059\u3002"
                    },
                    {
                        "en": "I never have enough time to eat healthy foods.",
                        "ja": "\u3044\u3064\u3082\u3001\u3051\u3093\u3053\u3046\u306b\u3044\u3044\u3082\u306e\u3092\u98df\u3079\u308b\u3058\u304b\u3093\u304c\u306a\u3044\u3093\u3067\u3059\u3002"
                    },
                    {
                        "en": "I like to eat while I\u2019m sleeping. It\u2019s just like sleepwalking, but it\u2019s called sleep-eating.",
                        "ja": "\u79c1\u306f\u3001\u5bdd\u306a\u304c\u3089\u98df\u3079\u308b\u306e\u304c\u597d\u304d\u3060\u3002\u5922\u904a\u75c5\u306e\u3088\u3046\u306a\u611f\u3058\u3067\u3001\u305d\u308c\u306f\u5922\u904a\u98df\u4e8b\u75c5\u3068\u547c\u3070\u308c\u308b\u3002"
                    }
                ]
            }
        }
    },
    {
        "word": "\u5b66\u751f",
        "jisho": {},
        "accent": {
            "ojad": [
                "\u304c\u304f\u305b\u3044"
            ],
            "suzuki": [
                "\u304c\u304f\u305b\u3044"
            ],
            "wadoku": [
                "\u304c\u304f\u305b\u3044"
            ]
        },
        "audio": {
            "forvo": [
                "https://apifree.forvo.com/audio/2o333h233m342k1j313a3i2c3j1j2e3b2b211i2m2o3c362l2f2e3j253f1b3o323q3n223e1k2c2n3b332f1o2e25212o2g3h1p3j2k352327252n1b251f1h3k2b39272c2l263e281h1i2j1b37352n3d1j3f1f271o281p211t1t_2d3c3b2b241n3f23262a2e3q3g3o3o282l2q282d2m3n1t1t",
                "https://apifree.forvo.com/audio/342p3q2a3i1f2i2d2n222h1i382h1l313f2e2b2p1m1f2h3e292o2k3o2k342l262g3l361i1i3l233f1j2n2a2j382n1m222n1h3n2p3n222i253i33373425322n3p1n1b2k2l3m22373g2b3e1j3d3d2f2p2c3i2b1j3g1i211t1t_3j1b3e352e2c31262b31362a2a3g291i3j3l3f2q31371t1t",
                "https://apifree.forvo.com/audio/1h2l391h2q2g381o3h2f1i1p251l3p1j353d2333291m2d321o1o2h252i35333d3i3g322b1o2e3n2h2n2g2k1f1p1g2l2q243h2m3d3g382f28353m323m372i3j3i3g2i2p3g3b2q212b221o3i2j2535223a2e28213p1h2h1t1t_1f2q2p232c35252o2k311h363o3f2j1j1b1h1k3b3o2h1t1t",
                "https://apifree.forvo.com/audio/3o212e1p1i34321o2b2d222j2g2i323p1k2d1p2l2b2m391b392i351j2m1n1f3i262b1n2p2b25353m3p3k1j3f2q3m251k3b1l2p1n1i1b232e1i3e3o1j3a1j2a1o_371i1f3g281j262k282l2i3n223632233g231o1p1n211t1t",
                "https://apifree.forvo.com/audio/3n3m211l3q1p2e2n25263m3521351l2h1b1j1g2n3f2i3e3j3m2e1k21392g1p2d2b3e1p1i2h1m2b352j1b1n352i2b2j1f313h3n1j3f3i291h3g3i1h3a1p2i1o1n_3b3d2c3h2p3k1h1n341n1k2b2a2b24253j3g3i2e1n3n1t1t",
                "https://apifree.forvo.com/audio/38353l2l212l353g2f1n38281g251k1i2e3e3p343i3k251f263l25212f3g2f1h2e253e1f1l1o2f381l2p2q1o1o3n1m1j3a2i3i382q2g1j22363h3j3m3c2l1i2j_3d3c2b222l2c1k362q263o211l1b2f221j321f3627211t1t",
                "https://apifree.forvo.com/audio/1n1l1g1o242g3i3m2p363o352429222q2q2q263o2e1l1g1j1m1j1o2b1g21351l392h1l3g2d241o3d3g3n3h3m1h3a293c332m32373l3m3135271h2k342j212f27_2m3q2c2j3q1l31212k2l32212c3l223b1n36341f32211t1t",
                "https://apifree.forvo.com/audio/372h2o2e3p3c2n211j2q243d1l2m2l3i3b3d3h242c1b222h2c1m1j2g242k3n3n2a34351p2p363b1n211o2a2c2d1h323q372l1b28262o3l353n1p3g351f3h2d23_323m2g3e1o3g3p1h281o3j363e2o1n2o1i1g1f1i343n1t1t",
                "https://apifree.forvo.com/audio/2f2429393d341j2l363i2e273m37393k3m2f27293b1i373126383428272d281i2c2m352g333m1h1n3q1n1j2f3o3f39373l3n1f3h1k1n261g3g3n2f3q233h3q3b_2h1o2j3e3c2m2n3q3i27292o1p2l2e2b1h3h2k2c1f2h1t1t",
                "https://apifree.forvo.com/audio/3g1o2h3q1n3c3c3q1g1m221p3a283j3m3j3l3f2o2n1n3k2a2j2f213m3i2n372q1f35233m3124353m3d393f1j3l2k3j1i3h1f3n2e2k321j271o253a3l232d3f2m_291k3m342q25332p3m2c2422232h2i361o211g323g371t1t"
            ],
            "wanikani": {
                "audio": [
                    {
                        "url": "https://files.wanikani.com/g2cqz8n0yfcy4n0d45sheojq064j",
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
                        "url": "https://files.wanikani.com/l6jqstgdee1l55fnt9906go7fmv1",
                        "metadata": {
                            "gender": "female",
                            "source_id": 26386,
                            "pronunciation": "\u304c\u304f\u305b\u3044",
                            "voice_actor_id": 1,
                            "voice_actor_name": "Kyoko",
                            "voice_description": "Tokyo accent"
                        },
                        "content_type": "audio/mpeg"
                    }
                ],
                "sentences": [
                    {
                        "en": "Which parts will students study at home today?",
                        "ja": "\u5b66\u751f\u306f\u4eca\u65e5\u3001\u3046\u3061\u3067\u3069\u3053\u3092\u3079\u3093\u304d\u3087\u3046\u3057\u307e\u3059\u304b\u3002"
                    },
                    {
                        "en": "Do you have student discount?",
                        "ja": "\u5b66\u751f\u308f\u308a\u5f15\u3063\u3066\u3042\u308a\u307e\u3059\u304b\uff1f"
                    },
                    {
                        "en": "\"We are all students of life,\" my dad said while farting.",
                        "ja": "\u300c\u6211\u3005\u306f\u307f\u306a\u4eba\u751f\u306e\u5b66\u751f\u3060\u3002\u300d\u3068\u8a00\u3044\u306a\u304c\u3089\u3001\u7236\u306f\u304a\u306a\u3089\u3092\u3057\u305f\u3002"
                    }
                ]
            }
        }
    }
]
