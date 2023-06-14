#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurences of an element by another"""
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
