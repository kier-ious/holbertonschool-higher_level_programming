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

# Static Method Dict to JSON string--------------------------------------------
    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string repr"""
        if list_dictionaries is None:
            return '[]'

        return json.dumps(list_dictionaries)

# Class Method-----------------------------------------------------------------
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string repr of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        json_data = []

        if list_objs is None:
            return []

        for obj in list_objs:
            json_data.append(obj.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(json_data))
