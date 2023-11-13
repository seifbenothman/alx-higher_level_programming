#!/usr/bin/python3
"""Base class"""
import turtle
import json
import csv


class Base:
    """Managing id attribute"""

    # Class variable to keep track of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance with an id or create a new id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw using Turtle graphics"""
        turtle.speed(2)

        # Draw rectangles
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)

        # Draw squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list of instances from JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Load list of instances from file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                contents = file.read()
                list_dicts = cls.from_json_string(contents)
                return [cls.create(**obj) for obj in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dummy = Square(1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

        class Square(Rectangle):
            """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
