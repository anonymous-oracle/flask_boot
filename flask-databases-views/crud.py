from models import db, Book, Author, Member

# creating two books
book1 = Book('book1')
book2 = Book('book2')

# adding books
db.session.add_all([book1, book2])
db.session.commit()

# check
print(Book.query.all())

book = Book.query.filter_by(name='book1').first()

# create member object
member = Member('member', book.id_)

# create authors for book
author1 = Author('author1', book.id_)
author2 = Author('author2', book.id_)

db.session.add_all([member, author1, author2])
db.session.commit()

# grab book1 again
book = Book.query.filter_by(name='book1').first()

print(book)
book.list_authors()