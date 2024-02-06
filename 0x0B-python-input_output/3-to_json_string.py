#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):

    """
    Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        A JSON string representing the object.
    """
    return json.dumps(my_obj)
