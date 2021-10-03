from typing import Dict, List

from dotenv import dotenv_values

from custom_types import Kaki, URL


NAME = "forvo"

def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    API_KEY: str = dotenv_values()['FORVO_API_KEY']
    return {key:[] for key in word_list}
