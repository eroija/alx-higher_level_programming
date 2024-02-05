#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:

    """Reprsent base geometry."""
    def area(self):

        """
        Raises an Exception with the message
        'area() is not implemented.'
        raise Exception("area() is not implemented")
        """
    def integer_validator(self, name, value):

        """
        Validates the value as an integer and greater
        than 0.

        Args:
            name: A string representing the name of
            the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or
            equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
