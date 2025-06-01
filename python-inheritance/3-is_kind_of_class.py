#!/usr/bin/python3
"""Function to check if an object is an instance of a class or a subclass."""

def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or a subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
