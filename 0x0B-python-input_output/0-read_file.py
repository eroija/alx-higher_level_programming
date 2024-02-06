#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):

    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The name of the file to be read.
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
