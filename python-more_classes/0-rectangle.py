#!/usr/bin/python3
class Rectangle:
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
