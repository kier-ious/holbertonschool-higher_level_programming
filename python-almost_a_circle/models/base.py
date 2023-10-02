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

        if list_objs is not None:
            for obj in list_objs:
                json_data.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(json_data))

# Static Method ---------------------------------------------------------------
    @staticmethod
    def from_json_string(json_string):
        """static method for returning the JSON list repr"""
        if not json_string:
            return []

        return json.loads(json_string)

# Class Method w/ dummy Rectangle and Square classes---------------------------
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attr already set"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

# File to instances -----------------------------------------------------------
    def load_from_file(cls):
        """Loading from JSON file named after class

        Returns:
            List of instances or an empty list
            if the file doesn't exist
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d)for d in list_dicts]

        except FileNotFoundError:

            return []
