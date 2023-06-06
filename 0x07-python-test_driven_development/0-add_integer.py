#!/usr/bin/python3
"""
add_integer is a module
a and b are its arguments
it returns sum of a and b
"""
def add_integer(a, b=98):
    """
    returns the sum of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise ValueError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise ValueError("b must be an integer")
    return (int(a) + int(b))
