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
        self.client = MongoClient(DB_URL)
