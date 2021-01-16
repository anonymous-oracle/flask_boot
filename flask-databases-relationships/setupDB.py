from app import db, Book

# CREATES ALL THE TABLES --> Db Table

db.create_all()

book1 = Book('The book', 1989)
book2 = Book('The book 2', 1991)

print(book1.id_)  # prints None
print(book2.id_)  # prints None

# add all at once
db.session.add_all([book1, book2])
db.session.commit()

# # OR
# db.session.add(book1)
# db.session.add(book2)
# db.session.commit()

print(book1.id_)  # prints None
print(book2.id_)  # prints None