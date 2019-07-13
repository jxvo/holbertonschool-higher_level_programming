#!/usr/bin/python3
"""module for Base model"""
import json


class Base:
    """Base class contains methods and id for all data models"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of Base

        id: set to number of base objects created if not already provided
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON representation of a list of objects to a file"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w+") as json_file:
                json_file.write(cls.to_json_string(None))
        else:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w+") as json_file:
                json_file.write(cls.to_json_string(dict_list))
