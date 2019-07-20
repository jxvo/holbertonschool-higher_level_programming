#!/usr/bin/python3
"""Advanced Task 12"""


class MyInt(int):
    """MyInt is a rebel that has == and != operators inverted"""
    def __eq__(self, other):
        """when obj is compared as == it should be interpreted as !="""
        return super() != other

    def __ne__(self, other):
        return super() == other
