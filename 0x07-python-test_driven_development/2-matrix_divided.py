#!/usr/bin/python3
"""
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor and round the results.
    """
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                    )

            if not all(len(row) == len(matrix[0]) for row in matrix):
                raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix
            ]
    return new_matrix


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
