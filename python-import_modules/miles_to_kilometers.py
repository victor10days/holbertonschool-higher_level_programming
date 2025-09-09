#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: {} <miles>".format(sys.argv[0]))
    sys.exit(1)

miles = float(sys.argv[1])
kilometers = miles * 1.60934
print("{:.2f} miles is equal to {:.2f} kilometers".format(miles, kilometers))

