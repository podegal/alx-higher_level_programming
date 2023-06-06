#!/usr/bin/python3

"""Defines a function to prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """
       Prints full name
       Args:
           first_name: first arg : str
           last_name: second arg : str (Default to empty string)
       Return:
              None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
