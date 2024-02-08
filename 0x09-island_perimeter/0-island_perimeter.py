#!/usr/bin/python3
'''
    implementation of the solution to the
    Island Perimeter interview question
'''


def island_perimeter(grid):
    '''
        function that finds perimeter
    '''
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # count all 4 sides initially

                # Check adjacent cells and subtract if neighbor is land
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


if __name__ == "__main__":
    pass
