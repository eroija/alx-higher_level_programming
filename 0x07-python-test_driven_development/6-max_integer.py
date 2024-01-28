#!/usr/bin/python3
"""This module finds max integer in a list"""


def max_integer(list=[]):

    """
    This function finds and returns the max integer
    in list of integers

    Returns:
        none if list is empty
    """

    if len(list) == 0:
        return None
    result = list[0]

    j = 1
    while j < len(list):
        if list[j] > result:
            result = list[j]
        j += 1
    return result
