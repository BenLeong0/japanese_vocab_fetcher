from typing import Dict, List


def get_vocab_dict(word_list: List[str]) -> Dict[str, Dict]:
    return {key:{} for key in word_list}
