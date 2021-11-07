import json
import re
from typing import Any

from flask.wrappers import Request, Response

from custom_types.alternative_string_types import HTMLString, Kaki, URL, Yomi


def get_words_from_request(request: Request):
    print(request.args.get('words'))
    return json.loads(request.args.get('words'))


def create_successful_response(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=200)


def create_failed_response(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=400)


def make_single_line(input_string: str) -> str:
    return re.sub(r'\s{2,}', '', input_string)


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
    return {Kaki(key) : value for key, value in input_dict.items()}
