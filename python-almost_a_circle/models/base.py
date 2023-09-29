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
            Base.__num_objects += 1
            self.id = Base.__nb_objects
