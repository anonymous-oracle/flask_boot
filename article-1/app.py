from flask import Flask
from flask import request, jsonify
import sqlite3 as sql

app = Flask(__name__)
app.config['DEBUG'] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# by default the get method is used even without mentioning
@app.route('/', methods=['GET'])
def home():
    return "Home page"

# a route to return all of the available entries in our catalog


@app.route('/books')
def api_all():
    query = 'select * from books'
    conn = sql.connect('books.db')
    cur = conn.cursor()
    all_books = cur.execute(query)

    return jsonify(all_books)


# @app.route('/book')
# def getBook():
#     # check if an id was provided as a part of the URL
#     # /books?id=0
#     if request.args.get('id'):
#         id_ = int(request.args['id'])
#     else:
#         return "Error: No id provided, please provide a valid id."

#     results = []

#     for book in books:
#         if book['id'] == id_:
#             results.append(book)
#     return jsonify({'book': results})




@app.route('/book')
def api_filter():
    queryParams = request.args
    id_ = queryParams.get('id')
    published = queryParams.get('published')
    author = queryParams.get('author')

    query = 'select * from books where'
    toFilter = []
    if id_:
        query += ' id=? and'
        toFilter.append(id_)
    if published:
        query += ' published=? and'
        toFilter.append(published)
    if author:
        query += ' author=? and'
        toFilter.append(author)
    if not (id_ or published or author):
        return pageNotFound
    query = query[:-4]+';'

    conn = sql.connect('books.db')
    cur = conn.cursor()
    results = cur.execute(query, toFilter)
    return jsonify(results)


if __name__ == '__main__':
    app.run()
