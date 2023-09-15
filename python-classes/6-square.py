#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """Square class with size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """init method w/ optional size"""
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate are of the Square"""
        return self.__size ** 2

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

    def my_print(self):
        """Printing the Square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


    @property
    def position(self):
        """Getter for size attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for size in method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = value

    def area(self):
        """Calculate are of the Square"""
        return self.__position ** 2


    def my_print(self):
        """Printing the Square with #"""
        if self.__position == 0:
            print()
        else:
            for _ in range(self.__position):
                print("#" * self.__position)
