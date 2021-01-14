from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/<name>')
# def indexGreet(name):
#     return render_template('index.html', name=name[0].upper()+name[1:].lower())

@app.route('/greet/<names>')
def indexGreetMany(names):
    # in the url, just pass the name list as a string of names separated by a ',' after adding a '?'
    # to a respective route point
    names = [name[0].upper()+name[1:].lower() for name in names.split(',')]
    return render_template('index.html', names=names, num_names=len(names))


if __name__ == '__main__':
    app.run(debug=True)
