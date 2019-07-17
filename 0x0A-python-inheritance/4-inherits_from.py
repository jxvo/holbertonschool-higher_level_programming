#!/usr/bin/python3
"""task 4"""


def inherits_from(obj, a_class):
    """does this object inherit from this class? True or False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
