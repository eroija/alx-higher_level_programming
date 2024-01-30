#!/usr/bin/python3
"""Defines a class square"""


class Square:

    """
    This class represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):

        """
        Initializes a new instance of the Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """

        self.size = size
        self.position = position

    @property
    def size(self):

        """
        Gets the size of the square.

        Returns:
            The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        """
        Gets the position of the square.

        Returns:
            The position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):

        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2
            positive integers.
        """

        if not isinstance(value, tuple) or len(value) != 2 \
        or not all(isinstance(i, int) and i > 0 for i in value):

