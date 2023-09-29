#!/usr/bin/python3
"""
A module to check peak
"""


def find_peak(list_of_integers):
    """
    Function that finds the peak of an unsorted
    list
    """
    if not list_of_integers:
        return None

    right, left = 0, len(list_of_integers) - 1

    while right < left:
        num = (right + left) // 2
        if list_of_integers[num] < list_of_integers[num + 1]:
            right = num + 1
        else:
            left = num

    return list_of_integers[right]
