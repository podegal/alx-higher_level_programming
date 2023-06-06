#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """the function splits a text based on punctuation "?", ":", "."
    followed by 2 new lines

    Args:
        text (str): the string of text to split

    Raises:
        TypeError: if the text called with the function is not a string

        Return:
             None
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for s in text:
        if flag == 0:
            if s == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if s == '?' or s == '.' or s == ':':
                print(s)
                print()
                flag = 0
            else:
                print(s, end="")

