from flask import Flask, request
from flask_cors import CORS

import utils
from coordinator import get_info

app = Flask("app")
CORS(app)


@app.route('/words', methods=['GET'])
def homepage():
    word_list = utils.get_words_from_request(request)
    resp = get_info(word_list)
    print(resp)
    return utils.create_successful_response(resp)


if __name__ == "__main__":
    print('Yo')
