#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base
from dataclasses import dataclass


class Rectangle(Base):
    """Defining a Rectangle class"""

    width: int
    height: int
    x: int = 0
    y: int = 0


    def area(self):
        """Calculate are of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle using the '#' character"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Printing the Rectangle with #"""
        return f"[Rectangle] ({self.id} {self.__x}/{self.__y} - \
        {self.__width}/{self.__height})"
