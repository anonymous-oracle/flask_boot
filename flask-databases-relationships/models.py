import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Book(db.Model):

    # manual tablename choice; flask automatically assigns a default name
    __tablename__ = 'books'
    # global db
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # one to many relationship: a book can have multiple authors
    # backref adds a reference to the Author class to specify that it has a relationship with the Book model
    # lazy is used to specify options on how to load the rows; dynamic just returns the query to view the related items
    authors = db.relationship('Author', backref='book', lazy='dynamic')
    # one to one relationship: one book can be borrowed by one member at a time
    member = db.relationship('Member', backref='book', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.member:
            return f"Book: {self.name}\t Status: Borrowed by {self.member.name}"
        return f"Book: {self.name}\t Status: Available"

    def list_authors(self):
        return self.authors


class Author(db.Model):
    __tablename__ = 'authors'
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = (db.Integer, db.ForeignKey('books.id'))

    def __init__(self, name, book_id):
        self.name = name
        self.book_id = book_id


class Member(db.Model):
    __tablename__ = 'members'

    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __init__(self, name, book_id):
        self.name = name
        self.book_id = book_id
