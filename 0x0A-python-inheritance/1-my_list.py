#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
