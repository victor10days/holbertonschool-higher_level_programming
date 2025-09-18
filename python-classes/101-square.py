#!/usr/bin/python3
"""This module defines a Square class with size and position attributes."""

class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character with position offset.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square
        for _ in range(self.__size):
            # Horizontal offset (position[0])
            print(" " * self.__position[0], end="")
            # Print the square row
            print("#" * self.__size)
