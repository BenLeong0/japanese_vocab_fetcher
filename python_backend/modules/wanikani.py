from typing import Dict, List

from dotenv import dotenv_values

from custom_types import Kaki, URL, WanikaniAPIResponse


NAME = "wanikani"
API_KEY: str = dotenv_values()['WANIKANI_API_KEY']

def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    if not word_list:
        return {}

    api_response = get_api_response(word_list)

    return {key:[] for key in word_list}


def get_api_response(word_list: List[Kaki]) -> WanikaniAPIResponse:
    url = get_url(word_list)


def get_url(word_list: List[Kaki]) -> URL:
    slugs = ','.join(word_list)
    url = f"https://api.wanikani.com/v2/subjects/?slugs={slugs}"
    return URL(url)
