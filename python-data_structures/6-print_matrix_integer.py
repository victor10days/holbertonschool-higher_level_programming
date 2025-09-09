#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers.

    Args:
        matrix (list of lists): A list of lists of integers.
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
