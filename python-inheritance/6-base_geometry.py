#!/usr/bin/python3
"""Empty class BaseGeometry that defines a base geometry class."""


class BaseGeometry:
    """A base class for geometry-related classes."""
    pass

def area(self):
    """Raises an Exception with the message 'area() is not implemented'."""
    raise Exception("area() is not implemented")
BaseGeometry.area = area
