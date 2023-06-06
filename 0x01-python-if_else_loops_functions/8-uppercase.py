#!/usr/bin/python3
def uppercase(str):
    modified_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        modified_str += char
    print("{}".format(modified_str))
