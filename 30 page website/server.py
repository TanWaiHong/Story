import random
from datetime import datetime, timedelta
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal-data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(250), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    kind = db.Column(db.Integer, nullable=False)
    post = db.Column(db.Integer, nullable=False)
    online = db.Column(db.Boolean, nullable=False)
    intro = db.Column(db.String(250), nullable=False)
    gmail = db.Column(db.String(250), nullable=False)
    birth = db.Column(db.String(250), nullable=False)
    img = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Person {self.id}>'


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    time = db.Column(db.String(250), nullable=False)
    post = db.Column(db.String(500), nullable=False)
    liked = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Blog {self.id}>'


class Game1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bet = db.Column(db.Integer, nullable=False)
    choice = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Game1 {self.id}>'


class LastTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(250), nullable=True)


db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class RpsEditForm(FlaskForm):
    rating = StringField("Your bet score (should be lower than your current score)")
    review = StringField("Your Review")
    choice = StringField("Choose rock paper or scissors(should be 0, 5 or 2)")
    submit = SubmitField("Done")


class RpsBetForm(FlaskForm):
    choice = StringField("Choose rock paper or scissors(should be 0, 5 or 2)")
    submit = SubmitField("Done")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


def random_number(a, b):
    num = random.randint(a, b)
    return num


def find_the_special(the_type):
    if the_type == "rich":
        score_dict = {person.id: person.score for person in Person.query.all()}
        rich_dict = sorted(score_dict, key=score_dict.get, reverse=True)[:3]
        return [Person.query.get(the_id) for the_id in rich_dict]
    elif the_type == "poor":
        score_dict = {person.id: person.score for person in Person.query.all()}
        rich_dict = sorted(score_dict, key=score_dict.get)[:3]
        return [Person.query.get(the_id) for the_id in rich_dict]


# homepage
@app.route('/SomeFunction/', methods=["POST", "GET"])
def SomeFunction():
    num = request.args.get("num")
    the_id = request.args.get("the_id")
    if num == "1":
        person = Person.query.get(the_id)
        person.score += 200
        person.online = False
        db.session.commit()
        db.session.commit()
        return redirect(url_for("user_logged_in", the_id=the_id))
    elif num == "2":
        today = datetime.today() + timedelta(hours=8)
        person = Person.query.get(the_id)
        new_blog = Blog(
            name=person.id,
            time=today.strftime("%b %d %Y, %X"),
            post=request.form['user-post'],
            liked="0"
        )
        person.post += 1
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for("user_logged_in", the_id=the_id))
    elif num == "3":
        person = Person.query.get(the_id)
        person.post -= 1
        post_id = request.args.get("post_id")
        blog = Blog.query.get(post_id)
        db.session.delete(blog)
        db.session.commit()
        return redirect(url_for("user_logged_in", the_id=the_id))
    elif num == "4":
        update_person = Person.query.get(the_id)
        update_person.intro = request.form['user-post']
        db.session.commit()
        return redirect(url_for("user_logged_in", the_id=the_id))
    elif num == '5':
        person = Person.query.get(the_id)
        if person.score >= 500:
            if person.kind < 7:
                person.kind += 1
            person.score -= 500
            db.session.commit()
        return redirect(url_for("user_logged_in", the_id=the_id))
    elif num == '6':
        post_id = request.args.get("post_id")
        blog = Blog.query.get(post_id)
        blog.liked = f"{int(blog.liked) + 1}"
        db.session.commit()
        return redirect(url_for("user_logged_in", the_id=the_id))


@app.route('/')
def user_welcome():
    return redirect(url_for("user_logged_in", the_id="none"))


@app.route('/logged-in/')
def user_logged_in():
    if LastTime.query.get(1).time != f'{datetime.today().day}':
        LastTime.query.get(1).time = f'{datetime.today().day}'
        for person_ in Person.query.all():
            person_.online = True
        db.session.commit()
    the_id = request.args.get('the_id')
    rich_list = find_the_special("rich")
    poor_list = find_the_special("poor")
    date_list = list()
    date_list.append(datetime.today().strftime("%d"))
    date_list.append(datetime.today().strftime("%B"))
    date_list.append(datetime.today().strftime("%Y"))
    personal_data = Person.query.all()
    return render_template(
        "index.html",
        pd=personal_data,
        rn=random_number,
        rl=rich_list,
        pl=poor_list,
        dl=date_list,
        tui=the_id,
        bo=Blog.query.all(),
        int=int
    )


