from collections import defaultdict
from enum import Enum
from threading import Thread
from typing import Any, DefaultDict, Dict, List

from modules import forvo, jisho, ojad, suzuki, wadoku
from custom_types import 書方, 読方, FullResponse

class Modules(Enum):
    OJAD = ojad
    SUZUKI = suzuki
    WADOKU = wadoku
    FORVO = forvo
    JISHO = jisho

    def get_info(self, word_list: List[書方]) -> Dict[書方, List]:
        if self.name in ('OJAD', 'SUZUKI', 'WADOKU'):
            return self.value.get_accent_dict(word_list)
        if self.name in ('FORVO', ):
            return self.value.get_audio_links(word_list)
        if self.name in ('JISHO', ):
            return self.value.get_vocab_data(word_list)
        raise ModuleError()


class ModuleError(Exception):
    pass


def get_info(word_list: List[書方]) -> List[FullResponse]:
    results_dict: DefaultDict[Modules, Dict[書方, Any]] = defaultdict(dict)

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
    word_list: List[書方],
    ojad_dict: Dict[書方, List[読方]],
    suzuki_dict: Dict[書方, List[読方]],
    wadoku_dict: Dict[書方, List[読方]],
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
