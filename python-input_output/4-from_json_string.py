#!/usr/bin/python3
"""Returning JSON format of an object"""
import json


def from_json_string(my_str):
    """Method that returns object from JSON"""
    return json.loads(my_str)
