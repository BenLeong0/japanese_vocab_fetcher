import json
import os
from typing import Dict, List

from dotenv import dotenv_values
import requests

from custom_types import Kaki, URL, ForvoAPIResponse


NAME = "forvo"

if os.path.exists(".env"):
    API_KEY: str = dotenv_values()['FORVO_API_KEY']
else:
    API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    return {word:get_audio_urls(word) for word in word_list}


def get_audio_urls(word: Kaki) -> List[URL]:
    response = call_api(word)
    return []


def call_api(word: Kaki) -> ForvoAPIResponse:
    api_url = get_api_url(word)
    response: ForvoAPIResponse = json.loads(requests.get(api_url).text)
    return response


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
