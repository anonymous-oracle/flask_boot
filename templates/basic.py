from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>welcome!!</h1>'

@app.route('/<name>')
def name(name):
    letters = list(name)
    dicts = {'name':name.upper()}
    return render_template('basic.html', name=name.upper(), letters=letters, dicts=dicts)

if __name__=='__main__':
    app.run()