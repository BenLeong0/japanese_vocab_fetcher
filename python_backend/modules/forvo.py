from typing import Dict, List


def get_audio_links(word_list: List[str]) -> Dict[str, List[str]]:
    return {key:[] for key in word_list}
