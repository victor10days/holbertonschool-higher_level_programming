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
        self.size = size  # Use the setter to validate

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"Square(size={self.__size})"
    
    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
            print()
    
    def __del__(self):
        """Print a message when the square is deleted."""
        print("Bye square...")
        