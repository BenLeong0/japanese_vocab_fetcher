from typing import Dict, List


def main(word_list: List[str]) -> Dict[str, Dict]:
    return {key:{} for key in word_list}
