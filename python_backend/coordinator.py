from enum import Enum
from collections import defaultdict
from threading import Thread
from typing import Dict, List

from modules import ojad, suzuki, wadoku

class Modules(Enum):
    OJAD = ojad
    SUZUKI = suzuki
    WADOKU = wadoku


class ModuleError(Exception):
    pass


def get_info(word_list: List[str]) -> Dict:
    results_dict = defaultdict(dict)

    def call_script(src: Modules):
        if src not in Modules:
            raise ModuleError(f"{src} is not a valid module")
        results_dict[src] = src.value.get_accent_dict(word_list)


    threads = [Thread(target=call_script, args=[module]) for module in Modules]
    print(threads)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(results_dict)

    return generate_response(
        word_list=word_list,
        ojad_dict=results_dict[Modules.OJAD],
        suzuki_dict=results_dict[Modules.SUZUKI],
        wadoku_dict=results_dict[Modules.WADOKU]
    )



def generate_response(
    word_list: List[str],
    ojad_dict: Dict[str,str],
    suzuki_dict: Dict[str,str],
    wadoku_dict: Dict[str,str],
):
    resp = [{
        'word': word,
        'accent': {
            'ojad': ojad_dict[word],
            'suzuki': suzuki_dict[word],
            'wadoku': wadoku_dict[word],
        },
    } for word in word_list]
    return resp
