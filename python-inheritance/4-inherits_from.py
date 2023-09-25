#!/usr/bin/python3
"""Checking to see if it's a subclass of"""


def inherits_from(obj, a_class):
    """Using isinstance to determine if a subclass"""
    if isinstance(obj, a_class) and not obj.__class__ == a_class:
        return True
    return False
