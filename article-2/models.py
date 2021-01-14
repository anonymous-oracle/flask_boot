import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

projectDirectory = os.path.dirname(os.path.abspath(__file__))
databaseFile = 'sqlite:///{}'.format(
    os.path.join(projectDirectory, 'bookdatabase.db'))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseFile
db = SQLAlchemy(app)

