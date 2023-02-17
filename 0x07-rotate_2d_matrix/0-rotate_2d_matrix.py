#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """n x n 2D matrix, rotate it
    90 degrees clockwise"""
    width = len(matrix[0])
    for i in range(width // 2):
        for j in range(i, width - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[width - 1 - j][i]
            matrix[width - 1 - j][i] = matrix[width - 1 - i][width - 1 - j]
            matrix[width - 1 - i][width - 1 - j] = matrix[j][width - 1 - i]
            matrix[j][width - 1 - i] = temp
