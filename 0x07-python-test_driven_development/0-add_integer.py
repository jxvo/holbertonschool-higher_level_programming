#!/usr/bin/python3
def add_integer(a, b=98):
        """ fad  """
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        return a + b
