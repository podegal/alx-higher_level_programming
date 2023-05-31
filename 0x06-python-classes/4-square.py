#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Defines a square with size private attibute
    a size property, a property setter and an area
    method"""
    def __init__(self, size=0):
        """initializes the square size"""
        self.__size = size

    @property
    def size(self):
        """retrieves the __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the __size"""
        if type(value) is not int:
            """raise error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """raise error"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square area"""
        return self.__size ** 2
