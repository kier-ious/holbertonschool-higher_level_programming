#!/usr/bin/python3
"""Module that returns the dictionary info w/ simple data
structure"""


def class_to_json(obj):
    """Convert object into a JSON dict"""
    result = {}

    if hasattr(obj, "__dict__"):
        """Check if the object has a dict attribute"""
        result = obj.__dict__.copy()
        
    return result
