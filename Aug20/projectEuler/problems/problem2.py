from utilities import numeric


class Problem2:
    """
    This class is implementation of Project Euler problem 2
    https://projecteuler.net/problem=2
    """

    def __init__(self, maximum=4000000):
        """
        This initializer takes the maximum
        :param maximum: default value is 4 million can be changed for debugging
        """
        self._maximum = maximum

    def compute(self):
        """
        This method will print the result of the project euler problem 2
        """
        first = 1
        second = 2
        result = 2
        while first + second < self._maximum:
            temp = first + second
            if numeric.is_divisible_by(temp, 2):
                result = result + temp
            first = second
            second = temp
        print(f"Result of the project euler problem 2 is {result}")
