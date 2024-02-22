#!/usr/bin/python3
"""
0-ratate_2d_matrix.py - a function that rotates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    Args:
        matrix (List): 2D matrix to be rotated
    """
    if len(matrix) <= 0:
        return
    if type(matrix) != list:
        return
    if not all(isinstance(row, list) for row in matrix):
        return

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    