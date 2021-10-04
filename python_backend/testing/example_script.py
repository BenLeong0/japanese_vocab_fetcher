import json
import requests

API_URL = "http://localhost:5000/words"
payload = {'words': ["食べる", "学生"]}
result = requests.get(API_URL, data=json.dumps(payload))
print(result.text)

example_response = [
    {
        "word": "\u98df\u3079\u308b",
        "jisho": {},
        "accent": {"ojad": ["\u305f\u3079' \u308b"],
        "suzuki": ["\u305f\u3079' \u308b"],
        "wadoku": ["\u305f\u3079' \u308b"]},
        "audio": {
            "forvo": [
                "https://apifree.forvo.com/audio/373k2d3h283g3m2l241k1f292a2m2g2f3i3k3p37393g2g281b3h3o351o3n1o3m2c2g2j2n2q312q3l2c2b3e2e323m1i212j2n2i27212n353h3f2g221k3e3f3g2h1l2k3p2c3d1b1g2g1j3l3d2f2e243a351f3127352b3n1t1t_1j372n27293n2k3o3c3p2d283a2d2q3k2k393p2a223n1t1t",
                "https://apifree.forvo.com/audio/392m2j1h342i3e2d1b37231m2f3h3q2c28351g3n333g1g1j1k353d2b2e271h3o1k2335253l3c3k213a3e3a31343934211o3m3g232o2n1m3q1k3a2m1m1f3m2q34_3h1o2i381j3l2m332m1o2a2o2q233f3q2o2q1h3j1n3n1t1t",
                "https://apifree.forvo.com/audio/2q2b3b251l3j2e3b3c322i2j1b3f2c1k353j3e1h2o3q2o2l2l213o1b331l1f3m3p1p2b1b3f3n3m2q3g3g3b373g211i1k38391k2k2a3j292m2q3k2l3g3b371m2e_3g3b3k1b241l1m1k3i321f2j2l27372g1b212g3a3o211t1t",
                "https://apifree.forvo.com/audio/1f2o3l2b3m2k1l1m253g3m2o21362a393j363228332q3d2934392q2l1l391g3e383h1k2e2d272a392b3o361k262p3i35272k3e313g2k1l3f2e39382j281g2m3n_1k3a3m393b2q2f2o251k2g1j2n342l1j383f2k2f34371t1t",
                "https://apifree.forvo.com/audio/2n2f373n1j2e3b3535351l312k1i1h3l3c39211o2p3p2n2p2e3i2n373f35262e1f2p1p1h1m3q3o1l3p282m3o31231p33373m2p3g2h2b1o25331o3k361b332k1h_3e2n3j2b1k3f362f212g2l1m2q1b271h323f3a362e371t1t",
                "https://apifree.forvo.com/audio/382l2q2n322l3j3q2d232m372c1b2825351k3m2n2h3o3c363o1m311m1l1h1k1m213k362q3k1h2e363l1o24253m1p2c3d22272k2l2f3h3j2l1f3i1n361b1k2m3a_272g39212c263f2l293e352c2l1j312m27211b3p2p2h1t1t",
                "https://apifree.forvo.com/audio/1j36213e2a3b3a242d3f3p1n38223h3i283a2n3k362n3l3a383k3o3k1f3p3i1o383p243f2h2h253i3p3a353f1j2d2p361l3o213n291p1n281f1p3m2m3g2n3f3k_2b32362c1p2q1n2i34282a1j2p251o211g1f3l292g371t1t",
                "https://apifree.forvo.com/audio/1h273o3p3f3p323j271o3n2n3k2b1n2p2b3c3g3g372m1g392i3j242n34353b332o2h2g3k2g3j2d221k1l2a333q3l3c2q2i352g363q3a2m2q3a271i1f1p381f3j_2l2929223b2m382a3o27273g1o3l3n1j351k3m3d353n1t1t",
                "https://apifree.forvo.com/audio/1h3d2a3b3b1k1i2j222f313d3j3m362i3n2m2q2m3h1j262n3e2l3k2c3i3h1i3n391m382j2k36212g2m332c29283i23271i3a2c2b3a1j263j382f2l332b2a3322_212q2d2e2g2l2f2a2f1n253o1o353m2f2j2g3a38252h1t1t",
                "https://apifree.forvo.com/audio/391m3k3e342k361i3n2c3j2h372c2m2e2o3b1o342h2d233b3e2p1f3i3o2m3m3e362h1f1g3m3g3g3o312q2l3o3o1f3o2d3g3k3m3f1n312q362d3e2j3a2121231b_2h1h3528221h323p1b2i3d3m321p3q1p2g353f2i322h1t1t"
            ],
            "wanikani": []
        }
    },
    {
        "word": "\u5b66\u751f",
        "jisho": {},
        "accent": {
            "ojad": ["\u304c\u304f\u305b\u3044"],
            "suzuki": ["\u304c\u304f\u305b\u3044"],
            "wadoku": ["\u304c\u304f\u305b\u3044"]
        },
        "audio": {
            "forvo": [
                "https://apifree.forvo.com/audio/253f3q1o2o3f3a3b32211h21273o3b3j3l1h233f1p3b2p3i3j3g1o2l1i3i2p3o2i362b342l2c2f2q282o2p221k3f3q2d1h2q2335372j1f3m39313j3a2h3p2o1k3p2p3c3q2g2f281l392n2n1m3n2l1g392k3i2g253k371t1t_3p2a312j2n2f2a1f2h3b1i2l1g3j2l3e3k2q1l1b22371t1t",
                "https://apifree.forvo.com/audio/3n2e1i3m1n2l1h253a24282l2f39282a1m32341n373j3b232l1o222j2f2k2q2q333i3j282o1n3p3n3q1i353l1p2f2h3b211p2i2p2o26271k222k3k21312f2b1k2q1o3i1i3j1i1p2j3h3q1b283c3q3q353g1k282j3q211t1t_252d361o2c3m1l3d3d3h2n23273d2d1h382p1p3m2o2h1t1t",
                "https://apifree.forvo.com/audio/2a383932363b3n3422271p3l3d2k2p3g2o221f3g37362p383i2n1o242i3b1f2p3o2c3k2f213p3l2i321g223b3g1g2l223b3p3q273n22252a1f241m233o1m2m3a261n253j373h2g3c213o2p2e31381n3q282j3d231j2h1t1t_312i332a2k3n2q212l3k34221m3q3p313123251j2d371t1t",
                "https://apifree.forvo.com/audio/2m281m25242f2a3k1g383e292l1n3723333e2e2i2q2m3b3c1g1h3p242m3p3g3b2q3j2g3o2h1l2h383q1h3b233n2m2l3j29222d3p2b2d391h212o312o3m2i3e27_362h3b1g363g1o3434251o2n2d1f3n1b1o2i25232m371t1t",
                "https://apifree.forvo.com/audio/3l1p3a2h1p1o361p3j1b2l3q2m3n31371l1p3d1g2k2e3b1p2o3l1m392p3i23212o32372p1b3n3i263m3k3o2f232h2o2a3j2125233k273q1b1j2k343e1i1p3n33_222d2a1j273b2i3l1l2d2o2e3o3c221p3i3o3p21332h1t1t",
                "https://apifree.forvo.com/audio/1o1k3n1p3325313m342l2g2l3e3d1n2i2k1p2m28381p213m2q3p2g361h1i391l253c23212q2o2j263e351h29263427243p221n22391m232p1b27263d1o3b2426_392q282434293n221b1j2b1n3a2p3q1h3m1o2n3c2h2h1t1t",
                "https://apifree.forvo.com/audio/391f1h2l3j231b272j1n2o233i2m35342l2j233k2h25291m3q1m1j3f3q3423262g3g2m283c2p213d2h37393q2f2d1g272d34232q391o363g2425223m3q3i3h22_1f331h313d252g291g1o1k1n1g3k2829263b2d1n283n1t1t",
                "https://apifree.forvo.com/audio/3k2m2c363j342c3o3i37233q393q2g2i3j3l3m26262j2h2e2a331f1m1f2p392p3p3j2l3i1o2i381h222k3f3p2f213h1h393i31283j1m2o3e2o3c212o362k3m2j_3m363f2e2e3m3n1b1i1i2g1l253f1o3i1h323o2q242h1t1t",
                "https://apifree.forvo.com/audio/2o1n2d332a34321k2l3i3j2a2i3e31312l251k3o2g1j3g2l293e1f3h2m223b273b3c2e2m242a32382g391b33242k3k3g1n3m2h3i27381i231h2d213b1b2q2b27_1n1b3c2a2c3p3k2f293m2i2i1k383e3j1l3n2q343l3n1t1t",
                "https://apifree.forvo.com/audio/1l38221g1h3329342e3q261g1j2m1p372e1o2h31213o2c3n1o2m2m231g1h2i3l2a3e311l33221l1o3a2c2925212d231j2q3m1h331f2q3g1k3j2g3j1k2f3m3b31_3n1k2b3n1j3g2c263c2n2b2q2i1g233b1p2m1i2c23211t1t"
            ],
            "wanikani": []
        }
    }
]
