#!/usr/bin/python3
""" An Island Perimeter """


def island_perimeter(grid):
    """  returns the perimeter of the island described in grid.
            - grid is a list of list of integers:
                0 represents water
                1 represents land
                Each cell is square, with a side length of 1
                Cells are connected horizontally/vertically (not diagonally).
                grid is rectangular, width and height not exceeding 100.
            - The grid is completely surrounded by water.
            - There is only one island (or nothing).
            - The island doesn’t have “lakes” (water inside that isn’t
                connected to the water surrounding the island).
    Args:
        grid (array): An array of lists that represent an island.
    Returns:
        The perimeter of the Island
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
