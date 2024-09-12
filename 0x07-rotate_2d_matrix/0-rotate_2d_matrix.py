#!/usr/bin/python3
""" module for matrix rotation """


def rotate_2d_matrix(matrix):
    """
        Rotate a N x N matrix by 90 degreee in clockwise direction using
        Inplace rotate square matrix by 90 degrees by forming cycles
    """
    N = len(matrix)
    # consider all square one by one
    for x in range(int(N / 2)):
        # Consider elements in group of 4 in current square
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N-y-1][x]
            matrix[N-y-1][x] = matrix[N-x-1][N-y-1]
            matrix[N-x-1][N-y-1] = matrix[y][N-x-1]
            matrix[y][N-x-1] = temp
