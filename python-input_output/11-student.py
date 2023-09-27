#!/usr/bin/python3
"""Defining a Student class"""


class Student:
    """Class for Student instances"""

    def __init__(self, first_name, last_name, age):
        """Initializing methods attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that returs dict info"""
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) != str:
                    return obj

    def reload_from_json(self, json):
        """Replaces all attrs of Student instance"""
        for attr in json:
            self.__dict__[attr] = json[attr]
