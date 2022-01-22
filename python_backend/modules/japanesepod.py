from threading import Thread
from typing import Optional

import requests

from custom_types.alternative_string_types import HTMLString, Kaki, URL
from custom_types.exception_types import APIError
from custom_types.response_types import JapanesePodAudio, ResponseItemJapanesePod


NAME = "japanesepod"


class JapanesePodAPIError(APIError):
    pass


def response_factory(
    audio_list: Optional[list[JapanesePodAudio]] = None
) -> ResponseItemJapanesePod:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "audio": [] if audio_list is None else audio_list,
        },
    }


def error_response_factory(error: JapanesePodAPIError) -> ResponseItemJapanesePod:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "audio": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemJapanesePod]:
    audio_dict: dict[Kaki, ResponseItemJapanesePod] = {}

    def call_script(word: Kaki) -> None:
        audio_dict[word] = get_audio_urls()

    threads: list[Thread] = [
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return audio_dict


def get_audio_urls(word: Kaki) -> ResponseItemJapanesePod:
    try:
        html = get_html_string(word)
    except JapanesePodAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return error_response_factory(api_error)

    return response_factory()


# Get HTML

def get_url(word: Kaki) -> URL:
    url = f"https://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ{word}"
    return URL(url)


def get_html_string(word: Kaki) -> HTMLString:
    url = get_url(word)
    response = requests.get(url, timeout=20)
    status_code = response.status_code

    if status_code != 200:
        error_msg: str = response.text
        raise JapanesePodAPIError(error_msg, status_code, url)

    html = HTMLString(response.text)
    return html
