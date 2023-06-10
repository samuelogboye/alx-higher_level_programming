#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for horizontal in matrix:
        for vertical in horizontal:
            if vertical == horizontal[-1]:
                print("{:d}".format(vertical), end="")
            else:
                print("{:d}".format(vertical), end=" ")
        print()
