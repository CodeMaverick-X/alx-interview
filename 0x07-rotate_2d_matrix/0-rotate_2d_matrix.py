#!/usr/bin/python3
"""rotate 2D matrix in state"""


def rotate_2d_matrix(matrix):
    """function that rotates 2d matrx"""
    len_row = len(matrix)
    len_col = len(matrix[0])

    lst_of_col = [[] for n in range(0, len_col)]
    for k in range(0, len_col):
        for n in range(len_row - 1, -1, -1):
            lst_of_col[k] += [matrix[n][k]]

    for n in range(len_row):
        for k in range(len_col):
            matrix[n][k] = lst_of_col[n][k]
