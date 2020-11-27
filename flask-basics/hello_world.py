from flask import Flask

app = Flask(__name__)

# the below decorator routes the return value of the index() function to host it on the webpage
# this return value can be entire html templates or a simple element as shown
# '/' indicates that it defaults to the localhost of the system
@app.route('/') # 127.0.0.1:5000
def index():
    return '<h1>hello world</h1>'

# following function demonstrates an additional page
@app.route('/info') # 127.0.0.1:5000/info
def info():
    return '<h1>web dev is cool</h1>'

# dynamic routing
@app.route('/user/<name>')
def user(name):
    return '<h1>the name is: {}</h1>'.format(name.upper())

# # below function is meant to give an error so that we can debug; it will produce an 'internal server error'
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>100th letter: {}</h1>'.format(name[100]) 


if __name__=='__main__':
    app.run()

    # # setting/using debug mode
    # app.run(debug=True)