@app.route('/profile/')
def user_profile():
    the_id = request.args.get('the_id')
    person_id = request.args.get('person_id')
    person = Person.query.get(person_id)
    return render_template(
        "profile.html",
        person=person,
        rn=random_number,
        the_id=the_id,
        int=int
    )


@app.route('/login-page', methods=["GET", "POST"])
def user_login():
    if request.method == 'POST':
        the_id = request.form['input-id']
        the_password = request.form['input-password']
        try:
            real_password = Person.query.get(the_id).password
        except AttributeError:
            return render_template("login.html", state="wrong")
        else:
            if real_password == "waiting":
                Person.query.get(the_id).password = the_password
                db.session.commit()
                return redirect(url_for("user_logged_in", the_id=the_id))
            else:
                if real_password == the_password:
                    return redirect(url_for("user_logged_in", the_id=the_id))
                else:
                    return render_template("login.html", state="wrong")
    return render_template("login.html", state="new")


@app.route('/set-intro')
def set_intro():
    the_id = request.args.get('the_id')
    person = Person.query.get(the_id)
    return render_template("set.html", person=person)


# rock paper scissors

@app.route('/r-p-s/')
def rps_home():
    the_id = request.args.get('the_id')
    all_deal = Game1.query.order_by(Game1.bet).all()
    did_the_id_beted = Game1.query.get(the_id)
    if did_the_id_beted is None:
        no_bet = True
    else:
        no_bet = False
    return render_template("rps-index.html", the_id=the_id, ad=all_deal, int=int, no_bet=no_bet)


@app.route("/rps-edit/", methods=["GET", "POST"])
def rps_edit():
    the_id = request.args.get('the_id')
    person = Person.query.get(the_id)
    form = RpsEditForm()
    deal_id = request.args.get("id")
    deal = Game1.query.get(deal_id)
    if form.validate_on_submit():
        if (form.choice.data == "0" or form.choice.data == "2" or form.choice.data == "5") \
                and 0 < int(form.rating.data) <= person.score:
            deal.bet = int(form.rating.data)
            deal.review = f'"{form.review.data}" by {person.name}'
            deal.choice = int(form.choice.data)
            db.session.commit()
            return redirect(url_for('rps_home', the_id=the_id))
        else:
            return render_template("rps-rate.html", deal=deal, form=form, the_id=the_id, person=person)
    return render_template("rps-rate.html", deal=deal, form=form, the_id=the_id, person=person)


@app.route("/rps-delete/")
def delete_rps():
    the_id = request.args.get('the_id')
    deal_id = request.args.get("id")
    deal = Game1.query.get(deal_id)
    db.session.delete(deal)
    db.session.commit()
    return redirect(url_for("rps_home", the_id=the_id))


@app.route("/rps-new/", methods=["GET", "POST"])
def new_rps():
    the_id = request.args.get('the_id')
    person = Person.query.get(the_id)
    form = RpsEditForm()
    if form.validate_on_submit():
        if (form.choice.data == "0" or form.choice.data == "2" or form.choice.data == "5") \
                and 0 < int(form.rating.data) <= person.score:
            new_deal = Game1(
                id=person.id,
                bet=int(form.rating.data),
                choice=int(form.choice.data),
                review=f'"{form.review.data}" by {person.name}',
                img_url=person.img,
            )
            today = datetime.today() + timedelta(hours=8)
            new_blog = Blog(
                name=person.id,
                time=today.strftime("%b %d %Y, %X"),
                liked="0",
                post=f"I create {new_deal.bet} score to bet.\n{form.review.data}",
            )
            person.post += 1
            db.session.add(new_blog)
            db.session.add(new_deal)
            db.session.commit()
            return redirect(url_for('rps_home', the_id=the_id))
        else:
            return render_template("rps-new.html", form=form, the_id=the_id, person=person)
    return render_template("rps-new.html", form=form, the_id=the_id, person=person)


