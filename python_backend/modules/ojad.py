from typing import Dict, List


def get_accent_dict(word_list: List[str]) -> Dict[str, List[str]]:
    if not word_list:
        return {}

    return {key:[] for key in word_list}
