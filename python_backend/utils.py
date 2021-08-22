import json

from flask.wrappers import Request


def get_words_from_request(request: Request):
    return json.loads(dict(request.args)['words'])
