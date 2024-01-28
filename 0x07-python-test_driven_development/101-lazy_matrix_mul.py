#!/usr/bin/python3
"""This defines a matrix multiplication using Numpy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):

    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix.
    """

    return (np.matmul(m_a, m_b))
