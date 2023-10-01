#!/usr/bin/python3
"""Square that inherites the Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining a Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new class"""
        super().__init__(size, size, x, y, id)

# __str__ ---------------------------------------------------------------------
    def __str__(self):
        """Printing the Square with #"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

# Update ----------------------------------------------------------------------
    def update(self, *args, **kwargs):
        """Update by adding validation"""
        ar_list = ["id", "x", "y", "size"]
        if args:
            for i in range(len(args)):
                setattr(self, ar_list[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

# Size -----------------------------------------------------------------------
    @property
    def size(self):
        """Getter for size attribute"""
        return self.height

    @size.setter
    def size(self, value):
        """Setter for size in method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
