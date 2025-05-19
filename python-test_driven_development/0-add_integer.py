#!/usr/bin/python3
"""
0-add_integer
Defines a single function, ``add_integer(a, b=98)``, that returns
the integer sum of *a* and *b* after validating their types.
"""


def add_integer(a, b=98):
    """
    Add two numbers as integers.

    Args:
        a: first number (int or float)
        b: second number (int or float); defaults to 98

    Returns:
        int: the integer sum of a and b

    Raises:
        TypeError: if either argument is not an int or float
    """
    # Validate first argument
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Validate second argument
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast floats to ints, then return the sum
    return int(a) + int(b)