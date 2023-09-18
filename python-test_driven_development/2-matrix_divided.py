#!/usr/bin/python3
"""Dividing a matrix"""


def matrix_divided(matrix, div):
    """Dives elements of the matrix by div"""
    for row in matrix:
        if not isinstance(row, list) or not all(isinstance(element, (int, float)) for element in row):
            return False
        return True

    if not matrix_divided(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
