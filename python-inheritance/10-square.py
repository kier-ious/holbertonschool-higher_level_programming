#!/usr/bin/python3
"""subclass of BaseGeometry, Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Creating a Square class

    Args:
        BaseGeometry (base class): Parent class
    """
    def __init__(self, size):
        BaseGeometry.integer_validator(self, 'size', size)
        self.__size = size
        size >= 0

    def area(self):
        return self.__size

    def __str__(self):

        print("[Square] {}".format(self.__size))
