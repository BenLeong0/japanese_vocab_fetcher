from typing import Dict, List, TypedDict


class kaki(str):
    """Kanji writing of a word"""

class yomi(str):
    """Accented reading of a word"""

class URL(str):
    """String representing a URL"""


class AccentResponse(TypedDict):
    """Dictionary containing the accent information of the full response"""
    ojad: List[yomi]
    suzuki: List[yomi]
    wadoku: List[yomi]

class AudioResponse(TypedDict):
    """Dictionary containing the audio information of the full response"""
    forvo: List[URL]
    wanikani: List[URL]

class FullResponse(TypedDict):
    """Full response to an API request"""
    word: kaki
    jisho: Dict[str, str]
    accent: AccentResponse
    audio: AudioResponse
