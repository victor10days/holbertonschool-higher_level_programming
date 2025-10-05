#!/usr/bin/python3
'''Basic serialization and deserialization of JSON.'''


import json

def serialize_and_save_to_file(data, filename):
    """Serializes data to JSON and saves it to a file."""


    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads data from a JSON file and deserializes it."""

    
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
