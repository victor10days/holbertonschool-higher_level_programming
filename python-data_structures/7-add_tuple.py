#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples.

    Args:
        tuple_a (tuple): First tuple.
        tuple_b (tuple): Second tuple.

    Returns:
        tuple: A new tuple with the sum of the two tuples.
    """
    a = list(tuple_a) + [0, 0]
    b = list(tuple_b) + [0, 0]
    return (a[0] + b[0], a[1] + b[1])
