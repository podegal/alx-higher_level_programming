#!/usr/bin/python3

"""
Defines a function that divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
       Divides all elements of a matrix by a number
       Args:
           matrix: list of lists with the same length
           div: number by which to divide
       Return:
           a new matrix of the same size
    """
    division_matrix = [[]]

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    division_matrix = [[round(i/div, 2) for i in row] for row in matrix]

    return (division_matrix)
