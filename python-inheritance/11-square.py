#!/usr/bin/python3
"""subclass of BaseGeometry, Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creating a Square class"""

    def __init__(self, size):
        """Intitializing new Square class
        Args:
            size (Int): Size of Square class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return the Square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
