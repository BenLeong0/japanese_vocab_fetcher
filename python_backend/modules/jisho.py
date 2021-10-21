from typing import Dict, List

from custom_types.alternative_string_types import Kaki
from custom_types.response_types import ResponseItemJisho


NAME = "jisho"


def result_factory(success: bool = True) -> ResponseItemJisho:
    return {
        "success": success,
        "main_data": {
        },
    }

def main(word_list: List[Kaki]) -> Dict[Kaki, ResponseItemJisho]:
    return {key:result_factory() for key in word_list}
