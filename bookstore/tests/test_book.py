import unittest

from pydantic import ValidationError

from ..book import Book


class TestBook(unittest.TestCase):
    def test_create_book(self):
        book = Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            description="A story of the decadent life of wealthy Americans during the Roaring Twenties",
            price=10.99,
            stock=100,
        )
        self.assertEqual(book.title, "The Great Gatsby")
        self.assertEqual(book.author, "F. Scott Fitzgerald")
        self.assertEqual(
            book.description,
            "A story of the decadent life of wealthy Americans during the Roaring Twenties",
        )
        self.assertEqual(book.price, 10.99)
        self.assertEqual(book.stock, 100)

    def test_create_book_with_invalid_price(self):
        with self.assertRaises(ValidationError):
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", description="A story of the decadent life of wealthy Americans during the Roaring Twenties", price="ten dollars", stock=100)  # type: ignore

    def test_create_book_with_invalid_stock(self):
        with self.assertRaises(ValidationError):
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", description="A story of the decadent life of wealthy Americans during the Roaring Twenties", price=10.99, stock="44e")  # type: ignore

        with self.assertRaises(ValidationError):
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", description="A story of the decadent life of wealthy Americans during the Roaring Twenties", price=10.99, stock="one hundred")  # type: ignore

    def test_create_book_with_invalid_title(self):
        with self.assertRaises(ValidationError):
            Book(title=None, author="F. Scott Fitzgerald", description="A story of the decadent life of wealthy Americans during the Roaring Twenties", price=10.99, stock=100)  # type: ignore

    def test_create_book_with_invalid_author(self):
        with self.assertRaises(ValidationError):
            Book(title="The Great Gatsby", author=None, description="A story of the decadent life of wealthy Americans during the Roaring Twenties", price=10.99, stock=100)  # type: ignore

    def test_create_book_with_invalid_description(self):
        with self.assertRaises(ValidationError):
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", description=None, price=10.99, stock=100)  # type: ignore

    def test_create_book_with_missing_title(self):
        with self.assertRaises(ValidationError):
            Book(
                author="F. Scott Fitzgerald",
                description="Foobar",
                price=10.99,
                stock=100,
            )  # type: ignore

    def test_create_book_with_missing_author(self):
        with self.assertRaises(ValidationError):
            Book(
                title="The Great Gatsby",
                description="Foobar",
                price=10.99,
                stock=100,
            )  # type: ignore

    def test_create_book_with_missing_description(self):
        with self.assertRaises(ValidationError):
            Book(
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                price=10.99,
                stock=100,
            )  # type: ignore

    def test_create_book_with_missing_price(self):
        with self.assertRaises(ValidationError):
            Book(
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                description="Foobar",
                stock=100,
            )  # type: ignore

    def test_create_book_with_missing_stock(self):
        with self.assertRaises(ValidationError):
            Book(
                title="The Great Gatsby",
                author="F. Scott Fitzgerald",
                description="Foobar",
                price=10.99,
            )  # type: ignore

    def test_construct_from_dict(self):
        some_book = {
            "some": "nonsense",
        }
        with self.assertRaises(ValidationError):
            Book(**some_book)  # type: ignore
