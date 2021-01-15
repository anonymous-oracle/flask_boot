from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'



class InfoForm(FlaskForm):
    title = StringField("Enter the title of the book")
    submit = SubmitField('Click to Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    title = False
    form = InfoForm()
    # the first time when the page is visited, the form is displayed; and when the validate on submit is clicked, the data will be recorded
    if form.validate_on_submit():
        title = form.title.data
        # setting back to '' so that the value won't be displayed back on the form even after the session
        form.title.data = ''
    return render_template('index.html', form=form, title=title)


if __name__ == '__main__':
    app.run(debug=True)
