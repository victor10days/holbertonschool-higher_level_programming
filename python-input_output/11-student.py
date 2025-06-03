#!/usr/bin/python3
"""Student class definition module."""
class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attributes to include in the dictionary.
                If None, all attributes are included.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from a JSON dictionary.

        Args:
            json (dict): A dictionary containing new values for the attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
    def __str__(self):
        """Returns a string representation of the Student instance."""
        return f"Student({self.first_name}, {self.last_name}, {self.age})"
    def __repr__(self):
        """Returns a string that can be used to recreate the Student instance."""
        return f"Student('{self.first_name}', '{self.last_name}', {self.age})"
