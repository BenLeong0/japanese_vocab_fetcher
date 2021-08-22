import json

from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS

import utils

app = Flask("app")
CORS(app)


@app.route('/words')
def homepage():
    print(utils.get_words_from_request(request))
    return utils.response_successful(['yo'])


if __name__ == "__main__":
    print('Yo')
