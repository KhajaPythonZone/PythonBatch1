#!/usr/bin/env python3

import getopt
import sys


def parse_args():
    """
    This method will parse arguments
    """
    opts, args = getopt.getopt(sys.argv[1:], "am")
    print(opts)
    print(args)


if __name__ == "__main__":
    parse_args()
