#!/usr/bin/python3
'''Converts a CSV Data to JSON.'''


import csv
import json


def convert_csv_to_json(csv_file):
    '''Converts a CSV Data to JSON.'''

    try:
        with open(csv_file, mode='r', encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            data = [row for row in csv_reader]

        with open('data.json', mode='w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
