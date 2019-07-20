#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
     __slots__ = ["first_name"]

try:
    a = MyClass()
    add_attribute(a, "hbtn", "Holberton")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
