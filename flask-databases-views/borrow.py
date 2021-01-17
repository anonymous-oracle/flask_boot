import os
from forms import BorrowForm, ReturnForm, AddForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

########################################
##########SQL DATABASE SECTION##########
########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

########################
#########MODELS#########
########################


class Book(db.Model):

    # manual tablename choice; flask automatically assigns a default name
    __tablename__ = 'books'
    # global db
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # one to many relationship: a book can have multiple authors; so the variable is called 'authors'
    # backref adds a reference to the Author class to specify that it has a relationship with the Book model
    # lazy is used to specify options on how to load the rows; dynamic just returns the query to view the related items
    # NOTE: when Book.author is accessed, a list will be returned
    authors = db.relationship('Author', backref='book', lazy='dynamic')
    # one to one relationship: one book can be borrowed by one member at a time
    # NOTE: when uselist=False is used, the relationship column will store the model object itself instead of storing it in a list like the above relationship
    # also lazy='dynamic' cannot be used since it is a single object and not a list
    member = db.relationship('Member', backref='book', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.member:
            return f"ID:[{self.id_}] -> Book: {self.name};\t Status: Borrowed by {self.member.name}"
        return f"ID:[{self.id_}] -> Book: {self.name};\t Status: Available"

    def list_authors(self):
        return self.authors


class Author(db.Model):
    __tablename__ = 'authors'
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id_'))

    def __init__(self, name, book_id):
        self.name = name
        self.book_id = book_id


class Member(db.Model):
    __tablename__ = 'members'

    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id_'))

    def __init__(self, name, book_id):
        self.name = name
        self.book_id = book_id

####################################
############VIEWS/ROUTES############
####################################


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/borrow', methods=['GET', 'POST'])
def borrow_book():
    availability = False
    form = BorrowForm()
    if form.validate_on_submit():
        name = form.data.get('name')
        nameOfMember = form.data.get('nameOfMember')
        books = [book for book in Book.query.filter_by(name=name)]
        for book in books:    
            if not book.member:
                availability = True
                book.member = Member(nameOfMember, book.id_)
                db.session.add(book)
                db.session.commit()
                return redirect(url_for('list_books'))
        if not availability:
                return redirect(url_for('list_books'))
    return render_template('borrow.html', form=form)


@app.route('/return', methods=['GET', 'POST'])
def return_book():
    form = ReturnForm()
    if form.validate_on_submit():
        bookId = form.data.get('id_')
        book = Book.query.filter_by(id_=bookId).first()
        book.member = None
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('list_books'))
    return render_template('return.html', form=form)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = AddForm()
    if form.validate_on_submit():
        bookName = form.data.get('name')
        book = Book(bookName)
        book.member = None
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('list_books'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_books():
    books = Book.query.all()
    return render_template('list.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
