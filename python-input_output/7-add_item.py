#!/usr/bin/python3
'''Adds all arguments to a Python list and saves them to a file in JSON format.'''


from sys import argv
import os.path
import importlib

load_from_json_file = importlib.import_module('6-load_from_json_file').load_from_json_file
save_to_json_file = importlib.import_module('5-save_to_json_file').save_to_json_file


def add_item(filename, items):
    '''Adds all arguments to a Python list and saves them to a file in JSON format.'''
    if os.path.exists(filename):
        current_items = load_from_json_file(filename)
    else:
        current_items = []
    current_items.extend(items)
    save_to_json_file(current_items, filename)  
    return current_items
