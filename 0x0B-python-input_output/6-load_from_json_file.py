#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):

    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file to load
        the object from.

    Returns:
        The object represented by the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
