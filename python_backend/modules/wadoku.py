from typing import Dict, List


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    return {key:[] for key in word_list}
