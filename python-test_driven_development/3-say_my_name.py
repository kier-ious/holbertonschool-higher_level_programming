#!/usr/bin/python3
"""Function that prints first and last name"""


def say_my_name(first_name, last_name=""):
    """Checking to see if first name is a string"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    """Checking to see if b is an integer or a float"""
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
