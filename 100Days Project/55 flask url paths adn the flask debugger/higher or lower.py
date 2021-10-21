from flask import Flask
import random

ans = random.randint(1, 10)
print(ans)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1><br>' \
           '<img src="https://memeguy.com/photos/images/those-are-some-useful-workout-moves-82862.gif">'


@app.route("/<int:guess>")
def user_guess(guess):
    if guess > ans:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < ans:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
