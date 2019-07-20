#!/usr/bin/python3
"""Task 8"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits width and height from parent class

    Args
    width: int width
    height: int height
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
