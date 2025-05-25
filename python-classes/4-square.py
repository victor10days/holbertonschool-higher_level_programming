#!/usr/bin/python3
"""Module for the Square class."""


class Square:
    """A class that defines a square."""
    def __init__(self, size=0):
        """Initialize the square with a size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __sizeof__(self):
        
        """Return the size of the square object in bytes.

        Returns:
            int: The size of the square object in bytes.
        """
        return super().__sizeof__() + self.__size.__sizeof__()
