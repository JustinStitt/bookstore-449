import os

from pymongo import MongoClient


DB_USERNAME = os.getenv("MONGO_USER")
DB_PASS = os.getenv("MONGO_PASS")
DB_URL = f"mongodb+srv://{DB_USERNAME}:{DB_PASS}@test-cluster.tak0x4e.mongodb.net/?retryWrites=true&w=majority"


class DB:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DB, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self.client = MongoClient(DB_URL).cpsc449.bookstore


if __name__ == "__main__":
    from .book import Book

    # db = DB().client.cpsc449.bookstore

    book = Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="A story of the decadent life of wealthy Americans during the Roaring Twenties",
        price=10.99,
        stock=100,
    )
    # result = db.insert_one(book.dict()) # raises DuplicateKeyErorr if already exists (title + author combo)
    # print(result.inserted_id)

    # author = "F. Scott Fitzgerald"
    # print(f"Finding all books by {author}")
    # for _book in db.find({"author": author}):
    #     print(_book)
