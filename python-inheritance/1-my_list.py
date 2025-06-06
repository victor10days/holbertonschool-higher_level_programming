#!/usr/bin/python3
"""Module that defines a subclass of list with additional functionality."""

class MyList(list):
    """A subclass of list that includes a method to print the list in sorted order."""
    
    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
