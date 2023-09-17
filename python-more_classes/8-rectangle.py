#!/usr/bin/python3
"""Rectangle class with width and height atrributes"""


class Rectangle:
    """Rectangle class with width and height atrributes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        else:
            self.__height = value

    def area(self):
        """Calculate are of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Printing the Rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += str(Rectangle.print_symbol) * self.width + "\n"

        return rectangle_str.rstrip()

    def __repr__(self):
        """Return str repr for recreating rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deleting instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
