from typing import Dict, List, Union

from custom_types.alternative_string_types import Kaki
from custom_types.exception_types import FailedResponseItem
from custom_types.response_types import ResponseItemJisho


NAME = "jisho"
JishoModuleReturnTypes = Union[ResponseItemJisho, FailedResponseItem]


def response_factory(success: bool = True) -> ResponseItemJisho:
    return {
        "success": success,
        "main_data": {
        },
    }

def main(word_list: List[Kaki]) -> Dict[Kaki, JishoModuleReturnTypes]:
    return {key:response_factory() for key in word_list}
