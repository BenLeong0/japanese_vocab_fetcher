# from collections import defaultdict
# import json
# import re
from typing import Optional

# from bs4 import BeautifulSoup as Soup
# import requests

from custom_types.alternative_string_types import Kaki, Yomi
from custom_types.exception_types import APIError
from custom_types.response_types import ContextSentence, ResponseItemTangorin


NAME = "tangorin"


class TangorinAPIError(APIError):
    pass


def response_factory(sentence_list: Optional[list[ContextSentence]] = None) -> ResponseItemTangorin:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "sentences": [] if sentence_list is None else sentence_list,
        },
    }


def error_response_factory(error: TangorinAPIError) -> ResponseItemTangorin:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "sentences": [],
        },
    }


def main(_word_list: list[Kaki]) -> dict[Kaki, ResponseItemTangorin]:
    return {}

# Multithread each word (see forvo)
# Fetch html
# Extract only results-dl div (to clean)
# Extract div's with class "sentences" (max 8?)
# Use regex to empty r"<rt class="roma">.*</rt>" components
# Extract text from s-jp div
# Extract text from s-en div
# Combine into ContextSentence dict
# Combine into list[ContextSentence]
# Build into ResponseItemTangorin
# Combine into dict[Kaki, ResponseItemTangorin]]
# Return
