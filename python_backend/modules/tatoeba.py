from threading import Thread
from typing import cast, Optional


from custom_types.alternative_string_types import Kaki, URL
from custom_types.exception_types import APIError
from custom_types.response_types import ContextSentence, ResponseItemTatoeba


NAME = "tatoeba"


class TatoebaAPIError(APIError):
    pass


def response_factory(sentence_list: Optional[list[ContextSentence]] = None) -> ResponseItemTatoeba:
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
        Thread(target=call_script, args=[word])
        for word in word_list
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return sentences_dict


def get_sentences(word: Kaki) -> ResponseItemTatoeba:
    print(word)
    return response_factory()


# Call API

def get_url_query(word: Kaki) -> str:
    if len(word) < 2:
        return cast(str, word)
    if word[-1] == "る" and word[-2] in ICHIDAN_PENULTIMATES:
        return word[:-1]
    if word[-1] in KANA_CONVERSIONS:
        conjugations = [word[:-1] + suf for suf in KANA_CONVERSIONS[word[-1]]]
        return "|".join(conjugations)
    return cast(str, word)


def get_url(word: Kaki) -> URL:
    query = get_url_query(word)
    url = f"https://tatoeba.org/en/api_v0/search?from=jpn&to=eng&query=%3D%22{query}%22"
    return URL(url)


# Helpers

KANA_CONVERSIONS = {
    "う": {"わ", "い", "う", "え", "お", "っ"},
    "く": {"か", "き", "く", "け", "こ", "い"},
    "ぐ": {"が", "ぎ", "ぐ", "げ", "ご", "い"},
    "す": {"さ", "し", "す", "せ", "そ", "し"},
    "つ": {"た", "ち", "つ", "て", "と", "っ"},
    "ぬ": {"な", "に", "ぬ", "ね", "の", "ん"},
    "ぶ": {"ば", "び", "ぶ", "べ", "ぼ", "ん"},
    "む": {"ま", "み", "む", "め", "も", "ん"},
    "る": {"ら", "り", "る", "れ", "ろ", "っ"},
}

ICHIDAN_PENULTIMATES = "えいけきげぎせしてちねにへひめみれり"
