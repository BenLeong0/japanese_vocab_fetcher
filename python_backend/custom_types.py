from typing import Dict, List, TypedDict


class 書方(str):
    """Kanji writing of a word"""

class 読方(str):
    """Accented reading of a word"""

class URL(str):
    """String representing a URL"""


class AccentResponse(TypedDict):
    """Dictionary containing the accent information of the full response"""
    ojad: List[読方]
    suzuki: List[読方]
    wadoku: List[読方]

class AudioResponse(TypedDict):
    """Dictionary containing the audio information of the full response"""
    forvo: List[URL]
    wanikani: List[URL]

class FullResponse(TypedDict):
    """Full response to an API request"""
    word: 書方
    jisho: Dict[str, str]
    accent: AccentResponse
    audio: AudioResponse
