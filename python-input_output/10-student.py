#!/usr/bin/python3
"""Creating a Student class"""


class Student:
    """Class for Student instances"""

    def __init__(self, first_name, last_name, age):
        """Initializing methods attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that returs dict info"""
        if attrs is None:
            return self.__dict__.copy()
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr
                    (self, attr)}
