from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    name = StringField("what is your name?")
    submit = SubmitField('submit')

@app.route('/', methods=['GET','POST'])
def index():
    name=False
    form = InfoForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = '' # if not set to null, then when the form reloads after clicking submit,
        # the previous name.data will be already entered in the text field
    return render_template('index.html', form=form,name=name)


if __name__=='__main__':
    app.run(debug=True)