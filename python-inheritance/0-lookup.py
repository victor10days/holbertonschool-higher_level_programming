#!/usr/bin/python3
"""This module defines a function to return the list of available attributes and methods of an object."""

def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
