#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):

        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):

        """Return string representation of the Square."""
        s1 = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"
        s2 = str(self.y) + " - " + str(self.width)
        s = s1 + s2
        return s

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square."""
        if 'size' in kwargs:
            kwargs['width'] = kwargs['size']
            kwargs['height'] = kwargs['size']
            del kwargs['size']
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the Square."""
        {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
