#!/usr/bin/python3
""" Function that returns a list of lists of integers representing the Pascal's triangle of a given size."""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle of a given size.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
