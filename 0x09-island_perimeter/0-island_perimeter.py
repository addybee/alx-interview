#!/usr/bin/python3
""" Solution for calculating the perimeter of an island in a grid. """


def island_perimeter(grid):
    """
    Calculate the perimeter of the island represented by 1s in the grid.

    Args:
        grid (list of list of int): 2D grid where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Iterate over the entire grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is land (1)
            if grid[row][col] == 1:
                # Check each neighboring cell (left, top, right, bottom)
                # and add to the perimeter if it's water or out of bounds
                if row == 0 or grid[row - 1][col] == 0:  # Top
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Left
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:  # Bottom
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
