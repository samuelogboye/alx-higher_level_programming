#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints all integers of a list in reverse order"""
    for num in range(len(my_list), 0, -1):
        print("{:d}".format(num))
