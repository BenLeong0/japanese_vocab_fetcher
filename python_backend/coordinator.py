from collections import defaultdict
from enum import Enum
from threading import Thread
from typing import Any, DefaultDict, Dict, List

from modules import forvo, jisho, ojad, suzuki, wadoku
from custom_types import kaki, yomi, FullResponse

class Modules(Enum):
    OJAD = ojad
    SUZUKI = suzuki
    WADOKU = wadoku
    FORVO = forvo
    JISHO = jisho

    def get_info(self, word_list: List[kaki]) -> Dict[kaki, List]:
        if self.name in ('OJAD', 'SUZUKI', 'WADOKU'):
            return self.value.get_accent_dict(word_list)
        if self.name in ('FORVO', ):
            return self.value.get_audio_links(word_list)
        if self.name in ('JISHO', ):
            return self.value.get_vocab_data(word_list)
        raise ModuleError()


class ModuleError(Exception):
    pass


def get_info(word_list: List[kaki]) -> List[FullResponse]:
    results_dict: DefaultDict[Modules, Dict[kaki, Any]] = defaultdict(dict)

    def call_script(src: Modules):
        if src not in Modules:
            raise ModuleError(f"{src} is not a valid module")
        results_dict[src] = src.get_info(word_list)


    threads = [Thread(target=call_script, args=[module]) for module in Modules]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return generate_response(
        word_list=word_list,
        ojad_dict=results_dict[Modules.OJAD],
        suzuki_dict=results_dict[Modules.SUZUKI],
        wadoku_dict=results_dict[Modules.WADOKU]
    )



def generate_response(
    word_list: List[kaki],
    ojad_dict: Dict[kaki, List[yomi]],
    suzuki_dict: Dict[kaki, List[yomi]],
    wadoku_dict: Dict[kaki, List[yomi]],
) -> List[FullResponse]:
    resp: List[FullResponse] = [{
        'word': word,
        'jisho': {},
        'accent': {
            'ojad': ojad_dict[word],
            'suzuki': suzuki_dict[word],
            'wadoku': wadoku_dict[word],
        },
        "audio": {
            "forvo": [],
            "wanikani": [],
        },
    } for word in word_list]
    return resp
