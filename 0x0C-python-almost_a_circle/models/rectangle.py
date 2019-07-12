#!/usr/bin/python3
"""module for Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Contains grid position and height/width attributes,
    inherits ID from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle

        Arguments:
        width: int width
        height: int height
        x: int x-coordinate
        y: int y-coordinate
        id: object ID (inherited)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates and sets private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates and sets private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates and sets private attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """validates and sets private attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
