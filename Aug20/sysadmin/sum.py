#!/usr/bin/env python3

import sys


def sum_of_numbers():
    """
    This method will print the sum of arguments passed from command line
    :return: sum of numbers from cmdline
    """
    # naive method
    # result = 0
    # for argument in sys.argv[1:]:
    #     result = result + int(argument)
    # return  result

    # list comprehension
    arguments = [int(argument) for argument in sys.argv[1:]]
    return sum(arguments)


def sum_of_squares():
    """
    This method will print the sum of arguments passed from command line
    :return: sum of squares numbers passed from cmdline
    """
    # list comprehension
    arguments = [int(argument) * int(argument) for argument in sys.argv[1:]]
    return sum(arguments)


if __name__ == "__main__":
    print(sum_of_numbers())
    print(sum_of_squares())
