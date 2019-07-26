#!/usr/bin/python3
"""module for Base model"""
import json
import os.path
import csv
import turtle
import random

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

    @classmethod
    def create(cls, **dictionary):
        """return a new instance with attrs taken int from a dictionary"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

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

    @classmethod
    def load_from_file(cls):
        """load a list of instances from a JSON file"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as json_file:
            obj_list = cls.from_json_string(json_file.read())
        return [cls.create(**attributes) for attributes in obj_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes CSV representation of a list of objects to a CSV file"""
        if list_objs is None:
            list_objs = []
        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            attrs = ["id", "size", "x", "y"]
        """each index will now contain a list of attribute values in order"""
        list_objs = [[getattr(obj, atr) for atr in attrs] for obj in list_objs]
        with open(cls.__name__ + ".csv", "w+", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for obj in list_objs:
                writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """creates a list of instances from a CSV file"""
        list_objs = []

        if not os.path.exists(cls.__name__ + ".csv"):
            return list_objs
        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            attrs = ["id", "size", "x", "y"]
        with open(cls.__name__ + ".csv", "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file, attrs)
            for row in reader:
                list_objs.append({key: int(val) for key, val in row.items()})
        return [cls.create(**attributes) for attributes in list_objs]

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries from a JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw our shapes using the turtle module"""
        colors = ["red", "purple", "violet", "blue", "teal",
                  "green", "neon", "yellow", "orange"]
        window = turtle.Screen()
        window.bgcolor("black")
        window.title("TURTLE TIME >:D")
        timmy = turtle.Turtle()
        turtle.shape("turtle")
        for shapes in list_rectangles + list_squares:
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.goto(shape.x, shape.y)
            turtle.pendown()
            for steps in range(4):
                turtle.forward(shape.height)
                turtle.left(random.randint(22, 77))
                turtle.forward(shape.width)
                turtle.right(90)
                turtle.forward(shape.height)
                turtle.right(random.randint(22, 77))
                turtle.forward(shape.width)
                turtle.left(90)
        turtle.exitonclick()
