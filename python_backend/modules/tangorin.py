from threading import Thread
from typing import Optional

from custom_types.alternative_string_types import Kaki
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


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemTangorin]:
    sentences_dict: dict[Kaki, ResponseItemTangorin] = {}

    def call_script(word: Kaki) -> None:
        sentences_dict[word] = get_sentences(word)

    threads: list[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return sentences_dict


def get_sentences(word: Kaki) -> ResponseItemTangorin:
    try:
        html = get_html(word)
    except TangorinAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return error_response_factory(api_error)

    sentence_sections = get_sections(html)
    sentence_list = build_sentence_list(sentence_sections)
    return response_factory(sentence_list)


# Get HTML

def get_html(*_):
    return


# Extract sections

def get_sections(*_):
    return


# Build sentence lists

def build_sentence_list(*_):
    return
