from typing import Required, TypedDict


class TatoebaAPIResultTranslation(TypedDict, total=False):
    id: int
    text: Required[str]
    lang: str
    correctness: int
    script: str | None
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
    script: str | None
    license: str
    translations: list[list[TatoebaAPIResultTranslation]]
    transcriptions: list
    audios: list
    user: TatoebaAPIResultUser
    lang_name: str
    dir: str
    lang_tag: str
    is_favorite: bool | None
    is_owned_by_current_user: bool
    permissions: str | None
    current_user_review: int | None


class TatoebaAPIResponse(TypedDict):
    """Expected format returned from the Tatoeba API"""

    paging: dict
    results: list[TatoebaAPIResult]
