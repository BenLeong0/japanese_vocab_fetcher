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
    },
}

WADOKU_COMEBACK: TestingDict = {
    'input': ['カムバック'],
    'html': get_file_as_string('resp_comeback.html'),
    'expected_output': {
        'カムバック': ["かむば' っく", "か' むばっく" ],
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

WADOKU_KO: TestingDict = {
    'input': ['湖'],
    'html': get_file_as_string('resp_ko.html'),
    'expected_output': {
        '湖': ["みずう' み" ],
        # '～湖': ["～'*こ'"],
    },
}
