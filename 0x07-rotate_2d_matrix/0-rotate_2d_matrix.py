#!/usr/bin/python3

def transpose_in_place(matrix: list) -> None:
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

if __name__ == "__main__":
    rotate_2d_matrix()
