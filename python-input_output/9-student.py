#!/usr/bin/python3
"""Creating a Student class"""


class Student:
    """Class for Student instances"""

    def __init__(self, first_name, last_name, age):
        """Initializing methods attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age =age

    def to_json(self):
        """Method that returs dict info"""
        return self.__dict__.copy()
