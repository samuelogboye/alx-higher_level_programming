#!/usr/bin/python3
"""A function  that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Opends the file and prints the content"""

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line)
