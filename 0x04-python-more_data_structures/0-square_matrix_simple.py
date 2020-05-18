#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for line in matrix:
        nmatrix.append(list(line))
    for line in nmatrix:
        for number in range(len(line)):
            line[number] = line[number] ** 2
    return nmatrix
