#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise inplace
    """

    matrix_len = len(matrix)

    # transpose the matrix (convert rows to columns)
    for i in range(matrix_len):
        for j in range(i, matrix_len):
            # swap elements at position (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90 degree rotation
    for i in range(matrix_len):
        matrix[i].reverse()
