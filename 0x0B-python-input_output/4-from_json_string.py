#!/usr/bin/python3
"""Import json module"""
import json
"""Module for json loads"""


def from_json_string(my_str):
    """ a function that returns an object represented by
    JSON string"""
    return json.loads(my_str)
