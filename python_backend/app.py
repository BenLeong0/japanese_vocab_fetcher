import json

from flask import Flask
from flask_cors import CORS

app = Flask("app")
CORS(app)


@app.route('/')
def homepage():
    return json.dumps("['yo']")


if __name__ == "__main__":
    print('Yo')
