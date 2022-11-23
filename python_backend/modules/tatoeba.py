from threading import Thread
from typing import Optional


from custom_types.alternative_string_types import Kaki
from custom_types.exception_types import APIError
from custom_types.response_types import ContextSentence, ResponseItemTatoeba


NAME = "tatoeba"


class TatoebaAPIError(APIError):
    pass


def response_factory(sentence_list: Optional[list[ContextSentence]] = None) -> ResponseItemTatoeba:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "sentences": [] if sentence_list is None else sentence_list,
        },
    }


def error_response_factory(error: TatoebaAPIError) -> ResponseItemTatoeba:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "sentences": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemTatoeba]:
    sentences_dict: dict[Kaki, ResponseItemTatoeba] = {}

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


def get_sentences(word: Kaki) -> ResponseItemTatoeba:
    print(word)
    return response_factory()
