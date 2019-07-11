#!/usr/bin/python3
"""Rectangle model that inherits from base"""
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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """returns private attribute"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets width"""
            self.__width = value

        @property
        def height(self):
            """returns private attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height"""
            self.__height = value

        @property
        def x(self):
            """returns private attribute"""
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            """returns private attribute"""
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
