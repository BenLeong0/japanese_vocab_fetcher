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

# class JishoResponse(TypedDict):
#     """Dictionary containing the jisho information of the full response"""
#     str: str
JishoResponse = Dict[str, str]

class ResponseItemAccents(TypedDict):
    """Dictionary containing the accent information of the full response"""
    ojad: List[Yomi]
    suzuki: List[Yomi]
    wadoku: List[Yomi]


class ResponseItemWanikaniAudio(TypedDict):
    """Dictionary containing the audio information from the Wanikani API response"""
    url: URL
    metadata: WanikaniPronunciationAudioMetadata
    content_type: str

class ResponseItemWanikani(TypedDict):
    """Dictionary containing the audio and sentence information from the Wanikani API response"""
    audio: List[WanikaniPronunciationAudio]
    sentences: List[WanikaniContextSentence]

class ResponseItemAudio(TypedDict):
    """Dictionary containing the audio information of the full response"""
    forvo: List[URL]
    wanikani: ResponseItemWanikani

class FullResponseItem(TypedDict):
    """Result dict for a word in an API request"""
    word: Kaki
    jisho: JishoResponse
    accent: ResponseItemAccents
    audio: ResponseItemAudio
