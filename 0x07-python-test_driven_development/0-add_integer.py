#!/usr/bin/python3
"""An integer addition function"""


def add_integer(a, b=98):

    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number.
        Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: The addition of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
