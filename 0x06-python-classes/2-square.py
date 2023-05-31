#!/usr/bin/python3

class Square:
    """Defines a Square with a private instance size attribute
    and a validation on the size"""

    def __init__(self, size=0):
        """Initialize the size of the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
