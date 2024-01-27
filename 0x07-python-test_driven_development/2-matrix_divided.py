#!/usr/bin/python3
"""It defines a matrix division function"""


def matrix_divided(matrix, div):

    """
    Divides all elements of a matrix

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of
        integers or floats.
        TypeError: If each row of the matrix does not
        have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: The new matrix with elements divided by
        div, rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or matrix == [] or
    not all(isinstance(row, list) for row in matrix) or
    not all(isinstance(ele, int) or isinstance(ele, float))
    for (ele in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ((list(map(lambda x: round(x / div, 2), row)) for row in matrix))
