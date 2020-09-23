import unittest

from mynumber import MyNumber


class TestMyNumber(unittest.TestCase):

    def test_is_even_positive(self):
        """
        This method is used to test even or odd functionality
        """
        my_number = MyNumber()  # Arrange
        result = my_number.is_even(10)  # Action
        self.assertEqual(result, True)  # Assert

    def test_is_even_negative(self):
        """
        This will test the is_even method with odd value
        """
        my_number = MyNumber()
        result = my_number.is_even(11)
        self.assertEqual(result, False)

    @unittest.skip("Work In Progress")
    def test_is_even_negative_boundary(self):
        my_number = MyNumber()
        result = my_number.is_even('hello')

