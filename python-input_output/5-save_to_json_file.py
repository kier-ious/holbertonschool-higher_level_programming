#!/usr/bin/python3
"""Save dat object to a file!"""
import json


def save_to_json_file(my_obj, filename):
    """Func from obj to txt in JSON"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