@app.route("/rps-bet/", methods=["GET", "POST"])
def rps_bet():
    the_id = request.args.get('the_id')
    person = Person.query.get(the_id)
    deal_id = request.args.get("id")
    deal = Game1.query.get(deal_id)
    if person.score < deal.bet:
        return redirect(url_for('rps_home', the_id=the_id))
    form = RpsBetForm()
    if form.validate_on_submit():
        if form.choice.data == "0" or form.choice.data == "2" or form.choice.data == "5":
            mc = int(form.choice.data)
            return redirect(url_for('result_rps', the_id=the_id, mc=mc, id=deal.id))
        else:
            return render_template("rps-bet.html", deal=deal, form=form, the_id=the_id)
    return render_template("rps-bet.html", deal=deal, form=form, the_id=the_id)


@app.route("/rps-result/")
def result_rps():
    the_id = request.args.get('the_id')
    deal_id = request.args.get("id")
    deal = Game1.query.get(deal_id)
    mc = int(request.args.get('mc'))
    person = Person.query.get(the_id)
    deal_person = Person.query.get(deal.id)
    today = datetime.today() + timedelta(hours=8)
    if mc == deal.choice:
        new_blog = Blog(
            name=person.id,
            time=today.strftime("%b %d %Y, %X"),
            post=f"I tied on a {deal.bet} score bet with {deal_person.name}.",
            liked="0"
        )
        person.post += 1
        db.session.add(new_blog)
        db.session.delete(deal)
        db.session.commit()
        return render_template("rps-result.html", deal=deal, the_id=the_id, result=2)
    elif mc == 0 and int(deal.choice) == 2 or mc == 2 and int(deal.choice) == 5 or mc == 5 and int(deal.choice) == 0:
        person.score += deal.bet
        deal_person.score -= deal.bet
        new_blog = Blog(
            name=person.id,
            time=today.strftime("%b %d %Y, %X"),
            post=f"I winning {deal.bet} score from {deal_person.name}!!",
            liked="0"
        )
        person.post += 1
        db.session.add(new_blog)
        db.session.delete(deal)
        db.session.commit()
        return render_template("rps-result.html", deal=deal, the_id=the_id, result=0)
    else:
        person.score -= deal.bet
        deal_person.score += deal.bet
        new_blog = Blog(
            name=person.id,
            time=today.strftime("%b %d %Y, %X"),
            liked="0",
            post=f"I losing {deal.bet} score to {deal_person.name}...",
        )
        person.post += 1
        db.session.add(new_blog)
        db.session.delete(deal)
        db.session.commit()
        return render_template("rps-result.html", deal=deal, the_id=the_id, result=1)


# movies
@app.route("/movies/")
def home():
    the_id = request.args.get('the_id')
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("movies-index.html", movies=all_movies, the_id=the_id)


@app.route("/edit/", methods=["GET", "POST"])
def rate_movie():
    the_id = request.args.get('the_id')
    person = Person.query.get(the_id)
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = f'"{form.review.data}" by {person.name}'
        db.session.commit()
        return redirect(url_for('home', the_id=the_id))
    return render_template("edit.html", movie=movie, form=form, the_id=the_id)


@app.route("/delete/")
def delete_movie():
    the_id = request.args.get('the_id')
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home", the_id=the_id))


@app.route("/add/", methods=["GET", "POST"])
def add_movie():
    the_id = request.args.get('the_id')
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": "67cbf495404908933af867e1de815348",
                "query": movie_title
            }
        )
        data = response.json()["results"]
        return render_template("select.html", options=data, the_id=the_id)

    return render_template("add.html", form=form, the_id=the_id)


@app.route("/find/")
def find_movie():
    the_id = request.args.get('the_id')
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(
            movie_api_url,
            params={
                "api_key": "67cbf495404908933af867e1de815348",
                "language": "en-US"
            }
        )
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id, the_id=the_id))


if __name__ == "__main__":
    app.run(debug=True)
