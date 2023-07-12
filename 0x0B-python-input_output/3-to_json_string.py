#!/usr/bin/python3
"""Import json module"""
import json
"""Module to dump"""


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an
    object (string)"""
    return json.dumps(my_obj, sort_keys=True)
