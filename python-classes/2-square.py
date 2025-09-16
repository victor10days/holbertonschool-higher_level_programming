#!/usr/bin/python3
#!/usr/bin/python3
"""This module defines a Square class with a size attribute."""


class Square:
    """A class that defines a square."""
    pass

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
