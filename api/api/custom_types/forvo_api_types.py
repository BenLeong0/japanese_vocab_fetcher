from typing import Literal, Optional

from api.custom_types.helpers import MyBaseModel


class ForvoAPIItem(MyBaseModel):
    id: int
    word: str
    pathmp3: str
    username: str
    original: Optional[str] = None
    addtime: Optional[str] = None
    hits: Optional[int] = None
    sex: Optional[str] = None
    country: Optional[str] = None
    code: Optional[str] = None
    langname: Optional[str] = None
    pathogg: Optional[str] = None
    rate: Optional[int] = None
    num_votes: Optional[int] = None
    num_positive_votes: Optional[int] = None


class ForvoAPIResponse(MyBaseModel):
    attributes: dict[Literal["total"], int]
    items: list[ForvoAPIItem]
