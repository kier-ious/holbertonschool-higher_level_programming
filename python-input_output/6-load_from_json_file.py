#!/usr/bin/python3
"""POOF, obj from JSON file"""
import json


def load_from_json_file(filename):
    """Func from obj from JSON"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
