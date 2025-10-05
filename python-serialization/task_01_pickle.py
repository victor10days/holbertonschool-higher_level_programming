#!/usr/bin/python3
'''Serializes and deserializes a Python object using pickle.'''


import pickle

class CustomObject:
    '''A simple class for demonstration purposes.'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def diplay(self):
        '''Display the object's attributes.'''
        print(f'Name: {self.name}, Age: {self.age}, Is Student: {self.is_student}')
    
    def serialize(self, filename):
        '''Serialize the object to a file using pickle.'''
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize an object from a file using pickle.'''
        with open(filename, 'rb') as file:
            return pickle.load(file)
