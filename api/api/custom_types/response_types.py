from typing import Optional

from api.custom_types.alternative_string_types import Kaki, URL, Yomi
from api.custom_types.exception_types import APIErrorDict
from api.custom_types.helpers import MyBaseModel
from api.custom_types.jisho_api_types import JishoAPIItem, JishoAPIItemJapanese
from api.custom_types.wanikani_api_types import WanikaniPronunciationAudio


class ResponseItem(MyBaseModel):
    """Dictionary containing the information from one of the modules"""

    success: bool
    error: Optional[APIErrorDict]


class ContextSentence(MyBaseModel):
    """Dictionary containing information about a context sentence for a vocab subject"""

    en: str
    ja: str


# Jisho


class JishoExtraItem(MyBaseModel):
    slug: str
    japanese: list[JishoAPIItemJapanese]


class JishoMainData(MyBaseModel):
    results: list[JishoAPIItem]
    extra: list[JishoExtraItem]


class ResponseItemJisho(ResponseItem):
    """Dictionary containing the information from Jisho"""

    main_data: JishoMainData


# OJAD


class OJADMainData(MyBaseModel):
    accent: list[Yomi]


class ResponseItemOJAD(ResponseItem):
    """Dictionary containing the accent information from OJAD"""

    main_data: OJADMainData


# Suzuki


class SuzukiMainData(MyBaseModel):
    accent: list[Yomi]


class ResponseItemSuzuki(ResponseItem):
    """Dictionary containing the accent information from Suzuki"""

    main_data: SuzukiMainData


# Wadoku


class WadokuMainData(MyBaseModel):
    accent: list[Yomi]


class ResponseItemWadoku(ResponseItem):
    """Dictionary containing the accent information from Wadoku"""

    main_data: WadokuMainData


# Forvo


class ForvoAudio(MyBaseModel):
    url: URL
    username: str


class ForvoMainData(MyBaseModel):
    audio: list[ForvoAudio]


class ResponseItemForvo(ResponseItem):
    """Dictionary containing the audio information from Forvo"""

    main_data: ForvoMainData


# JapanesePod


class JapanesePodAudio(MyBaseModel):
    url: URL
    writing: str
    reading: str


class JapanesePodMainData(MyBaseModel):
    audio: list[JapanesePodAudio]


class ResponseItemJapanesePod(ResponseItem):
    """Dictionary containing the audio information from JapanesePod"""

    main_data: JapanesePodMainData


# Wanikani


class WanikaniMainData(MyBaseModel):
    audio: list[WanikaniPronunciationAudio]
    sentences: list[ContextSentence]


class ResponseItemWanikani(ResponseItem):
    """Dictionary containing the audio and sentence information from Wanikani"""

    main_data: WanikaniMainData


# Tangorin


class TangorinMainData(MyBaseModel):
    sentences: list[ContextSentence]


class ResponseItemTangorin(ResponseItem):
    """Dictionary containing the accent information from Tangorin"""

    main_data: TangorinMainData


# Full response


class FullResponseItem(MyBaseModel):
    """Result dict for a word in an API request"""

    word: Kaki
    japanesepod: ResponseItemJapanesePod
    jisho: ResponseItemJisho
    ojad: ResponseItemOJAD
    suzuki: ResponseItemSuzuki
    wadoku: ResponseItemWadoku
    forvo: ResponseItemForvo
    tangorin: ResponseItemTangorin
    wanikani: ResponseItemWanikani
