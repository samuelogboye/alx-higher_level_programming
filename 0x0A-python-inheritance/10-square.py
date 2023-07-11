#!/usr/bin/python3
"""Importing from 7's BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
