#!/usr/bin/env python3

import argparse


def parse_arguments():
    """
    This method will parse the arguments
    :return:
    """
    # Created an parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--value', type=int, action='append', dest='numbers', help='Enter numbers')
    parser.add_argument('-o', '--operation', required=True, choices=['add', 'mul'])
    # # optional boolean argument
    # parser.add_argument('-o', '--output', action='store_true', help="Show Output")
    # # required argument
    # parser.add_argument('-n', '--name', required=True, help="Enter your name")
    # # specify type of input
    # parser.add_argument('-a', '--age', type=int, required=True, help="Enter your age")
    # # default value to the optional argument
    # parser.add_argument('-g', '--gender', default='Not Specified', help='Enter your gender')
    args = parser.parse_args()
    result = 0
    for number in args.numbers:
        if args.operation == 'add':
            result = result + number
        elif args.operation == 'mul':
            if result == 0:
                result = 1
            result = result * number

    print(result)


if __name__ == "__main__":
    parse_arguments()
