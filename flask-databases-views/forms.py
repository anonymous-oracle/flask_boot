from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class BorrowForm(FlaskForm):
    name = StringField('Name of Book:')
    nameOfMember = StringField('Name of member: ')
    submit = SubmitField('Borrow')


class ReturnForm(FlaskForm):
    id_ = IntegerField('ID number of book to return: ')
    submit = SubmitField('Return')


class AddForm(FlaskForm):
    name = StringField('Name of Book:')
    submit = SubmitField('Add')