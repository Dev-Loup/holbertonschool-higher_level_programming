#!/usr/bin/python3
"""
  2-matrix_divided module.
  Matrix division functions
  Functions:
    matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
      Divides all the elements of a matrix
      by a divisor, result is rounded by two
      decimal places.

      Args:
        matrix: list of lists containing dividends
        div: divisor
      Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
      Return:
        Addition type int
    """
    tperror = 0
    result = []
    indX = 0
    size = 0

    if type(matrix) is list:
        if type(div) not in {int, float}:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for X in matrix:
            if size == 0:
                size = len(X)
            elif size is not len(X):
                raise TypeError("Each row of the matrix " +
                                "must have the same size")
            if tperror == 1:
                break
            if type(X) is list:
                result.append([])
                for num in X:
                    if type(num) in (int, float):
                        result[indX].append(round(num / div, 2))
                    else:
                        tperror = 1
                        break
                indX += 1
            else:
                tperror = 1
    else:
        tperror = 1
    if tperror == 1 or len(matrix) == 0:
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")
    return (result)
