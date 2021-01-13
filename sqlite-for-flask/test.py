import sqlite3 as sql

connection = sql.connect('data.db')

cursor = connection.cursor()

createTable = "create table users (id int, username text, password text)"

cursor.execute(createTable)

user = (1, 'xyz', 'asdf')
insertQuery = 'insert into users values (?,?,?)'
cursor.execute(insertQuery, user)

users = [(2, 'asd', 'asdf'), (3, 'vefv', 'scd')]

cursor.executemany(insertQuery, users)

selectQuery = 'select * from users'
for row in cursor.execute(selectQuery):
    print(row)


connection.commit()
connection.close()
