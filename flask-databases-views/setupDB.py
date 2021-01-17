
from borrow import db, Book

# CREATES ALL THE TABLES --> Db Table

db.create_all()

# book1 = Book('book')
# book2 = Book('book')
# book3 = Book('book')
# book4 = Book('book')

# # print(book1.id_)  # prints None
# # print(book2.id_)  # prints None

# # # add all at once
# db.session.add_all([book1, book2, book3, book4])
# db.session.commit()

# # # # OR
# # # db.session.add(book1)
# # # db.session.add(book2)
# # # db.session.commit()

# # print(book1.id_)  # prints None
# # print(book2.id_)  # prints None

# books = [book for book in Book.query.filter_by(name='book')]
# print('========================================')
# print(books)