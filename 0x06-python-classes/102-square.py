#!/usr/bin/python3
class Square:
    """contains methods for our shape"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize an instance of a square"""
        self.size = size
        self.position = position

    def __str__(self):
        """overwrite string representation to draw square from '#' characters"""
        row = []
        if self.__size == 0:
            return ""
        for idx in range(self.position[1]):
            row.append("")
        for idx in range(self.__size):
            row.append(' ' * self.__position[0] + '#' * self.__size)
        return '\n'.join(row)

    def __eq__(self, other):
        """compare areas using  == operator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """compare areas using != operator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """compare areas using > operator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """compare areas using >= operator"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """compare areas using < operator"""
        return self.area() < other.area()

    def __le__(self, other):
        """compare areas using <= operator"""
        return self.area() <= other.area()

    @property
    def size(self):
        """returns private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """validates and sets private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size mmust be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns private attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """validates and sets private attribute"""
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area"""
        return self.__size ** 2

    def my_print(self):
        """prints our shape built out of '#' characters"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
