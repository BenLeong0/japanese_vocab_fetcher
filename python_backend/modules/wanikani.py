from typing import Dict, List

from dotenv import dotenv_values

from custom_types import Kaki, URL


NAME = "wanikani"
API_KEY: str = dotenv_values()['WANIKANI_API_KEY']

def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    return {key:[] for key in word_list}
