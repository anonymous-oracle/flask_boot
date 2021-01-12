from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth



# storing items in a list
items = []


class Student(Resource):
    def get(self, name):
        return {'student': name}


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # to ensure that the item is not repeated
        if next(filter(lambda item: item['name'] == name, items), None):
            return {'message': 'item with name %s already exists' % (name)}, 400
        data = request.get_json()
        newItem = {'name': data['name'], 'price': data['price']}
        items.append(newItem)
        return newItem, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


# https://127.0.0.1:5000/student/<name>
api.add_resource(Student, '/student/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<name>')


if __name__ == '__main__':
    app.run(debug=True)
