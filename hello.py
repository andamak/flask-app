from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'У меня получилось!? Работает 2021 01 28 11:35'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
