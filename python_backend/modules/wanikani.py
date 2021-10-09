from collections import defaultdict
import json
from typing import DefaultDict, Dict, List

from dotenv import dotenv_values
import requests

from custom_types import Kaki, URL, ResponseItemWanikani, WanikaniAPIResponse
from utils import decode_unicode


NAME = "wanikani"
API_KEY: str = dotenv_values()['WANIKANI_API_KEY']


class WanikaniAPIError(Exception):
    def __init__(
        self,
        error_msg: str,
        status_code: str,
        url: URL = URL(""),
    ):
        super().__init__(error_msg)
        self.error_msg = error_msg
        self.status_code = status_code
        self.url = url


def main(word_list: List[Kaki]) -> Dict[Kaki, List[URL]]:
    if not word_list:
        return {}

    try:
        api_response = get_api_response(word_list)  # pylint: disable=unused-variable
    except WanikaniAPIError as api_error:
        # TODO: Refactor entire program to handle and return errors
        print("An error occurred:", api_error.error_msg)
        return {word:[] for word in word_list}

    result_dict = build_result_dict(api_response)

    return {word: result_dict[word] for word in word_list}


def get_api_response(word_list: List[Kaki]) -> WanikaniAPIResponse:
    url = get_url(word_list)
    response = call_api(url)
    return response


def get_url(word_list: List[Kaki]) -> URL:
    slugs = ','.join(word_list)
    url = f"https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs={slugs}"
    return URL(url)


def call_api(url: URL) -> WanikaniAPIResponse:
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = json.loads(response.text)["error"]
        raise WanikaniAPIError(error_msg, status_code, url)

    response_data: WanikaniAPIResponse = json.loads(response.text)
    return response_data


def build_result_dict(response: WanikaniAPIResponse) -> DefaultDict[Kaki, ResponseItemWanikani]:
    result_dict: DefaultDict[Kaki, ResponseItemWanikani] = defaultdict(list)

    for resource in response["data"]:
        writing = Kaki(decode_unicode(resource["data"]["characters"]))

        pronunciation_audios = [
            audio for audio in resource["data"]["pronunciation_audios"]
            if audio["content_type"] == "audio/mpeg"
        ]
        for audio in pronunciation_audios:
            audio["url"] = URL(audio["url"])

        context_sentences = resource["data"]["context_sentences"]
        for sentence in context_sentences:
            sentence["ja"] = decode_unicode(sentence["ja"])

        result_dict[writing] = {
            "audio": pronunciation_audios,
            "sentences": context_sentences
        }

    return result_dict
