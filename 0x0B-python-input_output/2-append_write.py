#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):

    """
    Appends a string at the end of a text file (UTF8).

    Args:
        filename: The name of the file to append to.
        text: The text to be appended to the file.

    Returns:
        The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
