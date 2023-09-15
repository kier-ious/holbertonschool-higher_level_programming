#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """Square class with size attribute"""

    def __init__(self, size=0):
        """init method w/ optional size"""
        self.__size = size

    def area(self):
        """Calculate are of the Square"""
        return self.__size ** 2

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
