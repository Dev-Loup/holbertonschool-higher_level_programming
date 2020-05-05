#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for X in matrix:
        for Y in X:
            print('{:d}'.format(Y), end="")
            if Y != X[-1]:
                print(' ', end="")
        print()
