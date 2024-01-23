#!/usr/bin/python3
"""Define a class square"""


class Square:

    """
    This class represents a square.

    Attributes:
        - __size (int): The size of the square.

    Methods:
        - __init__(self, size=0): Initializes a new instance of
        the Square class with an optional size.
        size(self): Getter method to retrieve the size of the square.
        - size(self, value): Setter method to set the size of the square.
        - area(self): Calculates and returns the area of the square.
        - my_print(self): Prints the square using '#' characters.
    """

    def __init__(self, size=0):

        """
        Initializes a new instance of the Square class with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.__size = size

    @property
    def size(self):

        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setteri
    def size(self, value):

        """
        Setter method to set the size of the square.

        Args:
            value (int): The new size for the square.

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
        Calculates and returns the area of the square.

        Returns:
             int: The area of the square.
        """

        return self.__size ** 2

    def my_print(self):

        """
        Prints the square using '#' characters.

        If size is equal to 0, prints an empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
