#!/usr/bin/python3
'''Serializes and deserializes a Python object using pickle.'''


import pickle

class CustomObject:
    '''A simple class for demonstration purposes.'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''Display the object's attributes.'''
        print(f'Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}\n')
    
    def serialize(self, filename):
        '''Serialize the object to a file using pickle.'''
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize an object from a file using pickle.'''
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
        