from .db import DB
from .book import Book
from faker import Faker
from random import choice, uniform, seed, randint

"""
Populate the database with fake books
"""

N = 400
SEED = 1339

db = DB().collection
fake = Faker(seed=SEED)
seed(SEED)

authors = [fake.name() for _ in range(2 * 10)]


def main():
    current = 0
    for _ in range(N):
        title = fake.text(max_nb_chars=36)
        author = choice(authors)
        description = fake.sentence()
        price = round(uniform(0.01, 200.99), ndigits=2)
        stock = randint(0, 10_000)
        book = Book(
            title=title,
            author=author,
            description=description,
            price=price,
            stock=stock,
        )
        db.insert_one(book.dict())
        if current % 50 == 0:
            print(f"{current/N*100:.2f}% done", flush=True)
        current += 1
    print(f"Done inserting {N} book(s)")


if __name__ == "__main__":
    main()
