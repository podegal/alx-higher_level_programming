#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Defines a square with private size attibute
    a size property, a property setter and an area
    method"""
    def __init__(self, size=0):
        """Initializes the size"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
