#!/usr/bin/python3
"""Module for the Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        self.size = size  # Use the setter to validate

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __sizeof__(self):
        return super().__sizeof__() + self.__size.__sizeof__()

    def __str__(self):
        return f"Square(size={self.__size})"

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
