#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = []
    for row in matrix:
        row = list(map(lambda x: x**2, row))
        mtx.append(row)
    return mtx
