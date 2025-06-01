#!/usr/bin/python3
"""Module that defines the Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square from the Rectangle class."""
    
    def __init__(self, size):
        """Initializes a Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the area of the square."""
        return super().area()
