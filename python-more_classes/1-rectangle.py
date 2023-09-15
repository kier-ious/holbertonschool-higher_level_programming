#!/usr/bin/python3
"""An empty class rectangle that defines it"""


class Rectangle:
    """Square class with size attribute"""

    def __init__(self, height=0, width=(0, 0)):
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, tuple) or len(width) != 2\
                or not all(isinstance(i, int) and i >= 0 for i in width):
            raise TypeError("height must be an integer")

        self.__size = height
        self.__width = width

    @property
    def height(self):
        """Getter for size attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for size in method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Getter for size attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for size in method"""
        if not isinstance(value, tuple) or len(value) != 2\
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    def area(self):
        """Calculate are of the Square"""
        return self.__height ** 2

    def my_print(self):
        """Printing coordinates of the Square with #"""
        if self.__height == 0:
            print()
        else:
            for _ in range(self.__width[1]):
                print()
            for _ in range(self.__height):
                print(" " * self.__width[0] + "#" * self.__height)
