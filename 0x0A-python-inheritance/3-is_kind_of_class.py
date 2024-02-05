#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):

    """
    Checks if an object is an instance of or if the object
    is an instance of a class that inherited from it.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with.

    Returns:
        True if the object is an instance of or inherited
        from the specified class; False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
