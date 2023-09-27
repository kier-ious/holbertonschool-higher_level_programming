#!/usr/bin/python3
"""Adding and saving items to a JSON file"""
import sys
import json


INPUT_JSON_FILE = "add_item.json"
OUTPUT_JSON_FILENAME = "add_list.json"

def save_to_json_file(my_obj, filename):
    """Save Python object to a JSON file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Load Python object from a JSON file"""
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError
        return []

my_list = load_from_json_file(INPUT_JSON_FILE)
"""Initializes an empty list or load exisitng list from JSON"""

if len(sys.argv) > 1:
    """Check if there's command line arguments and extend list"""
    my_list.extend(sys.argv[1:])
    """Extending list w/ comd line args"""

save_to_json_file(my_list, OUTPUT_JSON_FILENAME)
"""Save updated list to add_list.json"""
