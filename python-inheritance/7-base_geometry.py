#!/usr/bin/python3
"""Integer Validation"""


class BaseGeometry:
    """The empty base class"""
    def area(self):
        """Raise an exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Using integer_value to determine status of name and value

        Args:
            name (string): Public instance attribute
            value (integer): Public instance attribute

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
