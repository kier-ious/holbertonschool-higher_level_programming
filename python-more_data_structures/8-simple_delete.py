#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = {}
    a_dictionary.pop(key, new_dict)
