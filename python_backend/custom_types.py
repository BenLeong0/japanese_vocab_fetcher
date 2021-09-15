from typing import DefaultDict, Dict, List, Protocol, TypedDict


class Kaki(str):
    """Kanji writing of a word"""

class Yomi(str):
    """Accented reading of a word"""

class URL(str):
    """String representing a URL"""


# class JishoResponse(TypedDict):
#     """Dictionary containing the jisho information of the full response"""
#     str: str
JishoResponse = Dict[str, str]

class AccentResponse(TypedDict):
    """Dictionary containing the accent information of the full response"""
    ojad: List[Yomi]
    suzuki: List[Yomi]
    wadoku: List[Yomi]

class AudioResponse(TypedDict):
    """Dictionary containing the audio information of the full response"""
    forvo: List[URL]
    wanikani: List[URL]

class FullResponse(TypedDict):
    """Full response to an API request"""
    word: Kaki
    jisho: JishoResponse
    accent: AccentResponse
    audio: AudioResponse
