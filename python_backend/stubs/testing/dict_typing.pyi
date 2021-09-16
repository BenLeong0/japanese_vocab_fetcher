from bs4 import BeautifulSoup as Soup
from custom_types import Kaki as Kaki, URL as URL, Yomi as Yomi
from typing import DefaultDict, Dict, List, TypedDict

class HTMLString(str): ...
class JishoDict(Dict): ...

class AccentDict(TypedDict):
    expected_output: Dict[Kaki, List[Yomi]]

class OjadExpectedSection(TypedDict, total=False):
    na_adj: bool
    writing_section: Soup
    writings: List[Kaki]
    reading_sections: List[Soup]
    readings: List[Yomi]

class OjadAccentDict(AccentDict):
    htmls: List[HTMLString]
    url: URL
    expected_sections: List[OjadExpectedSection]
    full_accent_dict: DefaultDict[Kaki, List[Yomi]]

class SuzukiExpectedSection(TypedDict):
    writing_section: Soup
    writing: Kaki
    reading_section: Soup
    accent_section: Soup
    reading: Yomi

class SuzukiAccentDict(AccentDict):
    html: HTMLString
    formdata: Dict[str, str]
    expected_sections: List[SuzukiExpectedSection]

class WadokuExpectedSection(TypedDict):
    writing_section: Soup
    writings: List[Kaki]
    reading_sections: List[Soup]
    readings: List[Yomi]

class WadokuAccentDict(AccentDict):
    html: HTMLString
    url: URL
    expected_sections: List[WadokuExpectedSection]
    full_accent_dict: DefaultDict[Kaki, List[Yomi]]

class AudioDict(Dict): ...

class ExpectedResultAccents(TypedDict):
    ojad: List[Yomi]
    suzuki: List[Yomi]
    wadoku: List[Yomi]

class ExpectedResultAudio(TypedDict):
    forvo: List[URL]
    wanikani: List[URL]

class ExpectedResult(TypedDict):
    word: Kaki
    jisho: JishoDict
    accent: ExpectedResultAccents
    audio: ExpectedResultAudio

class FullTestDict(TypedDict):
    id: str
    input: List[Kaki]
    jisho: JishoDict
    ojad: OjadAccentDict
    suzuki: SuzukiAccentDict
    wadoku: WadokuAccentDict
    forvo: AudioDict
    wanikani: AudioDict
    expected_result: List[ExpectedResult]
