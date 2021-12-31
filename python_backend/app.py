from flask import Flask, request
from flask_cors import CORS     # type: ignore

from coordinator import get_info
import utils

app = Flask("app")
CORS(app)


@app.route('/words', methods=['GET'])
def homepage():
    word_list = utils.get_words_from_request(request)
    resp = get_info(word_list)
    return utils.create_successful_response(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
