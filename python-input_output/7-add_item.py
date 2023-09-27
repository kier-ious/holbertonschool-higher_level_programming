#!/usr/bin/python3
"""Adding and saving items to a JSON file"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """Func from obj to txt in JSON"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Func from obj from JSON"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

my_list = []
"""Initialized empty list"""
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

my_list.extend(sys.argv[1:])
"""Extending list w/ comd line args"""

save_to_json_file(my_list, "add_list.json")
"""Save updated list to add_list.json"""
