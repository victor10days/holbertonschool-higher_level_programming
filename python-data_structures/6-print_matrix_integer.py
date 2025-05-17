#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, num in enumerate(row):
            end_char = " " if idx < len(row) - 1 else ""
            print("{:d}".format(num), end=end_char)
        print()
