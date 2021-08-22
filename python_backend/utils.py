import json
from typing import Any

from flask.wrappers import Request, Response


def get_words_from_request(request: Request):
    return json.loads(dict(request.args)['words'])


def response_successful(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=200)

def response_failed(payload: Any):
    resp = json.dumps(payload)
    return Response(resp, status=400)
