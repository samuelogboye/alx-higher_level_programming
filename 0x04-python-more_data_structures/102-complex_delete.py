#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """a function that deletes keys with a specific value in a dictionary"""
    keys_to_delete = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
