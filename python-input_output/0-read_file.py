#!/usr/bin/python3
"""Module to read a text file and print its content to stdout.
"""
def read_file(filename=""):
    """Reads a text file and prints its content to stdout."""

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')  # Use end='' to avoid adding an extra newline
