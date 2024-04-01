from typing import Literal, Optional

from api.custom_types.alternative_string_types import KakiField, YomiField
from api.custom_types.helpers import MyBaseModel, partial_model


class JishoAPIItemJapanese(MyBaseModel):
    word: Optional[KakiField] = None
    reading: Optional[YomiField] = None


class JishoAPIItemLink(MyBaseModel):
    text: str
    url: str


@partial_model
class JishoAPIItemSense(MyBaseModel):
    english_definitions: list[str]
    parts_of_speech: list[str]
    links: list[JishoAPIItemLink]
    tags: list[str]
    restrictions: list[str]
    see_also: list[str]
    antonyms: list[str]
    source: list[str]
    info: list[str]
    sentences: list


class JishoAPIItemAttribution(MyBaseModel):
    jmdict: bool
    jmnedict: bool
    dbpedia: str | Literal[False]


class JishoAPIItem(MyBaseModel):
    slug: str
    japanese: list[JishoAPIItemJapanese]
    is_common: Optional[bool] = None
    tags: Optional[list[str]] = None
    jlpt: Optional[list[str]] = None
    senses: Optional[list[JishoAPIItemSense]] = None
    attribution: Optional[JishoAPIItemAttribution] = None


class JishoAPIMeta(MyBaseModel):
    status: int


class JishoAPIResponse(MyBaseModel):
    meta: JishoAPIMeta
    data: list[JishoAPIItem]
