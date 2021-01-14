from enum import unique
import os
from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

projectDirectory = os.path.dirname(os.path.abspath(__file__))
databaseFile = 'sqlite:///{}'.format(
    os.path.join(projectDirectory, 'bookdatabase.db'))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseFile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    # table name will be the classname
    title = db.Column(db.String(80), unique=True,
                      nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.form:
        book = Book(title=request.form.get('title'))
        db.session.add(book)
        db.session.commit()
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
