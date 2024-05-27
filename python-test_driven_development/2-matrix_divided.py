#!/usr/bin/python3
"""
    Divide Matrix
"""


def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be number")
    if div is 0:
        raise ZeroDivisionError("division zero")

