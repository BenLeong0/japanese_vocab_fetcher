from typing import Dict, List, Literal, Optional, TypedDict


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


class WanikaniMeaning(TypedDict):
    """Dictionary containing information about subject's meaning"""
    meaning: str
    primary: bool
    accepted_answer: bool


class WanikaniAuxilliaryMeaning(TypedDict):
    """Dictionary containing information about a subject's auxilliary meaning"""
    meaning: str
    type: Literal["whitelist", "blacklist"]


class WanikaniReading(TypedDict):
    """Dictionary containing information about a reading for a vocab subject"""
    accepted_answer: bool
    primary: bool
    reading: str


class WanikaniContextSentence(TypedDict):
    """Dictionary containing information about a context sentence for a vocab subject"""
    en: str
    ja: str


class WanikaniPronunciationAudioMetadata(TypedDict):
    """Dictionary containing metadata about a pronunciation for a vocab subject"""
    gender: str
    source_id: int
    pronunciation: str
    voice_actor_id: int
    voice_actor_name: str
    voice_description: str


class WanikaniPronunciationAudio(TypedDict):
    """Dictionary containing information about a pronunciation for a vocab subject"""
    url: str
    content_type: str
    metadata: WanikaniPronunciationAudioMetadata


class WanikaniAPISubject(TypedDict):
    """Dictionary containing information about one subject"""
    id: int
    object: str
    auxiliary_meanings: List[WanikaniAuxilliaryMeaning]
    characters: str
    created_at: str
    document_url: str
    hidden_at: Optional[str]
    lesson_position: int
    level: int
    meaning_mnenomic: str
    meanings: List[WanikaniMeaning]
    slug: str
    spaced_repetition_system_id: int


class WanikaniAPIVocabularySubject(WanikaniAPISubject):
    """Dictionary containing information about one vocabulary subject"""
    component_subject_ids: List[int]
    context_sentences: List[WanikaniContextSentence]
    meaning_mnemonic: str
    parts_of_speech: List[str]
    pronunciation_audios: List[WanikaniPronunciationAudio]
    readings: List[WanikaniReading]
    reading_mnemonic: str



class WanikaniAPIResponse(TypedDict):
    """Expected format returned from the Wanikani API"""
    object: str
    url: str
    pages: Dict
    total_count: int
    data_updated_at: str
    data: List[WanikaniAPISubject]


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
