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

        def to_dictionary(self):
            """Return the dictionary"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
    def __str__(self):
        """Return string"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )
    if __name__ == "__main__":
        s1 = Square(5)
        print(s1)

        s1.update(10)
        print(s1)

        s1.update(1, 2)
        print(s1)

        s1.update(1, 2, 3)
        print(s1)

        s1.update(1, 2, 3, 4)
        print(s1)

        s1.update(x=12)
        print(s1)
        
        s1.update(size=7, y=1)
        print(s1)

        s1.update(size=7, id=89, y=1)
        print(s1)
