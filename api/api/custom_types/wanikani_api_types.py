from typing import Literal, Optional

from api.custom_types.helpers import MyBaseModel


class WanikaniMeaning(MyBaseModel):
    """Dictionary containing information about subject's meaning"""

    meaning: str
    primary: bool
    accepted_answer: bool


class WanikaniAuxilliaryMeaning(MyBaseModel):
    """Dictionary containing information about a subject's auxilliary meaning"""

    meaning: str
    type: Literal["whitelist", "blacklist"]


class WanikaniReading(MyBaseModel):
    """Dictionary containing information about a reading for a vocab subject"""

    accepted_answer: bool
    primary: bool
    reading: str


class WanikaniContextSentence(MyBaseModel):
    """Dictionary containing information about a context sentence for a vocab subject"""

    en: str
    ja: str


class WanikaniPronunciationAudioMetadata(MyBaseModel):
    """Dictionary containing metadata about a pronunciation for a vocab subject"""

    gender: str
    source_id: int
    pronunciation: str
    voice_actor_id: int
    voice_actor_name: str
    voice_description: str


class WanikaniPronunciationAudio(MyBaseModel):
    """Dictionary containing information about a pronunciation for a vocab subject"""

    url: str
    content_type: str
    metadata: WanikaniPronunciationAudioMetadata


class WanikaniAPISubject(MyBaseModel):
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


class WanikaniAPIResource(MyBaseModel):
    """Wanikani API resource object"""

    id: int
    object: str
    url: str
    data_updated_at: Optional[str]
    data: WanikaniAPIVocabularySubject


class WanikaniAPIResponse(MyBaseModel):
    """Expected format returned from the Wanikani API"""

    object: str
    url: str
    pages: dict
    total_count: int
    data_updated_at: Optional[str]
    data: list[WanikaniAPIResource]
