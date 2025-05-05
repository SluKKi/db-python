from app import app
from models import db, Author, Book

with app.app_context():
    db.create_all()

    author1 = Author(name='Лев Толстой')
    author2 = Author(name='Фёдор Достоевский')

    db.session.add(author1)
    db.session.add(author2)
    db.session.commit()

    book1 = Book(title='Война и мир', year=1869, author_id=author1.id)
    book2 = Book(title='Анна Каренина', year=1877, author_id=author1.id)
    book3 = Book(title='Преступление и наказание', year=1866, author_id=author2.id)

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()