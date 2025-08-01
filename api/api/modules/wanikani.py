import json
from collections import defaultdict

import requests
from dotenv import dotenv_values

from api.custom_types.alternative_string_types import URL, Kaki
from api.custom_types.exception_types import APIError
from api.custom_types.response_types import ResponseItemWanikani
from api.custom_types.wanikani_api_types import (
    WanikaniAPIResponse,
    WanikaniContextSentence,
    WanikaniPronunciationAudio,
)

NAME = "wanikani"
API_KEY: str = dotenv_values()["WANIKANI_API_KEY"]


class WanikaniAPIError(APIError):
    pass


def response_factory(
    audio_list: list[WanikaniPronunciationAudio] | None = None,
    sentence_list: list[WanikaniContextSentence] | None = None,
) -> ResponseItemWanikani:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "audio": [] if audio_list is None else audio_list,
            "sentences": [] if sentence_list is None else sentence_list,
        },
    }


def error_response_factory(error: WanikaniAPIError) -> ResponseItemWanikani:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "audio": [],
            "sentences": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemWanikani]:
    if not word_list:
        return {}

    try:
        api_response = get_api_response(word_list)  # pylint: disable=unused-variable
    except WanikaniAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return {word: error_response_factory(api_error) for word in word_list}

    result_dict = build_result_dict(api_response)

    return {word: result_dict[word] for word in word_list}


def get_api_response(word_list: list[Kaki]) -> WanikaniAPIResponse:
    url = get_url(word_list)
    response = call_api(url)
    return response


def get_url(word_list: list[Kaki]) -> URL:
    slugs = ",".join(word_list)
    url = f"https://api.wanikani.com/v2/subjects/?types=vocabulary&slugs={slugs}"
    return URL(url)


def call_api(url: URL) -> WanikaniAPIResponse:
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get(url, headers=headers)
    except Exception:
        raise WanikaniAPIError("request failed", 500, url) from None
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = response.text
        raise WanikaniAPIError(error_msg, status_code, url)

    response_data: WanikaniAPIResponse = json.loads(response.text)
    return response_data


def build_result_dict(
    response: WanikaniAPIResponse,
) -> defaultdict[Kaki, ResponseItemWanikani]:
    result_dict: defaultdict[Kaki, ResponseItemWanikani] = defaultdict(response_factory)

    for resource in response["data"]:
        writing = Kaki(resource["data"]["characters"])

        pronunciation_audios = [
            audio
            for audio in resource["data"]["pronunciation_audios"]
            if audio["content_type"] == "audio/mpeg"
        ]
        for audio in pronunciation_audios:
            audio["url"] = URL(audio["url"])

        context_sentences: list[WanikaniContextSentence] = resource["data"][
            "context_sentences"
        ]

        result_dict[writing]["main_data"]["audio"] += pronunciation_audios
        result_dict[writing]["main_data"]["sentences"] += context_sentences

    return result_dict
