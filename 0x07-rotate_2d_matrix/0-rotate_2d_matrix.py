#!/usr/bin/python3
'''
    module that reverses a matrix in place
'''


'''def transpose_in_place(matrix: list) -> None:
    '''
        Transposes a matrix in-place
    '''
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            # Swap elements (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix: list) -> None:
    '''
        reverses a list
    '''

    rows, cols = len(matrix), len(matrix[0])

    for i in range(cols):
        for j in range(rows // 2):
            matrix[j][i], matrix[rows - j - 1][i] = (
                matrix[rows - j - 1][i],
                matrix[j][i]
            )


def rotate_2d_matrix(matrix: list) -> None:
    '''
        rotates a 2d matrix
    '''
    transpose_in_place(matrix)
    reverse_matrix(matrix)
'''


def transpose_matrix(matrix, n):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    n = len(matrix)
    # print(n)

    """sample matrix
    1 2 3
    4 5 6
    7 8 9
    """

    # transpose matrix
    """
    1 4 7
    2 5 8
    3 6 9
    """

    transpose_matrix(matrix, n)

    # reverse matrix
    """
    7 4 1
    8 5 2
    9 6 3
    """
    reverse_matrix(matrix)

    return matrix