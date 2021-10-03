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
    return {word:get_audio_urls(word) for word in word_list}


def get_audio_urls(word: Kaki) -> List[URL]:
    api_url = get_api_url(word)
    return []


def get_api_url(word: Kaki) -> URL:
    url = \
        "https://apifree.forvo.com"\
        "/action/word-pronunciations"\
        "/format/json"\
        "/word/%s"\
        "/language/ja"\
        "/id_lang_speak/76"\
        "/key/%s"\
        % (word, API_KEY)
    return URL(url)
