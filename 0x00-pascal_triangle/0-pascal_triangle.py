#!/usr/bin/python3
'''
    Module that prints list of lists of
    integers representing Pascals triangle
'''

from typing import List


def pascal_triangle(n: int) -> List[list]:
    '''
    function that implements Pascal's triangle
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(triangle[-1])-1):
            a = triangle[-1][j]
            b = triangle[-1][j+1]
            temp.insert(-1, a + b)
        triangle.append(temp)

    return triangle