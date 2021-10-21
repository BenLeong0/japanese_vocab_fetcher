from typing import Literal, TypedDict

from custom_types.alternative_string_types import Kaki, URL, Yomi


class JishoAPIItemJapanese(TypedDict, total=False):
    word: Kaki
    reading: Yomi


class JishoAPIItemLink(TypedDict):
    test: str
    url: URL


class JishoAPIItemSense(TypedDict):
    english_definitions: list[str]
    parts_of_speech: list[str]
    links: list[JishoAPIItemLink]
    tags: list[str]
    restrictions: list[Yomi]
    see_also: list[str]
    antonyms: list[Yomi]
    source: list[str]
    info: list[str]


class JishoAPIItemAttribution(TypedDict):
    jmdict: bool
    jmnedict: bool
    dbpedia: URL


class JishoAPIItem(TypedDict):
    slug: Kaki
    is_common: bool
    tags: list[str]
    jlpt: list[str]
    japanese: list[JishoAPIItemJapanese]
    senses: list[JishoAPIItemSense]
    attribution: dict


class JishoAPIResponse(TypedDict):
    meta: dict[Literal["status"], int]
    data: list[JishoAPIItem]
