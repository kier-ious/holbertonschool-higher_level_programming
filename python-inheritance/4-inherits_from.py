#!/usr/bin/python3
"""Checking to see if it's a subclass of"""


def inherits_from(obj, a_class):
    """Using issubclass to determine if its a subclass"""
    return issubclass(type(obj), a_class)
