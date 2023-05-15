#!/usr/bin/python3
def multiple_returns(sentence):
    """tuple that returns the length of a string and its first character."""
    newtuple = ()
    if len(sentence) == 0:
        newtuple = 0, "None"
    else:
        newtuple = len(sentence), sentence[0]
    return newtuple
