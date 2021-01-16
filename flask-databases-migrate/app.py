import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
# no need to track every single modification to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

################################################################


class Book(db.Model):

    # manual tablename choice; flask automatically assigns a default name
    __tablename__ = 'books'
    # global db
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    publishedYear = db.Column(db.Integer)
    author = db.Column(db.Text)

    def __init__(self, name, publishedYear, author):
        self.name = name
        self.publishedYear = publishedYear
        self.author = author

    def __repr__(self):
        return f"Book: {self.name};\tPublished Year: {self.publishedYear}\n"
