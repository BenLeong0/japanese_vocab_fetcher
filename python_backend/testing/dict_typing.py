from typing import DefaultDict, Optional, TypedDict

from bs4 import BeautifulSoup as Soup

from custom_types.alternative_string_types import HTMLString, URL
from custom_types.jisho_api_types import JishoAPIItem, JishoAPIResponse
from custom_types.response_types import (
    JishoExtraItem,
    ResponseItemForvo,
    ResponseItemJapanesePod,
    ResponseItemJisho,
    ResponseItemOJAD,
    ResponseItemSuzuki,
    ResponseItemTangorin,
    ResponseItemWadoku,
    ResponseItemWanikani,
)
from custom_types.wanikani_api_types import WanikaniAPIResponse


# Jisho

ExpectedJishoOutput = dict[str, dict]

class JishoExpectedSection(TypedDict):
    """Dictionary containing the Jisho data for a single word"""
    url: URL
    api_response: JishoAPIResponse
    filtered_items: list[JishoAPIItem]
    extra_items: list[JishoExtraItem]

class JishoTestDict(TypedDict):
    """Dictionary generated by the Jisho module upon fetching a word's definition etc"""
    expected_sections: dict[str, JishoExpectedSection]
    expected_output: dict[str, ResponseItemJisho]


# Accents

class OjadExpectedSection(TypedDict):
    """Dictionary containing an HTML section extracted by the OJAD module
    and its contained information"""
    na_adj: bool
    writing_section: Soup
    writings: list[str]
    reading_sections: list[Soup]
    readings: list[str]


class OjadTestDict(TypedDict):
    """Dictionary generated by the OJAD module"""
    htmls: list[HTMLString]
    url: URL
    expected_sections: list[OjadExpectedSection]
    full_accent_dict: DefaultDict[str, list[str]]
    expected_output: dict[str, ResponseItemOJAD]


class SuzukiExpectedSection(TypedDict):
    """Dictionary containing an HTML section extracted by the Suzuki module
    and its contained information"""
    writing_section: Soup
    writing: str
    reading_section: Soup
    accent_section: Soup
    reading: str


class SuzukiTestDict(TypedDict):
    """Dictionary generated by the Suzuki module"""
    html: HTMLString
    formdata: dict[str, str]
    expected_sections: list[SuzukiExpectedSection]
    expected_output: dict[str, ResponseItemSuzuki]


class WadokuExpectedSection(TypedDict):
    """Dictionary containing an HTML section extracted by the Wadoku module
    and its contained information"""
    writing_section: Soup
    writings: list[str]
    reading_sections: list[Soup]
    readings: list[str]


class WadokuTestDict(TypedDict):
    """Dictionary generated by the Wadoku module"""
    html: HTMLString
    url: URL
    expected_sections: list[WadokuExpectedSection]
    full_accent_dict: DefaultDict[str, list[str]]
    expected_output: dict[str, ResponseItemWadoku]


class ForvoExpectedSection(TypedDict):
    """Dictionary generated by the audio for an individual word"""
    url: URL
    api_response: str
    total_items: int


class ForvoTestDict(TypedDict):
    """Dictionary generated by the Forvo module"""
    expected_sections: dict[str, ForvoExpectedSection]
    expected_output: dict[str, ResponseItemForvo]


class JapanesePodExpectedRow(TypedDict):
    """Dictionary generated by the JapanesePod module a single result for an individual word"""
    raw_row: str
    matches: tuple[str, Optional[str]]
    results: tuple[list[str], list[str]]
    relevant: bool


class JapanesePodExpectedSection(TypedDict):
    """Dictionary generated by the JapanesePod module for an individual word"""
    url: URL
    html: str
    expected_rows: list[JapanesePodExpectedRow]
    all_urls: list[URL]


class JapanesePodTestDict(TypedDict):
    """Dictionary generated by the JapanesePod module"""
    expected_sections: dict[str, JapanesePodExpectedSection]
    expected_output: dict[str, ResponseItemJapanesePod]


class TangorinExpectedSection(TypedDict):
    """Dictionary generated by the Tangorin module for an individual word"""
    url: URL
    html: str


class TangorinTestDict(TypedDict):
    """Dictionary generated by the Tangorin module"""
    expected_sections: dict[str, TangorinExpectedSection]
    expected_output: dict[str, ResponseItemTangorin]


class WanikaniTestDict(TypedDict):
    """Dictionary generated by the Wanikani module"""
    url: URL
    api_response: WanikaniAPIResponse
    result_dict: dict[str, ResponseItemWanikani]
    expected_output: dict[str, ResponseItemWanikani]


# Expected final result

class ExpectedResult(TypedDict):
    """Expected output for the main get_info() function"""
    word: str
    japanesepod: ResponseItemJapanesePod
    jisho: ResponseItemJisho
    ojad: ResponseItemOJAD
    suzuki: ResponseItemSuzuki
    wadoku: ResponseItemWadoku
    forvo: ResponseItemForvo
    tangorin: ResponseItemTangorin
    wanikani: ResponseItemWanikani


# Complete test dictionary type

class FullTestDict(TypedDict):
    """A dictionary containing all the information and expected results for any test"""
    id: str
    input: list[str]
    japanesepod: JapanesePodTestDict
    jisho: JishoTestDict
    ojad: OjadTestDict
    suzuki: SuzukiTestDict
    wadoku: WadokuTestDict
    forvo: ForvoTestDict
    tangorin: TangorinTestDict
    wanikani: WanikaniTestDict
    expected_result: list[ExpectedResult]
