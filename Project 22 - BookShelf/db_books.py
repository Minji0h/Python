import sqlite3

db = sqlite3.connect("books-collection.db")


def create_database():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
                   "title varchar(250) NOT NULL UNIQUE,"
                   "author varchar(250) NOT NULL,"
                   "rating FLOAT NOT NULL)")


def add_new_book(book_id: int, title: str, author: str, rating: str):
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO books VALUES("
                   f"{book_id}, '{title}','{author}','{rating}')")
    db.commit()