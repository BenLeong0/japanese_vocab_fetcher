from typing import Annotated

from pydantic import BeforeValidator


class Kaki(str):
    """Kanji writing of a word"""


KakiField = Annotated[Kaki, BeforeValidator(Kaki)]


class Yomi(str):
    """Accented reading of a word"""


YomiField = Annotated[Yomi, BeforeValidator(Yomi)]


class URL(str):
    """String representing a URL"""


URLField = Annotated[URL, BeforeValidator(URL)]


class HTMLString(str):
    """An HTML file stored as a string"""
