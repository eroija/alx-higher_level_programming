#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:

    """Class represents a rectangle"""

    def __init__(self, width=0, height=0):

        """
        Constructor for the Rectangle class

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """
        Getter method for retrieving the width attribute.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):

        """
        Setter method for setting the width attribute.

        Args:
            value (int): The value to set as the width.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """
        Getter method for retrieving the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):

        """
        Setter method for setting the height attribute.

        Args:
            value (int): The value to set as the height.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
