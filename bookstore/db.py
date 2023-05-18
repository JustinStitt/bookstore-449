import os

from pymongo import MongoClient


DB_USERNAME = os.getenv("MONGO_USER")
DB_PASS = os.getenv("MONGO_PASS")
DB_URL = f"mongodb+srv://{DB_USERNAME}:{DB_PASS}@test-cluster.tak0x4e.mongodb.net/?retryWrites=true&w=majority"


class DB:
    """
    Singleton design pattern for Database instance management
    (only allow a single DB to be constructed)
    """

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DB, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self.client = MongoClient(DB_URL)
        self.collection = self.client.cpsc449.bookstore


if __name__ == "__main__":
    """
    random stuff for testing... not important
    """
    # from .book import Book

    db = DB().collection
    # db.create_index([("$**", "text")])
    # result = db.find_one({"_id": ObjectId("6464542c184525d3db84dcce")})
    # # result = db.find_one({"title": "The Great Gatsby"})
    # print(result)

    # book = Book(
    #     title="The Great Gatsby",
    #     author="F. Scott Fitzgerald",
    #     description="A story of the decadent life of wealthy Americans during the Roaring Twenties",
    #     price=10.99,
    #     stock=100,
    # )
    # result = db.insert_one(book.dict()) # raises DuplicateKeyErorr if already exists (title + author combo)
    # print(result.inserted_id)

    # author = "F. Scott Fitzgerald"
    # print(f"Finding all books by {author}")
    # for _book in db.find({"author": author}):
    #     print(_book)
