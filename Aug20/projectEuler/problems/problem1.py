from utilities import numeric


# This module does have all the necessary references to solve the
# problem from https://projecteuler.net/problem=1

class Problem1:
    """
    This class is implementation of Project Euler Problem1
    """

    def __init__(self, multiple_1=3, multiple_2=5, maximum=1000):
        """
        Initialize the Problem1 class with multiple_1,multiple_2
        till maximum value
        :param multiple_1:
        :param multiple_2:
        :param maximum:
        """
        self._multiple_1 = multiple_1
        self._multiple_2 = multiple_2
        self._maximum = maximum

    def compute(self):
        """
        This method will compute and print the results
        """
        result = 0
        for index in range(1000):
            if numeric.is_divisible_by(index, self._multiple_1) or numeric.is_divisible_by(index, self._multiple_2):
                result = result + index
        print(f"Result of project euler problem 1 is {result}")
