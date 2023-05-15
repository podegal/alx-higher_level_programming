#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for xter in my_string:
        if (xter != 'c' and xter != 'C'):
            newString += xter
    return (newString)
