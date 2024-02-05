#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):

    """Invert int operators == and !=."""
    def __eq__(self, other):

        """Overrides the == operator."""
        return not super().__eq__(other)

    def __ne__(self, other):

        """Overrides the != operator."""
        return not super().__ne__(other)
