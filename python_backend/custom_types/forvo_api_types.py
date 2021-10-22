from typing import Literal, TypedDict


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
    attributes: dict[Literal["total"], int]
    items: list[ForvoAPIItem]
