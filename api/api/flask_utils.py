import json
from typing import Any

from flask.wrappers import Request, Response

from api.custom_types.alternative_string_types import Kaki


def get_words_from_request(request: Request) -> list[Kaki]:
    dumped_word_list: str = request.args.get("words", "[]")
    word_list: list[Kaki] = json.loads(dumped_word_list)
    return word_list


def create_successful_response(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=200)


def create_failed_response(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=400)
