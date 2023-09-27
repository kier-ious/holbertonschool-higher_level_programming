#!/usr/bin/python3
"""Returning JSON format of an object"""
import json


def to_json_string(my_obj):
    """Method that returns JSON"""
    return json.dumps(my_obj)
