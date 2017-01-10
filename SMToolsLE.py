from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'I will inshaa Allah start my project.'


if __name__ == '__main__':
    app.run()
