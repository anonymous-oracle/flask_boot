import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__)) # to create the db in the same directory
# print(basedir)

app = Flask(__name__)

##################DATABASE CREATION WITH MIGRATION##################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# migration is used to enable on the go updates to the sqlite database;
# it helps to add new columns as and when it is needed using the flask
# terminal commands
Migrate(app, db)
###################################################################

class Puppy(db.Model):
# this is a table object
    # manual table name choice
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    # to demonstrate the migration, we add a breed column
    breed = db.Column(db.Text)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        # return "Puppy Name: {0}, Puppy Age: {1}".format(self.name, self.age)
        return f"{self.breed} Puppy, {self.name} is {self.age} year/s old"


#################MIGRATION SETUP TERMINAL COMMANDS####################
# export FLASK_APP=<path-to-flask-app-script>
# flask db init
# flask db migrate -m "<some-init-message>"
# flask db upgrade

# in the above example we added breed column, so now we just use the 'flask db migrate -m "<message>"'
# command to affect the changes

# flask db migrate -m "<update-message>"
# flask db upgrade