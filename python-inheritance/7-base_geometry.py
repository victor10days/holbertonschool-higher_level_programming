#!/usr/bin/python3

"""BaseGeometry class."""


class BaseGeometry:
    """Geometry class that defines area."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        name = str()
        if != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
