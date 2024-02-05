#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):

    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will
        be added.
        name: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have
        new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
