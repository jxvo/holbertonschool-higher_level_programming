#!/usr/bin/python3
class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None and type(attrs) is not list:
            return self.__dict__
        for attribute in attrs:
            if type(attribute) is not str:
                return self.__dict__
        obj = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                obj.update({key: value})
        return obj
