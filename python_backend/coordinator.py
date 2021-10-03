from collections import defaultdict
from threading import Thread
from typing import Any, DefaultDict, Dict, List, Protocol

from custom_types import Kaki, FullResponse
from modules import forvo, jisho, ojad, suzuki, wadoku, wanikani


class Module(Protocol): # pylint: disable=too-few-public-methods
    NAME: str
    def main(self, word_list: List[Kaki]) -> Dict: ...


MODULES = (
    forvo,
    jisho,
    ojad,
    suzuki,
    wadoku,
    wanikani
)

def get_info(word_list: List[Kaki]) -> List[FullResponse]:
    results_dict = generate_results_dict(word_list)
    response = generate_response(results_dict, word_list)
    return response


def generate_results_dict(word_list: List[Kaki]) -> DefaultDict[str, Dict[Kaki, Any]]:
    results_dict: DefaultDict[str, Dict[Kaki, Any]] = defaultdict(dict)

    def call_script(module: Module, word_list: List[Kaki]) -> None:
        results_dict[module.NAME] = module.main(word_list)

    threads: List[Thread] = [
        Thread(target=call_script, args=[module, word_list])
        for module in MODULES
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return results_dict


def generate_response(
    results_dict: DefaultDict[str, Dict[Kaki, Any]],
    word_list: List[Kaki],
) -> List[FullResponse]:
    resp: List[FullResponse] = [{
        'word': word,
        'jisho': results_dict['jisho'][word],
        'accent': {
            'ojad': results_dict['ojad'][word],
            'suzuki': results_dict['suzuki'][word],
            'wadoku': results_dict['wadoku'][word],
        },
        "audio": {
            "forvo": results_dict['forvo'][word],
            "wanikani": results_dict['wanikani'][word],
        },
    } for word in word_list]
    return resp
