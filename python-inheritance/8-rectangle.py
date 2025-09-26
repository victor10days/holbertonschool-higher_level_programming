#!/usr/bin/python3

"""BaseGeometry class."""


class BaseGeometry:
    """Geometry class that defines area."""

    def area(self):
        """Exception is raised for string to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

            class Rectangle(BaseGeometry):
                """Class rectangle that inherits from BaseGeometry."""
                def __init__(self, width, height):
                    self.integer_validator("width", width)
                    self.integer_validator("height", height)
                    self.width = width
                    self.height = height
