from bson import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from .book import Book, BookUpdate
from .db import DB

app = FastAPI()
db = DB().collection


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/books")
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


@app.get("/books")
async def get_books():
    documents = db.find()
    return JSONResponse(content=dumps(documents))


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: str):
    try:
        obj_id = ObjectId(book_id)
    except InvalidId as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid ID provided... {e} e.g. '6464542c184525d3db84dcce'",
        )

    result = db.find_one({"_id": obj_id})
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Book with id = {book_id} NOT found!"
        )

    return JSONResponse(content=dumps(result))


@app.post("/books/{book_id}")
async def update_book_by_id(book_id: str, book: BookUpdate = Depends()):
    try:
        obj_id = ObjectId(book_id)
    except InvalidId as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid ID provided... {e} e.g. '6464542c184525d3db84dcce'",
        )

    changed_fields = {k: v for (k, v) in book.dict().items() if v is not None}
    result = db.update_one({"_id": obj_id}, {"$set": changed_fields})
    return {
        "message": f"updated {result.modified_count} book{'s' if result.modified_count != 1 else ''}"
    }
