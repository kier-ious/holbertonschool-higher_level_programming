#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base
from dataclasses import dataclass


class Rectangle(Base):
    """Defining a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def id(self):
        return self.__id

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width in method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height in method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x in method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y in method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate are of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle using the '#' character"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Printing the Rectangle with #"""
        return f"[Rectangle] ({self.id} {self.__x}/{self.__y} - \
        {self.__width}/{self.__height})"
