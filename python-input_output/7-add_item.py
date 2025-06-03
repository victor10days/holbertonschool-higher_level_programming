#!/usr/bin/python3
"""Script that adds all arguments to a Python list, and then saves them to a file."""

import sys
import json

from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

def add_item():
    """Adds all command line arguments to a Python list and saves them to a file."""
    
    filename = "add_item.json"
    
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []
    
    items.extend(sys.argv[1:])
    
    save_to_json_file(items, filename)
if __name__ == "__main__":
    add_item()
