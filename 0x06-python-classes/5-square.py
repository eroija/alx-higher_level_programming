#!/usr/bin/python3
"""Define a class square"""


class Square:

    """
    This class represents a square by it's size.
    """

    def __init__(self, size=0):

        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size

    @property
    def size(self):

        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """
        Calculates the area of the square.

        Returns:
             int: The area of the square.
        """

        return self.__size * self.__size

    def my_print(self):

        """
        Prints the square using the '#' character.
        """

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()
