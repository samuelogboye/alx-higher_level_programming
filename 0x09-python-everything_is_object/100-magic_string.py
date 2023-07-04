#!/usr/bin/python3
def magic_string():
    magic_string.count = magic_string.count + 1 if hasattr(magic_string, 'counter') else 1
    return ', '.join(['BestSchool'] * magic_string.counter)
