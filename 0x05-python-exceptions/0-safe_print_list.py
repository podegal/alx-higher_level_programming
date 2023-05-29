#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' Prints x elements of my_list'''
    count = 0
    item = my_list[i]
    for i in range(x):
        try:
            print(item, end="")
            count += 1
        except IndexError:
            break
    print()
    return (count)
