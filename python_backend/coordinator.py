from collections import defaultdict
from threading import Thread
from typing import Any, DefaultDict, Dict, List

from modules import forvo, jisho, ojad, suzuki, wadoku, wanikani
from custom_types import Kaki, FullResponse


def get_info(word_list: List[Kaki]) -> List[FullResponse]:
    results_dict: DefaultDict[str, Dict[Kaki, Any]] = defaultdict(dict)

    def call_script(module_name, module_function, word_list: List[Kaki]):
        results_dict[module_name] = module_function(word_list)

    threads: List[Thread] = [
        Thread(target=call_script, args=["jisho", jisho.get_vocab_dict, word_list]),
        Thread(target=call_script, args=["ojad", ojad.get_accent_dict, word_list]),
        Thread(target=call_script, args=["suzuki", suzuki.get_accent_dict, word_list]),
        Thread(target=call_script, args=["wadoku", wadoku.get_accent_dict, word_list]),
        Thread(target=call_script, args=["forvo", forvo.get_audio_links, word_list]),
        Thread(target=call_script, args=["wanikani", wanikani.get_audio_links, word_list]),
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return generate_response(
        results_dict=results_dict,
        word_list=word_list,
    )


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
