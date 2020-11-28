import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__)) # to create the db in the same directory
# print(basedir)

app = Flask(__name__)

##################DATABASE CREATION##################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

####################################################

class Puppy(db.Model):

    # manual table name choice
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # return "Puppy Name: {0}, Puppy Age: {1}".format(self.name, self.age)
        return f"Puppy, {self.name} is {self.age} year/s old"