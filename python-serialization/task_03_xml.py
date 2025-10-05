#!/usr/bin/python3
'''Serialiazing and deserializing with XML.'''


import xml.etree.ElementTree as ET
import json

def serialize_to_xml(dictionary, filename):
    '''Serializes a dictionary to an XML file.'''
    root = ET.Element('root')
    for key, value in dictionary.items():
        item = ET.SubElement(root, 'item', key=key)
        item.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    '''Deserializes an XML file to a dictionary.'''
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for item in root.findall('item'):
        key = item.get('key')
        value = item.text
        dictionary[key] = value
    return dictionary
