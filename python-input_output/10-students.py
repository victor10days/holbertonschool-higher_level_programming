#!/usr/bin/python3
'''Student class that defines a student by: (based on 9-student.py)'''


class Student:
    '''Student class that defines a student by: (based on 9-student.py)'''

    def __init__(self, first_name, last_name, age):
        '''Initializes a Student instance.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student instance.'''
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list) or not all(isinstance(i, str) for i in attrs):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance.'''
        for key, value in json.items():
            setattr(self, key, value)
        return self

if __name__ == '__main__':
    student = Student("John", "Doe", 20)
    print(student.to_json())  # {'first_name': 'John', 'last_name': 'Doe', 'age': 20}
    print(student.to_json(['first_name', 'age']))  # {'first_name': 'John', 'age': 20}
    print(student.to_json(['middle_name']))  # {'first_name': 'John', 'last_name': 'Doe', 'age': 20}
    print(student.to_json('first_name'))  # {'first_name': 'John', 'last_name': 'Doe', 'age': 20}
    student.reload_from_json({'first_name': 'Jane', 'age': 22})
    print(student.to_json())  # {'first_name': 'Jane', 'last_name': 'Doe', 'age': 22}
