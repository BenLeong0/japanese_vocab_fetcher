from threading import Thread
from typing import Optional

# from bs4 import BeautifulSoup as Soup
# from bs4.element import Tag
# import requests

from custom_types.alternative_string_types import Kaki
from custom_types.exception_types import APIError
from custom_types.response_types import ContextSentence, ResponseItemJapanesePod


NAME = "japanesepod"


class JapanesePodAPIError(APIError):
    pass


def response_factory(audio_list: Optional[list[ContextSentence]] = None) -> ResponseItemJapanesePod:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "audio": [] if audio_list is None else audio_list,
        },
    }


def error_response_factory(error: JapanesePodAPIError) -> ResponseItemJapanesePod:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "audio": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemJapanesePod]:
    audio_dict: dict[Kaki, ResponseItemJapanesePod] = {}

    def call_script(word: Kaki) -> None:
        audio_dict[word] = response_factory()

    threads: list[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return audio_dict