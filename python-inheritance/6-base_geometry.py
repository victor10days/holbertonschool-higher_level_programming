#!/usr/bin/python3

"""BaseGeometry class."""


class BaseGeometry:
    """Geometry class that defines area."""

    def area(self):
        if self.__class__.__name__ == BaseGeometry:
            raise Exception("area() is not implemented")
