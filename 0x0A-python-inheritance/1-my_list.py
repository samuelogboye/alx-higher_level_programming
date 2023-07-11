#!/usr/bin/python3
"""This module returns a sorted list"""


class MyList(list):
    """A class attribute that inherit from list and return
    the list sorted"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
