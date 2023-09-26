#!/usr/bin/python3
"""subclass of BaseGeometry, Square"""
Rectangle = __import__('9-base_geometry').Rectangle


class Square(Rectangle):
    """Creating a Square class"""

    def __init__(self, size):
        """Intitializing new Square class
        Args:
            size (Int): Size of Square class
        """
        self.integer_validator("size", size)
        def area(self).__init__(size, size)
        self.__size = size
