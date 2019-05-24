#!/usr/bin/python3
if __name__ == "__main__":
    def add_integer(a, b=98):
        """ fad  """
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        if a is None or not isinstance(a, int):
            raise TypeError("a must be an integer")
        if b is None or not isinstance(b, int):
            raise TypeError("b must be an integer")
        return a + b
