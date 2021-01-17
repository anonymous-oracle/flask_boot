from app import db, Book


separator="###############################{0}##############################"
# CREATE
mybook = Book('book1', 265)
db.session.add(mybook)
db.session.commit()

# READ
allbooks = Book.query.all()  # list of books
print(separator.format('READ'))
[print(f"{book.id_}. {book}") for book in allbooks]

# select by id
bookone = Book.query.get(1)
print(separator.format('ID SELECTION'))
print(bookone)

# filters
book_filter = Book.query.filter_by(name='book1')
print(separator.format('QUERY BY FILTERING'))
print(book_filter)

# UPDATE
bookUpdate = Book.query.get(1)
print(separator.format('BEFORE UPDATE'))
print(bookUpdate)
bookUpdate.publishedYear = 1265
db.session.add(bookUpdate)
print(separator.format('AFTER UPDATE'))
print(bookUpdate)
db.session.commit()

# DELETE
book  = Book.query.get(1)
db.session.delete(book)
db.session.commit()






db.drop_all()
