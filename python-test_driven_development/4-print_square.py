#!/usr/bin/python3
"""Printing a square"""


def print_square(size):
    """Checking to see if it's an int"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        """CHecking to see if it's >= to 0"""
        raise ValueError("size must be >= 0")

    for o in range(size):
        for k in range(size):
            print("#", end="")

        print()
 