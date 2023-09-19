#!/usr/bin/python3
"""Dividing a matrix"""


def matrix_divided(matrix, div):
    """Divides elements of the matrix by div"""

    erm = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(
            isinstance(element, (int, float)) for element in row
            ) for row in matrix
            ):
        raise TypeError(erm)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_matrix_row = []
        for element in row:
            new_matrix_row.append(round(element / div, 2))
        new_matrix.append(new_matrix_row)

    return new_matrix
