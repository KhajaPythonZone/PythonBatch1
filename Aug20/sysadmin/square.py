#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    for number in sys.stdin:
        value = int(number.strip())
        print(value*value)
