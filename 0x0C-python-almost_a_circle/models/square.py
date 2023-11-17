#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Size attribute setter"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Update attributes based on arguments and keyword arguments"""
        attributes = ["id", "size", "x", "y"]
        
        if args:
            for i, value in enumerate(args):
                setattr(self, key, value)

    def __str__(self):
        """Return string"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )
    def to_dictionary(self):
        """Return the dictionary"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y,
                }
