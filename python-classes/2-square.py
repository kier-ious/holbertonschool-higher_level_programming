#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """Square class with size attribute"""

    def __init__(self, size=0):
        """init method w/ optional size"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = size
