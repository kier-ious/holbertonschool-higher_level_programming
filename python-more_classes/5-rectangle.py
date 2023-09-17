#!/usr/bin/python3
"""Rectangle class with width and height atrributes"""


class Rectangle:
    """Rectangle class with width and height atrributes"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

    def area(self):
        """Calculate are of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        """Printing the Rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Return str repr for recreating rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deleting instance"""
        print("Bye rectangle...")
