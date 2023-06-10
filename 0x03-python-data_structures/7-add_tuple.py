#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds 2 tuples"""
    a_value_one = 0
    a_value_two = 0
    b_value_one = 0
    b_value_two = 0

    try:
        a_value_one = tuple_a[0]
        a_value_two = tuple_a[1]
        b_value_one = tuple_b[0]
        b_value_two = tuple_b[1]
    except IndexError:
        pass

    if a_value_one == 0:
        a_value_one = 0
    if a_value_two == 0:
        a_value_two = 0
    if b_value_one == 0:
        b_value_one = 0
    if b_value_two == 0:
        b_value_two = 0

    value_one = a_value_one + b_value_one
    value_two = a_value_two + b_value_two
    return value_one, value_two
