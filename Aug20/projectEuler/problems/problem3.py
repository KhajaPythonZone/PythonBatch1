from utilities import  numeric

class Problem3:
    """
    This is implementation of Project Euler problem 3 @
    https://projecteuler.net/problem=3
    """
    def __init__(self, number=600851475143):
        """
        Initialize problem 3 with default number
        :param number:
        """
        self._number = number

    def compute(self):
        """
        This method will compute the result of Problem3
        """
        for index in range(self._number//2,1,-1):
            if numeric.is_divisible_by(self._number,index) and numeric.is_prime(index):
                print(f"largest prime factor of {self._number} is {index}")
                break

