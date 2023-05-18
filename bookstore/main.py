from bson import ObjectId
from bson.json_util import dumps
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from .book import Book, BookUpdate
from .db import DB
from .validation import validate_book_id

app = FastAPI()
db = DB().collection


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/books")
async def add_book(book: Book = Depends()):
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
@validate_book_id
async def get_book_by_id(book_id: str):
    obj_id = ObjectId(book_id)
    result = db.find_one({"_id": obj_id})
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Book with id = {book_id} NOT found!"
        )

    return JSONResponse(content=dumps(result))


@app.post("/books/{book_id}")
@validate_book_id
async def update_book_by_id(book_id: str, book: BookUpdate = Depends()):
    obj_id = ObjectId(book_id)
    changed_fields = {k: v for (k, v) in book.dict().items() if v is not None}
    result = db.update_one({"_id": obj_id}, {"$set": changed_fields})
    return {
        "message": f"updated {result.modified_count} book{'s' if result.modified_count != 1 else ''}"
    }


@app.delete("/books/{book_id}")
@validate_book_id
async def delete_book_by_id(book_id: str):
    obj_id = ObjectId(book_id)
    result = db.delete_one({"_id": obj_id})
    if result.deleted_count < 1:
        raise HTTPException(
            status_code=404, detail=f"Could not find book with id {book_id} to delete."
        )

    return {"message": f"deleted book with id {book_id}"}


@app.get("/search")
async def search_for_book(
    title: str | None = None,
    author: str | None = None,
    min_price: float = 0.0,
    max_price: float = 10e9,
):
    in_price_range = {"price": {"$gte": min_price, "$lte": max_price}}
    has_title = {"title": title}
    has_author = {"author": author}
    query = {"$or": [has_title, has_author], **in_price_range}

    results = db.find(query)
    return JSONResponse(content=dumps(results))


@app.get("/total")
async def get_total_books():
    return db.count_documents({})


@app.get("/popular_authors")
async def get_popular_authors():
    pipeline = [
        {"$group": {"_id": "$author", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5},
    ]

    results = list(db.aggregate(pipeline))

    return JSONResponse(content=dumps(results))


@app.get("/best_selling")
async def get_best_selling():
    results = db.find().sort("stock", -1).limit(5)

    return JSONResponse(content=dumps(results))
