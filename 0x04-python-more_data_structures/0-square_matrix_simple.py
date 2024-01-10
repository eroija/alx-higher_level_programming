#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    total = [[0 for x in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total[i][j] = matrix[i][j] ** 2
    return total
