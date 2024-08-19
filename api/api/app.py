from flask import Flask, request
from flask_cors import CORS  # type: ignore

from api import flask_utils
from api.coordinator import get_info

app = Flask("app")
CORS(app)


@app.route("/words", methods=["GET"])
def homepage():
    word_list = flask_utils.get_words_from_request(request)
    resp = get_info(word_list)
    return flask_utils.create_successful_response(resp)


if __name__ == "__main__":
    # app.run(
    #     host='0.0.0.0', debug=True, port=5000, ssl_context=('cert.pem', 'key.pem')
    # )
    app.run(host="0.0.0.0", port=5000)
