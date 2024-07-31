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
    if type(grid) != list:
        return 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(rows) and k[1] in range(cols) else 0
                     for k in idx]

            if grid[i][j]:
                perimeter += sum([1 if not r or not grid[k[0]][k[1]] else 0
                                  for r, k in zip(check, idx)])
    return perimeter
