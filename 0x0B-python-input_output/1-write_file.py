#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):

    """
    Writes a string to a text file (UTF8)

    Args:
        filename: The name of the file to write to.
        text: The text to be written to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
