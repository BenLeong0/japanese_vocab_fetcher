from typing import Annotated

from pydantic import BeforeValidator


class Kaki(str):
    """Kanji writing of a word"""


class Yomi(str):
    """Accented reading of a word"""


class URL(str):
    """String representing a URL"""


URLField = Annotated[URL, BeforeValidator(lambda x: URL(x))]


class HTMLString(str):
    """An HTML file stored as a string"""
