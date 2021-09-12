import json
import re
from typing import Any

from flask.wrappers import Request, Response


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
