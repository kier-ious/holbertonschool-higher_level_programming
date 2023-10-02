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
        class_name = cls.__name__
        if class_name == "Rectangle":
            dummy = globals()["Rectangle"](1,0)
        elif class_name == "Square":
            dummy = globals()["Square"](1)

        dummy.update(**dictionary)
        return dummy

    class Rectangle:
        def __init__(self, width, height):
            super().__init__()
            self.width = width
            self.height = height

        def to_dictionary(self):
            return {
                'id': self.id,
                'width': self.width,
                'height': self.height
            }

        def update(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

        def __str__(self):
            return f"Rectangle({self.width}, {self.height})"

    class Square(Rectangle):
        def __init__(self, size):
            super().__init__(size, size)

        def to_dictionary(self):
            return {
                'id': self.id,
                'size': self.width
            }
