from typing import Optional, TypedDict


class TatoebaAPIResultTranslation(TypedDict, total=False):
    id: int
    text: str
    lang: str
    correctness: int
    script: Optional[str]
    transcriptions: list
    audios: list
    isDirect: bool
    lang_name: str
    dir: str
    lang_tag: str


class TatoebaAPIResultUser(TypedDict):
    username: str


class TatoebaAPIResult(TypedDict):
    id: int
    text: str
    lang: str
    correctness: int
    script: Optional[str]
    license: str
    translations: list[list[TatoebaAPIResultTranslation]]
    transcriptions: list
    audios: list
    user: TatoebaAPIResultUser
    lang_name: str
    dir: str
    lang_tag: str
    is_favorite: Optional[bool]
    is_owned_by_current_user: bool
    permissions: Optional[str]
    current_user_review: Optional[int]


class TatoebaAPIResponse(TypedDict):
    """Expected format returned from the Wanikani API"""
    paging: dict
    results: list[TatoebaAPIResult]
