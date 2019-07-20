#!/usr/bin/python3
"""Advanced Task 13"""
def add_attribute(obj, attr, value):
    if not isinstance(obj, (str, int)):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
