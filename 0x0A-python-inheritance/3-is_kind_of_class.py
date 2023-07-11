#!/usr/bin/python3
"""Checking the instance of class object"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True if an instance is of,
        or if the object is an instance of a class that inherited from,
        the specified class; otherwise False."""

    return isinstance(obj, a_class)
