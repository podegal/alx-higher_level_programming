#!/usr/bin/python3
"""Magic class to define a circle object"""
import math


class MagicClass:
    """ a magic class that creates a circle and evalutes
    its area and circumference"""
    def __init__(self, radius=0):
        """initialize the radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        """evaluates the area of the circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """evaluates the circumference of the circle"""
        return (2 * math.pi * self.__radius)
