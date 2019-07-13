#!/usr/bin/python3
"""module for Square class that inherits from Rectangle"""
from models.base import Base
from models.rectangle import Rectangle

attrs = ["id", "size", "x", "y"]

class Square(Rectangle):
    """like a rectangle, but square (no width/height, just size)"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize a new square

        Arguments
        size: int (inherited)
        x: int x-coordinate (inherited)
        y: int y-coordinate (inherited)
        id: object ID (inherited)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwrites the string represetation of the square's attributes"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """updates the square's attributes using args or kw-args"""
        if args:
            for idx in range(len(args)):
                if args[idx]:
                    setattr(self, attrs[idx], args[idx])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary of the square's attributes"""
        this_dict = {}
        for idx in attrs:
            this_dict.update({idx: getattr(self, idx)})
        return this_dict

    @property
    def size(self):
        """returns rectangle's private width attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """resets private attributes so be more sqaure-like"""
        self.width = value
        self.height = value
