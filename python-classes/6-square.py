#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """Square class with size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2\
                or not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size in method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for size attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for size in method"""
        if not isinstance(value, tuple) or len(value) != 2\
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate are of the Square"""
        return self.__size ** 2

    def my_print(self):
        """Printing coordinates of the Square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
