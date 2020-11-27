from flask import Flask

app = Flask(__name__)

# the below decorator routes the return value of the index() function to host it on the webpage
# this return value can be entire html templates or a simple element as shown
# '/' indicates that it defaults to the localhost of the system
@app.route('/') # 127.0.0.1:5000
def index():
    return '<h1>hello world</h1>'

@app.route('/puppy_latin/<name>')
def platin(name):
    if name[-1]!='y':
        return '<h3>the name is: {}y</h3>'.format(name)
    if name[-1]=='y':
        return '<h3>the name is: {}iful</h3>'.format(name)


if __name__=='__main__':
    app.run()

    # # setting/using debug mode
    # app.run(debug=True)
