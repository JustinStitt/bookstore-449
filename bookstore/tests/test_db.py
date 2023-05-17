import unittest
from ..db import DB


class TestDB(unittest.TestCase):
    def test_singleton(self):
        """
        This function tests the singleton design pattern implementation in the DB class.

        Parameters:
        self (TestCase): The TestCase object that this function is a method of.

        Returns:
        None

        Raises:
        AssertionError: If the ids of db1 and db2 are not equal, indicating that the singleton pattern was not implemented correctly.
        """

        db1 = DB()
        db2 = DB()
        self.assertEqual(id(db1), id(db2))

    def test_connection(self):
        """
        Test the connection to MongoDB Atlas.

        This function tests the connection to MongoDB Atlas by attempting to ping the server. It uses the `client` object from the `DB` class to connect to the server. If the connection is successful, the function returns without any errors. If the connection fails, the function raises an exception with a detailed error message.

        Parameters:
        -----------
        self : object
            The instance of the class that this method is called on.

        Returns:
        --------
        None

        Raises:
        -------
        AssertionError
            If the connection to MongoDB Atlas fails.

        Example:
        --------
        >>> test = TestClass()
        >>> test.test_connection()
        """
        client = DB().client
        try:
            client.admin.command("ping")
        except Exception as e:
            raise AssertionError(
                f"Failed MongoDB Atlas connection with exception e: {e}"
            )
