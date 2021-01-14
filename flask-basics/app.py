from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/info')
def info():
    return "<h1>flask is light and strong</h1>"

@app.route('/<name>')
def other_page(name):
    return "<h1>page for {}</h1>".format(name)

if __name__=='__main__':
    app.run(debug=True)