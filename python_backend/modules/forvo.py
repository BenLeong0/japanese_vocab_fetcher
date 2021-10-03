import os
from typing import Dict, List

from dotenv import dotenv_values

from custom_types import Kaki, URL


NAME = "forvo"

if os.path.exists(".env"):
    API_KEY: str = dotenv_values()['FORVO_API_KEY']
else:
    API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    return {key:[] for key in word_list}
