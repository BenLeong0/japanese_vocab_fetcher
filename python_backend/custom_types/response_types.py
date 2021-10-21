from typing import Dict, List, TypedDict

from custom_types.alternative_string_types import (
    Kaki,
    URL,
    Yomi,
)
from custom_types.wanikani_api_types import (
    WanikaniContextSentence,
    WanikaniPronunciationAudio,
)


class ResponseItem(TypedDict):
    """Dictionary containing the information from one of the modules"""
    success: bool


# Jisho

# class JishoResponse(TypedDict):
#     """Dictionary containing the jisho information of the full response"""
#     str: str
JishoResponse = Dict[str, str]


# Forvo

class ForvoMainData(TypedDict):
    audio: List[URL]

class ResponseItemForvo(ResponseItem):
    """Dictionary containing the audio information from Forvo"""
    main_data: ForvoMainData


# Wanikani

class WanikaniMainData(TypedDict):
    audio: List[WanikaniPronunciationAudio]
    sentences: List[WanikaniContextSentence]

class ResponseItemWanikani(ResponseItem):
    """Dictionary containing the audio and sentence information from Wanikani"""
    main_data: WanikaniMainData


# Full response

class FullResponseItem(TypedDict):
    """Result dict for a word in an API request"""
    word: Kaki
    jisho: JishoResponse
    ojad: List[Yomi]
    suzuki: List[Yomi]
    wadoku: List[Yomi]
    forvo: ResponseItemForvo
    wanikani: ResponseItemWanikani
