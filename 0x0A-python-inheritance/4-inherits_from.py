#!/usr/bin/python3
""" Checking if Object is an instance of a class that
    inherited (directly or indirectly) from a specified class
"""


def inherits_from(obj, a_class):
    """ Function that retuns True if an object is is directly
        from a specific class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
