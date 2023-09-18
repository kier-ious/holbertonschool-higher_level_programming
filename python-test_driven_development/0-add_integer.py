#!/usr/bin/python3
"""Adding two intgers together"""


def add_integer(a, b=98):
    """Checking to see if a is an integer or a float"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    """Checking to see if b is an integer or a float"""
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
