#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not isinstance(a_dictionary, dict):
        a_dictionary = {}

    if key is None:
        a_dictionary[key] = value
    return a_dictionary
