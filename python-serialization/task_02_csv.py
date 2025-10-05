#!/usr/bin/python3
'''Converts a CSV Data to JSON.'''


import csv
import json

def convert_csv_to_json(csv_file):
    '''Converts a CSV Data to JSON.'''


    if json_file is None:
        json_file = csv_file.replace('.csv', '.json')

    try:
        with open(csv_file, mode='r', encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            data = [row for row in csv_reader]

        with open(json_file, mode='w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, indent=4)

        print(f"Data successfully converted from {csv_file} to {json_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
