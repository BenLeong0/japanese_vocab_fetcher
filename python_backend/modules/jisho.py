from typing import Dict, List

from custom_types import Kaki


NAME = "jisho"

def main(word_list: List[Kaki]) -> Dict[Kaki, Dict]:
    return {key:{} for key in word_list}
