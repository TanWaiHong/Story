from flask import Flask
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

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# Read All Records
# all_books = db.session.query(Book).all()
# and also you can
# all_books = Book.query.all()

# create a new book record
# new_book = Book(id=2, title="Ha1rry Potter", author='J.1 K. Rowling', rating=19.3)
# db.session.add(new_book)
# db.session.commit()

# update a book record by query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# update a book record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Potter and the Goblet of Fire"
# db.session.commit()

# delete a particular record by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
