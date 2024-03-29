#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):

    """
    Returns an object represented by a JSON string.

    Args:
        my_str: The JSON string to be converted to
        a Python data structure.

    Returns:
        An object represented by the JSON string.
    """
    return json.loads(my_str)
