from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye_bye():
    return 'Bye'


"C:/Users/User/Desktop/coding/python/code place/100Days Project/54 flask & function decorator/hello.py"

if __name__ == "__main__":
    app.run()
