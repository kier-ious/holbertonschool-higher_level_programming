#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#Static Method Dict to JSON string---------------------------------------------
    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string repr"""
        if list_dictionaries is None:
            return '[]'

        return json.dumps(list_dictionaries)
