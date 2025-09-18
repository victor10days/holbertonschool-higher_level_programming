#!/usr/bin/python3
"""This module defines a square class with size attributes."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

    def __eq__(self, other):
        """Check if two squares are equal based on their area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Check if two squares are not equal based on their area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Check if this square is less than another based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Check if this square is less than or equal to another."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Check if this square is greater than another based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Check if this square is greater than or equal to another."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
