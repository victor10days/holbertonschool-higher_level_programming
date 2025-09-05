#!/usr/bin/python3

from add_0 import add
import sys

if __name__ == "__main__":
    result = 0
    for i in range(1, len(sys.argv)):
        try:
            num = int(sys.argv[i])
            result = add(result, num)
        except ValueError:
            print("Error: {} is not an integer".format(sys.argv[i]))
            sys.exit(1)
    print("{}".format(result))
