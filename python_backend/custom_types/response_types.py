from typing import Dict, List, TypedDict

from custom_types.alternative_string_types import (
    Kaki,
    URL,
    Yomi,
)
from custom_types.wanikani_api_types import (
    WanikaniContextSentence,
    WanikaniPronunciationAudio,
    WanikaniPronunciationAudioMetadata,
)


# Jisho

# class JishoResponse(TypedDict):
#     """Dictionary containing the jisho information of the full response"""
#     str: str
JishoResponse = Dict[str, str]


# Wanikani

class ResponseItemWanikani(TypedDict):
    """Dictionary containing the audio and sentence information from the Wanikani API response"""
    success: bool
    audio: List[WanikaniPronunciationAudio]
    sentences: List[WanikaniContextSentence]


# Forvo

class ResponseItemForvo(TypedDict):
    """Dictionary containing the audio information from the Wanikani API response"""
    success: bool
    audio: List[URL]

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
