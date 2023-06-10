#!/usr/bin/python3
def max_integer(my_list=[]):
    """A function that finds the biggest integer of a list"""

    if len(my_list) == 0:
        return None
    else:
        my_list.sort()
        biggest_int = my_list[-1]
    return biggest_int
