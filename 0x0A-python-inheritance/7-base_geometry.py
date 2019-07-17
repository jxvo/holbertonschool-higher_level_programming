#!/usr/bin/python3
"""task 5"""


class BaseGeometry():
    """only contains area for now"""
    def area(self):
        """does nothing for now"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
