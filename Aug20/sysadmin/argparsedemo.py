#!/usr/bin/env python3

import argparse


def parse_arguments():
    """
    This method will parse the arguments
    :return:
    """
    # Created an parser
    parser = argparse.ArgumentParser()
    # optional boolean argument
    parser.add_argument('-o', '--output', action='store_true', help="Show Output")
    # required argument
    parser.add_argument('-n', '--name', required=True, help="Enter your name")
    # specify type of input
    parser.add_argument('-a', '--age', type=int, required=True, help="Enter your age")
    # default value to the optional argument
    parser.add_argument('-g', '--gender', default='Not Specified', help='Enter your gender')
    args = parser.parse_args()

    if args.output:
        print(f"Since output is selected. Hi {args.name} and you will have a wonderful career")
        if args.age > 30:
            print(f"hurry up to learn the necessary stuff, you are growing older {args.age}")


if __name__ == "__main__":
    parse_arguments()
