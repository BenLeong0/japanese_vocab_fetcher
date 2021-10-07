from typing import Dict, List, Literal, TypedDict


class Kaki(str):
    """Kanji writing of a word"""

class Yomi(str):
    """Accented reading of a word"""

class URL(str):
    """String representing a URL"""

class HTMLString(str):
    """An HTML file stored as a string"""


class ForvoAPIItem(TypedDict):
    id: int
    word: str
    original: str
    addtime: str
    hits: int
    username: str
    sex: str
    country: str
    code: str
    langname: str
    pathmp3: str
    pathogg: str
    rate: int
    num_votes: int
    num_positive_votes: int


class ForvoAPIResponse(TypedDict):
    attributes: Dict[Literal["total"], int]
    items: List[ForvoAPIItem]


class WanikaniAPIResponse(TypedDict):
    """Expected format returned from the Wanikani API"""


# class JishoResponse(TypedDict):
#     """Dictionary containing the jisho information of the full response"""
#     str: str
JishoResponse = Dict[str, str]

class ResponseItemAccents(TypedDict):
    """Dictionary containing the accent information of the full response"""
    ojad: List[Yomi]
    suzuki: List[Yomi]
    wadoku: List[Yomi]

class ResponseItemAudio(TypedDict):
    """Dictionary containing the audio information of the full response"""
    forvo: List[URL]
    wanikani: List[URL]

class FullResponseItem(TypedDict):
    """Result dict for a word in an API request"""
    word: Kaki
    jisho: JishoResponse
    accent: ResponseItemAccents
    audio: ResponseItemAudio
