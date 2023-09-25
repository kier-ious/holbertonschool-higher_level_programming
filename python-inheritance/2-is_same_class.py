#!/usr/bin/python3
"""Checking if the objest is an instance of the class"""


def is_same_class(obj, a_class):
    """Using type to check if obj is in same class"""
    if type(obj) == a_class:
        return True
    else:
        return False
