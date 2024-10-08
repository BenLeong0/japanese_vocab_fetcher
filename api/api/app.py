from flask import Flask, request
from flask_cors import CORS  # type: ignore

from api import utils
from api.coordinator import get_info

app = Flask("app")
CORS(app)


@app.route("/words", methods=["GET"])
def homepage():
    word_list = utils.get_words_from_request(request)
    resp = get_info(word_list)
    return utils.create_successful_response(resp)


def lambda_handler(event, context):
    word_list = utils.get_words_from_lambda(event)
    resp = get_info(word_list)
    return resp


if __name__ == "__main__":
    # app.run(
    #     host='0.0.0.0', debug=True, port=5000, ssl_context=('cert.pem', 'key.pem')
    # )
    app.run(host="0.0.0.0", port=5000)
