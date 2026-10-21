import json
import re
from typing import Any

from api.custom_types.alternative_string_types import URL, HTMLString, Kaki, Yomi


def get_words_from_lambda(event: dict[str, dict[str, str]]) -> list[Kaki]:
    query_params = event["queryStringParameters"]
    dumped_word_list = query_params.get("words", "[]")
    word_list: list[Kaki] = json.loads(dumped_word_list)
    return word_list


def parse_words_body(body: Any) -> tuple[list[Kaki], list[str] | None]:
    """
    Validate a POST /words body of the form {"words": [...], "sources": [...]}
    and return the word list and (optional) list of sources
    """
    if not isinstance(body, dict):
        raise ValueError("Body must be a JSON object")
    words = body.get("words")
    if not isinstance(words, list) or not all(isinstance(w, str) for w in words):
        raise ValueError("'words' must be a list of strings")
    sources = body.get("sources")
    if sources is not None and (
        not isinstance(sources, list) or not all(isinstance(s, str) for s in sources)
    ):
        raise ValueError("'sources' must be a list of strings")
    word_list = [Kaki(w.strip()) for w in words if w.strip()]
    return word_list, sources


def make_single_line(input_string: str) -> str:
    return re.sub(r"\s{2,}", "", input_string)


def remove_end_brackets(input_string: str) -> str:
    if "(" not in input_string:
        return input_string
    return input_string[: input_string.index("(")]


def escape_unicode(word: Kaki) -> str:
    return word.encode("unicode-escape").decode()


def decode_unicode(word: str) -> Kaki:
    return Kaki(word.encode().decode("unicode-escape"))


def convert_list_of_str_to_kaki(input_list: list[str]) -> list[Kaki]:
    return list(map(Kaki, input_list))


def convert_list_of_str_to_yomi(input_list: list[str]) -> list[Yomi]:
    return list(map(Yomi, input_list))


def convert_list_of_str_to_url(input_list: list[str]) -> list[URL]:
    return list(map(URL, input_list))


def convert_list_of_str_to_htmlstring(input_list: list[str]) -> list[HTMLString]:
    return list(map(HTMLString, input_list))


def convert_dict_str_keys_to_kaki(input_dict: dict[str, Any]) -> dict[Kaki, Any]:
    return {Kaki(key): value for key, value in input_dict.items()}
