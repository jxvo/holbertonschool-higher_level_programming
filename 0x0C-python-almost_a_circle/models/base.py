#!/usr/bin/python3
"""module for Base model"""


class Base:
    """Base class contains methods and id for all data models"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base

        id: set to number of base objects created if not already provided
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
