import json
from threading import Thread

import requests

from api.custom_types.alternative_string_types import URL, Kaki
from api.custom_types.exception_types import APIError
from api.custom_types.response_types import ContextSentence, ResponseItemTatoeba
from api.custom_types.tatoeba_api_types import TatoebaAPIResponse, TatoebaAPIResult

NAME = "tatoeba"

KANA_CONVERSIONS = {
    "う": ["わ", "い", "う", "え", "お", "っ"],
    "く": ["か", "き", "く", "け", "こ", "い"],
    "ぐ": ["が", "ぎ", "ぐ", "げ", "ご", "い"],
    "す": ["さ", "し", "す", "せ", "そ"],
    "つ": ["た", "ち", "つ", "て", "と", "っ"],
    "ぬ": ["な", "に", "ぬ", "ね", "の", "ん"],
    "ぶ": ["ば", "び", "ぶ", "べ", "ぼ", "ん"],
    "む": ["ま", "み", "む", "め", "も", "ん"],
    "る": ["ら", "り", "る", "れ", "ろ", "っ"],
}

ICHIDAN_PENULTIMATES = "いきぎしじちぢにひびぴみりえけげせぜてでねへべぺめれ"


class TatoebaAPIError(APIError):
    pass


def response_factory(
    sentence_list: list[ContextSentence] | None = None,
) -> ResponseItemTatoeba:
    return {
        "success": True,
        "error": None,
        "main_data": {
            "sentences": [] if sentence_list is None else sentence_list,
        },
    }


def error_response_factory(error: TatoebaAPIError) -> ResponseItemTatoeba:
    return {
        "success": False,
        "error": error.to_dict(),
        "main_data": {
            "sentences": [],
        },
    }


def main(word_list: list[Kaki]) -> dict[Kaki, ResponseItemTatoeba]:
    sentences_dict: dict[Kaki, ResponseItemTatoeba] = {}

    def call_script(word: Kaki) -> None:
        sentences_dict[word] = get_sentences(word)

    threads: list[Thread] = [
        Thread(target=call_script, args=[word]) for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return sentences_dict


def get_sentences(word: Kaki) -> ResponseItemTatoeba:
    try:
        response = call_api(word)
    except TatoebaAPIError as api_error:
        print("An error occurred:", api_error.error_msg)
        return error_response_factory(api_error)

    sentences = extract_sentences(response)
    return response_factory(sentences)


# Call API


def get_url_query(word: Kaki) -> str:
    if len(word) < 2:
        return word
    if word[-1] == "い":
        return word[:-1]
    if word[-1] == "る" and word[-2] in ICHIDAN_PENULTIMATES:
        return word[:-1]
    if word[-1] in KANA_CONVERSIONS:
        conjugations = [word[:-1] + suffix for suffix in KANA_CONVERSIONS[word[-1]]]
        return "%22|%22".join(conjugations)
    return word


def get_url(word: Kaki) -> URL:
    query = get_url_query(word)
    url = f"https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22{query}%22"
    return URL(url)


def call_api(word: Kaki) -> TatoebaAPIResponse:
    url = get_url(word)
    try:
        response = requests.get(url, timeout=20)
    except Exception:
        raise TatoebaAPIError("request failed", 500, url) from None

    status_code = response.status_code

    if status_code != 200:
        error_msg: str = response.text
        raise TatoebaAPIError(error_msg, status_code, url)

    response_data: TatoebaAPIResponse = json.loads(response.text)
    return response_data


# Extract sentences


def extract_sentence(result: TatoebaAPIResult) -> ContextSentence | None:
    translations = [
        translation
        for translation_group in result["translations"]
        for translation in translation_group
    ]
    if not translations:
        return None
    return {"ja": result["text"], "en": translations[0]["text"]}


def extract_sentences(response: TatoebaAPIResponse) -> list[ContextSentence]:
    sentences = [extract_sentence(result) for result in response["results"]]
    return [sentence for sentence in sentences if sentence is not None]
