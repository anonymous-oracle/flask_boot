from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     DateTimeField, RadioField, SelectField,
                     TextField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'


class SimpleForm(FlaskForm):
        submit = SubmitField('Click to submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    # the first time when the page is visited, the form is displayed; and when the validate on submit is clicked, the data will be recorded
    if form.validate_on_submit():
        flash('you clicked!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
