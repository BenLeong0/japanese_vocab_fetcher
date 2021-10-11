import json
from threading import Thread
from typing import Dict, List

from dotenv import dotenv_values
import requests

from custom_types.alternative_string_types import Kaki, URL
from custom_types.exception_types import APIError
from custom_types.forvo_api_types import ForvoAPIItem, ForvoAPIResponse
from custom_types.response_types import ResponseItemForvo
from utils import decode_unicode


NAME = "forvo"
API_KEY: str = dotenv_values()['FORVO_API_KEY']


class ForvoAPIError(APIError):
    pass


def main(word_list: List[Kaki]) -> Dict[Kaki, ResponseItemForvo]:
    audio_urls_dict: Dict[Kaki, ResponseItemForvo] = {}

    def call_script(word: Kaki) -> None:
        audio_urls_dict[word] = get_audio_urls(word)

    threads: List[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return audio_urls_dict


def get_audio_urls(word: Kaki) -> ResponseItemForvo:
    try:
        response = call_api(word)
    except ForvoAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {"success": False, "audio": []}

    url_list = extract_audio_url_list(response, word)
    return {"success": True, "audio": url_list}


def call_api(word: Kaki) -> ForvoAPIResponse:
    api_url = get_api_url(word)
    response = requests.get(api_url)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = json.loads(response.text)["error"]
        raise ForvoAPIError(error_msg, status_code, api_url)

    response_data: ForvoAPIResponse = json.loads(response.text)
    return response_data


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


def extract_audio_url_list(response: ForvoAPIResponse, word: Kaki) -> List[URL]:
    items = response["items"]
    filtered_items = [item for item in items if correct_word(item, word)]
    return [extract_audio_url(item) for item in filtered_items]


def extract_audio_url(item: ForvoAPIItem) -> URL:
    url = item["pathmp3"]
    return URL(url)


def correct_word(item: ForvoAPIItem, word: Kaki) -> bool:
    return (
        word == item["word"] or
        word == decode_unicode(item["word"])
    )
