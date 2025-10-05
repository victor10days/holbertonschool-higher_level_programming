#!/usr/bin/python3
def serialize_and_save_to_file(data, filename):
    """Serializes data to JSON and saves it to a file."""

    
    import json

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    return None

def load_from_json_file(filename):
    """Loads data from a JSON file and deserializes it."""


    import json

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
    return None
