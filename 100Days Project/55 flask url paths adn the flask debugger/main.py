from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapping():
        html = function()
        return f"<b>{html}</b>"

    return wrapping


@app.route("/")
@make_bold
def imac():
    return '<h1 style="text-align: center">hi</h1>' \
           '<p>This is a paragraph.</p>'


@app.route("/hi/<int:name>/<path:where>")
def hello_world(name, where):
    return f"Hello {name + 12} form {where}!!"
    # http://127.0.0.1:5000/hi/12/sjfjlkw/sfwef/12


if __name__ == "__main__":
    app.run(debug=True)
