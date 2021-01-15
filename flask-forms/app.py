from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/thank_you')
def thank_you():
    firstName=request.args.get('first')
    lastName=request.args.get('last')
    return render_template('thank_you.html',first=firstName, last=lastName)

if __name__ == '__main__':
    app.run(debug=True)
