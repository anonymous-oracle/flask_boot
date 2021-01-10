# simulate a store app
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        'name': 'example-store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]

# SERVER PERSPECTIVE
# POST: receive data from client
# GET: send data to the client based on request


@app.route('/')
def home():
    return render_template('index.html')

# TASKS:

# POST /store data: {name}


@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>/item


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found :('})

# GET /store; send store lists


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            newItem = {
                'name': data['name'],
                'price': data['price']
            }
            store['items'].append(newItem)
            return jsonify(newItem)
    return jsonify({'message': 'store not found :('})

# GET /store/<string:name>/item


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found :('})


if __name__ == '__main__':
    app.run(debug=True)
