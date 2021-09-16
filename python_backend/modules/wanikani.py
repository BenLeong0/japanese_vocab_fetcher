from typing import Dict, List


NAME = "wanikani"


def main(word_list: List[str]) -> Dict[str, List[str]]:
    print('wanikani fn')
    return {key:[] for key in word_list}
