from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template("index.html", ab=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']
        new_book = Book(title=name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
