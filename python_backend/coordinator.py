from collections import defaultdict
from threading import Thread
from typing import Any, DefaultDict, Protocol

from custom_types.alternative_string_types import Kaki
from custom_types.response_types import FullResponseItem
from modules import forvo, japanesepod, jisho, ojad, suzuki, tangorin, tatoeba, wadoku, wanikani


class Module(Protocol): # pylint: disable=too-few-public-methods
    NAME: str
    def main(self, word_list: list[Kaki]) -> dict: ...


MODULES = (
    forvo,
    japanesepod,
    jisho,
    ojad,
    suzuki,
    tangorin,
    tatoeba,
    wadoku,
    wanikani,
)

def get_info(word_list: list[Kaki]) -> list[FullResponseItem]:
    results_dict = generate_results_dict(word_list)
    response = generate_response(results_dict, word_list)
    return response


def generate_results_dict(word_list: list[Kaki]) -> DefaultDict[str,dict[Kaki, Any]]:
    results_dict: DefaultDict[str,dict[Kaki, Any]] = defaultdict(dict)

    def call_script(module: Module, word_list: list[Kaki]) -> None:
        results_dict[module.NAME] = module.main(word_list)

    threads: list[Thread] = [
        Thread(target=call_script, args=[module, word_list])
        for module in MODULES
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return results_dict


def generate_response(
    results_dict: DefaultDict[str,dict[Kaki, Any]],
    word_list: list[Kaki],
) -> list[FullResponseItem]:
    resp: list[FullResponseItem] = [
        {'word' : word} |   # type: ignore
        {module.NAME : results_dict[module.NAME][word] for module in MODULES}   # type: ignore
        for word in word_list
    ]
    return resp
