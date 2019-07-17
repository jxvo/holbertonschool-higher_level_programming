#!/usr/bin/python3
import math


class MagicClass:
    """do you believe in magic?"""
    def __init__(self, radius=0):
        """initialize magic object"""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """square the radius and multiply by Pi"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """get the circumference"""
        return 2 * math.pi * self.__radius
