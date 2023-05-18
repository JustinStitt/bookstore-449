from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    description: str
    price: float
    stock: int


class BookUpdate(BaseModel):
    title: str | None
    author: str | None
    description: str | None
    price: float | None
    stock: int | None
