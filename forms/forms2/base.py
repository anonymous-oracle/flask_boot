from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, 
DateTimeField, RadioField, SelectField,
 TextField, TextAreaField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    name = StringField("what is your name?", validators=[DataRequired()])
    state = BooleanField('are you happy in life?')
    mood = RadioField('please choose your mood:', choices=[('mood1','happy'),['mood2','excited']])
    food_choice = SelectField(u'pick your favorite food:', choices=[('food1','healthy'), ('food2', 'fast food')])
    feedback = TextAreaField()
    submit = SubmitField('submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        # the session object is basically a lookup dictionary 
        # which temprarily stores the data entered by the user
        # over and across the session
        session['name']=form.name.data
        session['state']=form.state.data
        session['mood']=form.mood.data
        session['food_choice']=form.food_choice.data
        session['feedback']=form.feedback.data
        # this is a python version of the url_for() function; once the submit button is clicked,
        # the redirect function redirects to the thankyou page
        return redirect(url_for('thankyou'))

    # index.html is rendered upon the first time visit to the page
    # once the form submission is validated, then the page redirects to thankyou page
    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__=='__main__':
    app.run(debug=True)