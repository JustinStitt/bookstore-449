from bson.json_util import dumps
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from .book import Book
from .db import DB

app = FastAPI()
db = DB().client


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/add_book")
async def add_book(title: str, author: str, description: str, price: float, stock: int):
    book = Book(
        title=title, author=author, description=description, price=price, stock=stock
    )
    try:
        result = db.insert_one(book.dict())
        if not result:
            raise HTTPException(status_code=500, detail="Failed to insert book.")
    except DuplicateKeyError:
        raise HTTPException(status_code=409, detail="Book already exists.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong... {e}")

    return {"message": "success"}


@app.get("/get_books")
async def get_books():
    documents = db.find()
    return JSONResponse(content=dumps(documents))
