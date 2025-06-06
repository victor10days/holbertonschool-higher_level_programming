#!/usr/bin/python3
"""Function that creates an Object from a "JSON file"."""

import json
def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python data structure represented by the JSON file.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
