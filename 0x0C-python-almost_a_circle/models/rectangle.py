#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):

    """Represent a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):

        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The id of the rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):

            """Getter for the width attribute."""
            return self.__width

        @width.setter
        def width(self, value):

            """Setter for the width attribute."""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):

            """Getter for the height attribute."""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for the height attribute."""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):

            """Getter for the x attribute."""
            return self.__x

        @x.setter
        def x(self, value):

            """Setter for the x attribute."""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):

            """Getter for the y attribute."""
            return self.__y

        @y.setter
        def y(self, value):

            """Setter for the y attribute."""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """Return the area of the Rectangle."""
            return self.width * self.height

        def display(self):

            """ displays a rectangle """
            rectangle = self.y * "\n"
            for i in range(self.height):
                rectangle += (" " * self.x)
                rectangle += ("#" * self.width) + "\n"

            print(rectangle, end='')

        def __str__(self):

            """Return the print() and str() representation of the Rectangle."""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.x, self.y, self.width, self.height)

        def update(self, *args, **kwargs):
            """Update the attributes of the Rectangle."""
            if args is not None and len(args) is not 0:
                list_atr = ['id', 'width', 'height', 'x', 'y']
                for i in range(len(args)):
                    setattr(self, list_atr[i], args[i])
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

        def to_dictionary(self):
            """ Returns a dictionary with attributes """
            return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
