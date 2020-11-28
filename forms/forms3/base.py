from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, 
DateTimeField, RadioField, SelectField,
 TextField, TextAreaField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    name = StringField('enter your name: ')
    submit = SubmitField('click me')

@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        # can have multiple flash messages which send an iterator to the page
        session['name'] = form.name.data
        flash('your name is: {}'.format(session['name']))
        return redirect(url_for('index'))
    # index.html is rendered upon the first time visit to the page
    # once the form submission is validated, then the page redirects to thankyou page
    return render_template('index.html',form=form)


if __name__=='__main__':
    app.run(debug=True)