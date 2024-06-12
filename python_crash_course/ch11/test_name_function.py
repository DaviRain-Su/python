import unittest
from name_function import get_formatted_name

# This class must inherit from unittest.TestCase
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """test if the function works for names like 'Janis Joplin' """
        formatted_name = get_formatted_name('janis', 'joplin')
        # This method is used to check if the value returned by the function is equal to the expected value
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """test if the function works for names like 'Wolfgang Amadeus Mozart' """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        # assertEqual() method is used to check if the value returned by the function is equal to the expected value
        # assertNotEqual() method is used to check if the value returned by the function is not equal to the expected value
        # assertTrue() method is used to check if the value returned by the function is True
        # assertFalse() method is used to check if the value returned by the function is False
        # assertIn() method is used to check if the value returned by the function is in the list of expected values
        # assertNotIn() method is used to check if the value returned by the function is not in the list of expected values
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
