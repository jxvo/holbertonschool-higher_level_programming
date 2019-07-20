#!/usr/bin/python3
"""Advanced Task 13"""


def add_attribute(obj, attr, value):
    """__dict__ are for dynamic attributes
    __slots__ is for pre-set attrs that can't be changed
    """
    if hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
