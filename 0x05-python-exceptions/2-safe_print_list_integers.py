#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ''' Prints only the first x integer of my_list'''
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
