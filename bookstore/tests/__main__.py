import unittest
from .test_book import TestBook
from .test_db import TestDB

TESTS = [TestBook, TestDB]

if __name__ == "__main__":
    print(f"Testing: ")
    for test in TESTS:
        print(f"> {test}")
    unittest.main()
