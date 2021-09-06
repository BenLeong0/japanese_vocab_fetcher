from typing import DefaultDict, Dict, List, TypedDict


# Jisho

JishoDict = Dict


# Accents

class AccentDict(TypedDict):
    html: str
    url: str
    expected_sections: List[dict]
    full_accent_dict: DefaultDict
    expected_output: Dict[str, List[str]]


# Audio

AudioDict = Dict


# Expected Result

class ExpectedResultAccents(TypedDict):
    ojad: List[str]
    suzuki: List[str]
    wadoku: List[str]

class ExpectedResultAudio(TypedDict):
    forvo: List[str]
    wanikani: List[str]

class ExpectedResult(TypedDict):
    word: str
    jisho: Dict
    accent: ExpectedResultAccents
    audio: ExpectedResultAudio


# Complete type

class TestDict(TypedDict):
    id: str
    input: List[str]
    jisho: JishoDict
    ojad: AccentDict
    suzuki: AccentDict
    wadoku: AccentDict
    forvo: AudioDict
    wanikani: AudioDict
    expected_result: List[ExpectedResult]
