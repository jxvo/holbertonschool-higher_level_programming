#!/usr/bin/python3
"""Advanced Task 13"""
def add_attribute(obj, attr, value):
    if hasattr(obj, "__dict__") or  hasattr(obj, "__slots__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
