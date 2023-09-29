#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defining a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# Width -----------------------------------------------------------------------
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

# Height ----------------------------------------------------------------------
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

# X ---------------------------------------------------------------------------
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

# Y ---------------------------------------------------------------------------
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

# Area ------------------------------------------------------------------------
    def area(self):
        """Calculate are of the Rectangle"""
        return self.__width * self.__height

# Display ---------------------------------------------------------------------
    def display(self):
        """Print Rectangle using the '#' character"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")

# __str__ ---------------------------------------------------------------------
    def __str__(self):
        """Printing the Rectangle with #"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.__id, self.__y, self.__width, self.__height)

# Update ----------------------------------------------------------------------
    def update(self, *args, **kwargs):
        ar_list = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, ar_list[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

# Dictionary ------------------------------------------------------------------
