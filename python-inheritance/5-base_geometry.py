#!/usr/bin/python3
"""Class BaseGeometry that defines a base geometry class."""

class BaseGeometry:
    """A base class for geometry-related classes."""
    
    def area(self):
        """Calculates the area of the geometry.
        
        Raises:
            Exception: If the area method is not implemented.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer.
        
        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
