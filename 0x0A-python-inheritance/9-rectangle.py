#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Represent a rectangle using BaseGeometry.
    """
    def __init__(self, width, height):

        """
        Initializes a Rectangle instance with
        width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):

        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):

        """eturns the rectangle description."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
