#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(list(map(lambda num: num ** 2, row)) for row in matrix)
