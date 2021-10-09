import json
from typing import Dict, List

from dotenv import dotenv_values
import requests

from custom_types import Kaki, URL, WanikaniAPIResponse


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
        return {key:[] for key in word_list}

    return {key:[] for key in word_list}


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
