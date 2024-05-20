#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    number_rows = len(matrix)
    number_cols = len(matrix[0])

    for i in range(0, number_rows):
        for j in range(0, number_cols):
            if j == number_cols - 1:
                print("{:d}".format(matrix[i][j], end=''))
            else:
                print("{:d}".format(matrix[i][j], end=' '))
        print()
