from collections import defaultdict
import json
from typing import DefaultDict, Dict, List, Union

from dotenv import dotenv_values
import requests

from custom_types.alternative_string_types import Kaki, URL
from custom_types.exception_types import APIError, api_error_response_factory
from custom_types.response_types import FailedResponseItem, ResponseItemWanikani
from custom_types.wanikani_api_types import (
    WanikaniAPIResponse,
    WanikaniContextSentence,
    WanikaniPronunciationAudio,
)

NAME = "wanikani"
API_KEY: str = dotenv_values()['WANIKANI_API_KEY']
WanikaniModuleReturnTypes = Union[ResponseItemWanikani, FailedResponseItem]


def response_factory(
    audio_list: List[WanikaniPronunciationAudio] = None,
    sentence_list: List[WanikaniContextSentence] = None,
) -> ResponseItemWanikani:
    if audio_list is None:
        audio_list = []
    if sentence_list is None:
        sentence_list = []

    return {
        "success": True,
        "main_data": {
            "audio": audio_list,
            "sentences": sentence_list,
        },
    }


class WanikaniAPIError(APIError):
    pass


def main(word_list: List[Kaki]) -> Dict[Kaki, WanikaniModuleReturnTypes]:
    if not word_list:
        return {}

    try:
        api_response = get_api_response(word_list)  # pylint: disable=unused-variable
    except WanikaniAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word: api_error_response_factory(api_error) for word in word_list}

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
    result_dict: DefaultDict[Kaki, ResponseItemWanikani] = defaultdict(response_factory)

    for resource in response["data"]:
        writing = Kaki(resource["data"]["characters"])

        pronunciation_audios = [
            audio for audio in resource["data"]["pronunciation_audios"]
            if audio["content_type"] == "audio/mpeg"
        ]
        for audio in pronunciation_audios:
            audio["url"] = URL(audio["url"])

        context_sentences = resource["data"]["context_sentences"]

        result_dict[writing]['main_data']["audio"] += pronunciation_audios
        result_dict[writing]['main_data']["sentences"] += context_sentences

    return result_dict
