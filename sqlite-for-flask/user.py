from flask_restful import Resource, reqparse
import sqlite3 as sql

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


    # converts the following to a class method instead of an object/resource method
    @classmethod
    def find_by_username(cls, username):
        connection = sql.connect('data.db')
        cursor = connection.cursor()

        query = 'select * from users where username=?'
        result = cursor.execute(query, (username,))
        row=result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sql.connect('data.db')
        cursor = connection.cursor()

        query = 'select * from users where id=?'
        result = cursor.execute(query, (_id,))
        row=result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field cannot be blank.")
    
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field cannot be blank.")
    
    def post(self):
        data = UserRegister.parser.parse_args()
        # if User.find_by_username(data['username'])

        connection=sql.connect('data.db')
        cursor = connection.cursor()

        query = 'insert into users values (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {'message': 'User created successfully'}, 201