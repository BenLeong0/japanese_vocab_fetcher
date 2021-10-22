from functools import partial
import json
from threading import Thread
from typing import Dict, List, Union

import requests

from custom_types.alternative_string_types import Kaki, URL
from custom_types.exception_types import APIError, FailedResponseItem, api_error_response_factory
from custom_types.jisho_api_types import JishoAPIItem, JishoAPIResponse
from custom_types.response_types import ResponseItemJisho, JishoExtraItem, JishoMainData


NAME = "jisho"
JishoModuleReturnTypes = Union[ResponseItemJisho, FailedResponseItem]


def response_factory(data: JishoMainData) -> ResponseItemJisho:
    return {
        "success": True,
        "main_data": data,
    }


class JishoAPIError(APIError):
    pass


def main(word_list: List[Kaki]) -> Dict[Kaki, JishoModuleReturnTypes]:
    results_dict: Dict[Kaki, JishoModuleReturnTypes] = {}

    def call_script(word: Kaki) -> None:
        results_dict[word] = get_jisho_data(word)

    threads: List[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return results_dict


def get_jisho_data(word: Kaki) -> JishoModuleReturnTypes:
    try:
        response = call_api(word)
    except JishoAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return api_error_response_factory(api_error)

    data = extract_jisho_data(response, word)
    return response_factory(data)


def get_api_url(word: Kaki) -> URL:
    url = f"https://jisho.org/api/v1/search/words?keyword={word}"
    return URL(url)


def call_api(word: Kaki) -> JishoAPIResponse:
    url = get_api_url(word)
    response = requests.get(url)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = json.loads(response.text)["error"]
        raise JishoAPIError(error_msg, status_code, url)

    response_data: JishoAPIResponse = json.loads(response.text)
    meta_data = response_data["meta"]
    meta_data_status_code = meta_data["status"]

    if meta_data_status_code != 200:
        internal_error_msg: str = "An error occurred. Meta data: " + json.dumps(meta_data)
        raise JishoAPIError(internal_error_msg, meta_data_status_code, url)

    return response_data


def convert_to_extra_item(item: JishoAPIItem) -> JishoExtraItem:
    return {
        "slug": item["slug"],
        "japanese": item["japanese"]
    }


def segregate_items(
    items: list[JishoAPIItem],
    word: Kaki
) -> tuple[list[JishoAPIItem], list[JishoExtraItem]]:
    matching_items: list[JishoAPIItem] = []
    extra_items: list[JishoExtraItem] = []

    def item_is_matching(item: JishoAPIItem, word: Kaki) -> bool:
        for japanese in item["japanese"]:
            if (
                ("word" in japanese and word == japanese["word"]) or
                ("reading" in japanese and word == japanese["reading"])
            ):
                return True
        return False

    for item in items:
        if item_is_matching(item, word):
            matching_items.append(item)
        else:
            converted_item = convert_to_extra_item(item)
            extra_items.append(converted_item)

    return matching_items, extra_items


def extract_jisho_data(response: JishoAPIResponse, word: Kaki) -> JishoMainData:
    items: list[JishoAPIItem] = response["data"]
    matching_items, extra_items = segregate_items(items, word)
    return {"results": matching_items, "extra": extra_items}
