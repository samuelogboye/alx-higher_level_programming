#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return None
