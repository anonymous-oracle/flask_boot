from os import name
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):

    name = StringField('name of puppy: ')
    submit = SubmitField('add')

class DelForm(FlaskForm):
    id = IntegerField('id of puppy to remove: ')
    submit = SubmitField('remove')


class Adopt(FlaskForm):
    name = StringField('name of the owner: ')
    pup_id = IntegerField('enter id of puppy: ')
    submit = SubmitField('adopt')
