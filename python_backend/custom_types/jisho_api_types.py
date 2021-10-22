from typing import TypedDict


class JishoAPIItemJapanese(TypedDict, total=False):
    word: str
    reading: str


class JishoAPIItemLink(TypedDict):
    text: str
    url: str


class JishoAPIItemSense(TypedDict, total=False):
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


class JishoAPIItemAttribution(TypedDict):
    jmdict: bool
    jmnedict: bool
    dbpedia: str


class JishoAPIItem(TypedDict, total=False):
    slug: str
    is_common: bool
    tags: list[str]
    jlpt: list[str]
    japanese: list[JishoAPIItemJapanese]
    senses: list[JishoAPIItemSense]
    attribution: dict


class JishoAPIMeta(TypedDict):
    status: int


class JishoAPIResponse(TypedDict):
    meta: JishoAPIMeta
    data: list[JishoAPIItem]
