#!/usr/bin/python3
"""A module for a square"""


class Square:

    """
    This class represents a square.

    Attributes:
        - size (int): The size of the square.

    Methods:
        - __init__(self, size): Initializes a new instance
        of the Square class with a given size.
    """

    def __init__(self, size):

        """
        Initializes a new instance of the Square
        class with a given size.

        Args:
            size (int): The size of the square.
        """

        self.__size = size
