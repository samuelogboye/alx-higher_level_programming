#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A function that computes the squate value of all integers of a matrix"""
    new_mat = matrix.copy()
    final = []
    for i in new_mat:
        row = list(map(lambda x: x ** 2, i))
        final.append(row)
    return final
