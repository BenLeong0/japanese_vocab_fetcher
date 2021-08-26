from typing import List, TypedDict

def get_file_as_string(filename):
    filelocation = "testing/test_wadoku/"
    with open(filelocation+filename, 'r', encoding='utf8') as myfile:
        return myfile.read()


class TestingDict(TypedDict):
    html: str
    expected_output: List[str]


WADOKU_MEGANE: TestingDict = {
    'input': ['眼鏡'],
    'html': get_file_as_string('resp_megane.html'),
    'expected_output': {
        '眼鏡': ["め' がね", "がんきょう" ],
        '眼鏡屋': [],
        '眼鏡橋': ["めがね' ばし"]
    },
}

WADOKU_COMEBACK: TestingDict = {
    'input': ['カムバック'],
    'html': get_file_as_string('resp_comeback.html'),
    'expected_output': {
        'カムバック': ["かむば' っく", "かむばっく" ],
        'カムバックする': ["かむば' っくする"],
    },
}

WADOKU_TABERU_GAKUSEI: TestingDict = {
    'input': ['食べる', '学生'],
    'html': get_file_as_string('resp_taberu_gakusei.html'),
    'expected_output': {
        '食べる': ["たべ' る" ],
        '学生': ["がくせい"],
    },
}
