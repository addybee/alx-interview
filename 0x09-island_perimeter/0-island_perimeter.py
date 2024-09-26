#!/usr/bin/python3
""" island perimeter problem solution"""


def island_perimeter(grid):
    """"""
    perimeter = 0
    # iterate through the grid
    # skip the first and last rows and columns
    for row in range(1, (len(grid) - 1)):
        for col in range(1, len(grid[row]) - 1):
            # check if a cell is a land (1)
            if grid[row][col]:
                # check for no land(0 cell) on the left of current land(cell)
                if not grid[row][col-1]:
                    # add 1 to perimeter
                    perimeter += 1
                # check for no land(0 cell) on the top of current land(cell)
                if not grid[row-1][col]:
                    # add 1 to perimeter
                    perimeter += 1
                # check for no land(0 cell) on the right of current land(cell)
                if not grid[row][col+1]:
                    # add 1 to perimeter
                    perimeter += 1
                # check for no land(0 cell) on the bottom of current land(cell)
                if not grid[row+1][col]:
                    # add 1 to perimeter
                    perimeter += 1
    return perimeter
