#!/usr/bin/python3
def matrix_divided(matrix, div):
    """all elements of matrix (list of lists) are divided by div"""

    __long_error = "matrix must be a matrix (list of lists) of integers/floats"

    if len(matrix) < 1:
        raise TypeError(__long_error)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be an integer")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        if len(row) < 1:
            raise TypeError(__long_error)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(__long_error)
            new_row.append(round(val / div, 2))
        new_matrix.append(new_row)
    return new_matrix
