from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                     DateTimeField, RadioField, SelectField,
                     TextField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'


class InfoForm(FlaskForm):
    title = StringField("Enter the title of the book",
                        validators=[DataRequired()])
    isAMember = BooleanField('Are you a member?: ')
    genre = RadioField('Please choose the genre of your readings: ', choices=[
                       ('choice1', 'genre 1'), ('choice2', 'genre 2')])
    promotions = SelectField(u'Pick one of the following books which are promoted:', choices=[
                             ('choice1', 'abc'), ('choice2', 'xyz'), ('choice3', 'pqr')])
    feedback = TextAreaField()
    submit = SubmitField('Click to submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    # the first time when the page is visited, the form is displayed; and when the validate on submit is clicked, the data will be recorded
    if form.validate_on_submit():
        session['title'] = form.title.data
        if form.isAMember:
            session['isAMember'] = 'Yes'
        else:
            session['isAMember'] = 'No'
        session['genre'] = form.genre.data
        session['promotions'] = form.promotions.data
        session['feedback'] = form.feedback.data
    # we stored the form data in the session above and using the redirect method we pass the session to the page to be redirected to
        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
