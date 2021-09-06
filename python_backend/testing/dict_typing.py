from typing import DefaultDict, Dict, List, TypedDict

from bs4 import BeautifulSoup as Soup

# General types

書方 = str
読方 = str
URL = str
HTMLString = str


# Jisho

JishoDict = Dict


# Accents

class ExpectedSection(TypedDict):
    writing_section: Soup
    writings: List[書方]
    reading_sections: Soup
    readings: List[読方]


class AccentDict(TypedDict):
    html: HTMLString
    url: URL
    expected_sections: List[ExpectedSection]
    full_accent_dict: DefaultDict[書方, List[読方]]
    expected_output: Dict[書方, List[読方]]


# Audio

AudioDict = Dict


# Expected Result

class ExpectedResultAccents(TypedDict):
    ojad: List[読方]
    suzuki: List[読方]
    wadoku: List[読方]

class ExpectedResultAudio(TypedDict):
    forvo: List[URL]
    wanikani: List[URL]

class ExpectedResult(TypedDict):
    word: 書方
    jisho: JishoDict
    accent: ExpectedResultAccents
    audio: ExpectedResultAudio


# Complete type

class TestDict(TypedDict):
    id: str
    input: List[書方]
    jisho: JishoDict
    ojad: AccentDict
    suzuki: AccentDict
    wadoku: AccentDict
    forvo: AudioDict
    wanikani: AudioDict
    expected_result: List[ExpectedResult]
