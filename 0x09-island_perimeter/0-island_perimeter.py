#!/usr/bin/python3
"""
interview challange that gets the perimeter of an island
"""


def island_perimeter(grid):
    """return the perimeter of the island described in
    grid"""
    peri = 0
    len_row = len(grid[0])
    len_grid = len(grid)
    for row in range(len_grid):
        for col in range(len_row):
            if grid[row][col]:
                if (row - 1 >= 0 and grid[row - 1]
                        and not (grid[row - 1][col])) or row == 0:
                    peri += 1
                if (row + 1 <= (len_grid - 1) and grid[row + 1]
                        and not grid[row + 1][col]) or row == len_grid - 1:
                    peri += 1
                if col - 1 >= 0 and grid[row][col - 1]:
                    pass
                else:
                    peri += 1
                if col + 1 <= len_row - 1 and grid[row][col + 1]:
                    pass
                else:
                    peri += 1
    return peri
