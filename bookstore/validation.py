from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from functools import wraps


def validate_book_id(endpoint):
    @wraps(endpoint)
    async def wrapper(*args, **kwargs):
        book_id: str = kwargs.get("book_id", "")
        try:
            ObjectId(book_id)
        except InvalidId as e:
            raise HTTPException(
                status_code=500,
                detail=f"Invalid ID provided... {e} e.g. '6464542c184525d3db84dcce'",
            )

        return await endpoint(*args, **kwargs)

    return wrapper
