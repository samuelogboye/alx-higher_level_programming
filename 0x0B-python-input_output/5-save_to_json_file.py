#!/usr/bin/python3
"""Import json module"""
import json
"""Module to write object to a text file"""


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using
    a JSON representation"""
    with open(filename, 'w',  encoding="utf-8") as f:
        json.dump(my_obj, f)
