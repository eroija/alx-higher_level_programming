#!/usr/bin/python3
"""It that defines a name printing function"""


def say_my_name(first_name, last_name=""):

    """
    Prints a message with the given first name and
    last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.
        Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Returns:
        TypeError: if first_name and last_name are
        not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
