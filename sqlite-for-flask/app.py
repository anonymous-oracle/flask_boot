from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from werkzeug.exceptions import TooManyRequests

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


# storing items in a list
items = []


class Student(Resource):
    def get(self, name):
        return {'student': name}


class Item(Resource):
    # the parser belongs to the class and not just one specific Item object/resource
    # determines what fields of the payload are used to update the item
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help='This field cannot be left blank')

    @jwt_required()  # can put this decorator on any of the methods below and they would require authorization
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # to ensure that the item is not repeated
        if next(filter(lambda item: item['name'] == name, items), None):
            return {'message': 'item with name %s already exists' % (name)}, 400

        data = request.get_json()
        newItem = {'name': name, 'price': data['price']}
        items.append(newItem)
        return newItem, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        # the .parse_args() will allow only the added arguments and remove the others in the payload
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item == None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


# https://127.0.0.1:5000/student/<name>
# api.add_resource(Student, '/student/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<name>')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(debug=True)
