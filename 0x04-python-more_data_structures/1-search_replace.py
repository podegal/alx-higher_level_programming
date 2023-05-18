#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = my_list[:]
    for a in range(len(my_list)):
        if newList[a] == search:
            newList[a] = replace
    return newList
