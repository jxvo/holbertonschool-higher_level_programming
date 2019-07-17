#!/usr/bin/python3
class LockedClass:
    """allows no other new attributes to be created"""
    __slots__ = "first_name"
