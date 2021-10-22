from typing import Literal, Optional, TypedDict


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
    created_at: str
    level: int
    slug: str
    hidden_at: Optional[str]
    document_url: str
    characters: str
    meanings: list[WanikaniMeaning]
    auxiliary_meanings: list[WanikaniAuxilliaryMeaning]
    meaning_mnemonic: str
    lesson_position: int
    spaced_repetition_system_id: int


class WanikaniAPIVocabularySubject(WanikaniAPISubject):
    """Dictionary containing information about one vocabulary subject"""
    readings: list[WanikaniReading]
    parts_of_speech: list[str]
    component_subject_ids: list[int]
    reading_mnemonic: str
    context_sentences: list[WanikaniContextSentence]
    pronunciation_audios: list[WanikaniPronunciationAudio]


class WanikaniAPIResource(TypedDict):
    """Wanikani API resource object"""
    id: int
    object: str
    url: str
    data_updated_at: Optional[str]
    data: WanikaniAPIVocabularySubject


class WanikaniAPIResponse(TypedDict):
    """Expected format returned from the Wanikani API"""
    object: str
    url: str
    pages: dict
    total_count: int
    data_updated_at: Optional[str]
    data: list[WanikaniAPIResource]
