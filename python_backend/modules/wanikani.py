from typing import Dict, List

from custom_types import Kaki, URL


NAME = "wanikani"

def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    return {key:[] for key in word_list}
