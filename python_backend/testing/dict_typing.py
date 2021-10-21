from typing import DefaultDict, Dict, List, TypedDict

from bs4 import BeautifulSoup as Soup

from custom_types.alternative_string_types import HTMLString, URL
from custom_types.response_types import ResponseItemForvo, ResponseItemOJAD, ResponseItemWadoku, ResponseItemWanikani
from custom_types.wanikani_api_types import WanikaniAPIResponse


# Jisho

ExpectedJishoOutput = Dict[str, Dict]

class JishoTestDict(TypedDict):
    """Dictionary generated by the Jisho module upon fetching a word's definition etc"""
    expected_output: ExpectedJishoOutput


# Accents

class AccentModuleTestDict(TypedDict):
    """Dictionary generated by modules that fetch the accent of words (ie OJAD, Suzuki, Wadoku)"""
    expected_output: Dict[str, List[str]]


class OjadExpectedSection(TypedDict):
    """Dictionary containing an HTML section extracted by the OJAD module
    and its contained information"""
    na_adj: bool
    writing_section: Soup
    writings: List[str]
    reading_sections: List[Soup]
    readings: List[str]


class OjadTestDict(TypedDict):
    """Dictionary generated by the OJAD module"""
    htmls: List[HTMLString]
    url: URL
    expected_sections: List[OjadExpectedSection]
    full_accent_dict: DefaultDict[str, List[str]]
    expected_output: Dict[str, ResponseItemOJAD]


class SuzukiExpectedSection(TypedDict):
    """Dictionary containing an HTML section extracted by the Suzuki module
    and its contained information"""
    writing_section: Soup
    writing: str
    reading_section: Soup
    accent_section: Soup
    reading: str


class SuzukiTestDict(AccentModuleTestDict):
    """Dictionary generated by the Suzuki module"""
    html: HTMLString
    formdata: Dict[str, str]
    expected_sections: List[SuzukiExpectedSection]


class WadokuExpectedSection(TypedDict):
    """Dictionary containing an HTML section extracted by the Wadoku module
    and its contained information"""
    writing_section: Soup
    writings: List[str]
    reading_sections: List[Soup]
    readings: List[str]


class WadokuTestDict(TypedDict):
    """Dictionary generated by the Wadoku module"""
    html: HTMLString
    url: URL
    expected_sections: List[WadokuExpectedSection]
    full_accent_dict: DefaultDict[str, List[str]]
    expected_output: Dict[str, ResponseItemWadoku]


# Audio

class AudioDict(TypedDict):
    """Dictionary generated by modules that fetch audio files of words (ie Forvo, Wanikani)"""
    expected_output: Dict[str, List[URL]]


class ForvoExpectedSection(TypedDict):
    """Dictionary generated by the audio for an individual word"""
    url: URL
    api_response: str
    total_items: int


class ForvoTestDict(TypedDict):
    """Dictionary generated by the Forvo module"""
    expected_sections: Dict[str, ForvoExpectedSection]
    expected_output: Dict[str, ResponseItemForvo]


class WanikaniTestDict(TypedDict):
    """Dictionary generated by the Wanikani module"""
    url: URL
    api_response: WanikaniAPIResponse
    result_dict: Dict[str, ResponseItemWanikani]
    expected_output: Dict[str, ResponseItemWanikani]


# Expected final result

class ExpectedResult(TypedDict):
    """Expected output for the main get_info() function"""
    word: str
    jisho: ExpectedJishoOutput
    ojad: ResponseItemOJAD
    suzuki: List[str]
    wadoku: ResponseItemWadoku
    forvo: ResponseItemForvo
    wanikani: ResponseItemWanikani


# Complete test dictionary type

class FullTestDict(TypedDict):
    """A dictionary containing all the information and expected results for any test"""
    id: str
    input: List[str]
    jisho: JishoTestDict
    ojad: OjadTestDict
    suzuki: SuzukiTestDict
    wadoku: WadokuTestDict
    forvo: ForvoTestDict
    wanikani: WanikaniTestDict
    expected_result: List[ExpectedResult]
