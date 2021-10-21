from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<string:name>')
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io/?name={name}").json()
    age_response = requests.get(f"https://api.agify.io/?name={name}").json()
    return render_template("guess.html", name=name, gr=gender_response["gender"], ar=age_response["age"])


@app.route("/blog/<num>/<nana>")
def get_blog(num, nana):
    blog_url = "https://api.npoint.io/dc3892fcb84e83fc7eea"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(num)
    print(nana)
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
