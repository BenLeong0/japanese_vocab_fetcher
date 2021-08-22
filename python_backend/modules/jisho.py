from typing import Dict, List


def get_vocab_data(word_list: List[str]) -> Dict[str, List[Dict]]:
    return {key:[] for key in word_list}
