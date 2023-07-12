#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """
        returns dictionary representation with simple data structure.
    """
    return obj.__dict__
