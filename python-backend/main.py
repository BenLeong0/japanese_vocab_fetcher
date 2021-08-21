from flask import Flask

app = Flask("app")


@app.route('/')
def homepage():
    return "<p>Yo</p>"


if __name__ == "__main__":
    print('Yo')
