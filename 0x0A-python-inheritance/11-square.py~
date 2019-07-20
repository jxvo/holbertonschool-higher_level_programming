#!/usr/bin/python3
"""Task 10"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """like a rectange, but square"""
    def __init__(self, size):
        """initialize a new instance of a square"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
