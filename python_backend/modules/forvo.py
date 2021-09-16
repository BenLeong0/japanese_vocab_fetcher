from typing import Dict, List


NAME = "forvo"


def main(word_list: List[str]) -> Dict[str, List[str]]:
    return {key:[] for key in word_list}
