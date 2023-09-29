#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base
from dataclasses import dataclass


class Rectangle(Base):
    """Defining a Rectangle class"""

    __width: int
    __height: int
    __x: int = 0
    __y: int = 0

    def __post_init__(self):
        """Custom error messages"""
        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        if not isinstance(self.width, int):
            raise TypeError("height must be an integer")
        if not isinstance(self.width, int):
            raise TypeError("x must be an integer")
        if not isinstance(self.width, int):
            raise TypeError("y must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

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
