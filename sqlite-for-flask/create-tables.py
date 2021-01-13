import sqlite3 as sql
from sqlite3.dbapi2 import Cursor

connection = sql.connect('data.db')
cursor = connection.cursor()

createTable = 'create table if not exists users (id integer primary key, username text, password text)'
cursor.execute(createTable)

connection.commit()
connection.close()