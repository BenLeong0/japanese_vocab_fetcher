import json
import re
from typing import Any, Dict, List

from flask.wrappers import Request, Response

from custom_types import HTMLString, Kaki, URL, Yomi


def get_words_from_request(request: Request):
    return json.loads(request.data)['words']


def create_successful_response(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=200)


def create_failed_response(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=400)


def remove_punct(input_string: str) -> str:
    return re.sub(r'[\n￨･~]', '', input_string)


def make_single_line(input_string: str) -> str:
    return re.sub(r'\s{2,}', '', input_string)


def escape_unicode(word: Kaki) -> str:
    return word.encode("unicode-escape").decode()

def decode_unicode(word: str) -> Kaki:
    return Kaki(word.encode().decode("unicode-escape"))


def convert_list_of_str_to_kaki(input_list: List[str]) -> List[Kaki]:
    return list(map(Kaki, input_list))

def convert_list_of_str_to_yomi(input_list: List[str]) -> List[Yomi]:
    return list(map(Yomi, input_list))

def convert_list_of_str_to_url(input_list: List[str]) -> List[URL]:
    return list(map(URL, input_list))

def convert_list_of_str_to_htmlstring(input_list: List[str]) -> List[HTMLString]:
    return list(map(HTMLString, input_list))

def convert_dict_str_keys_to_kaki(input_dict: Dict[str, Any]) -> Dict[Kaki, Any]:
    return {Kaki(key): value for key, value in input_dict.items()}
