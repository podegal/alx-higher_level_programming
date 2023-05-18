#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    orderedDictKeys = list(sorted(a_dictionary.keys()))
    for j in orderedDictKeys:
        print("{}: {}".format(j, a_dictionary[j]))
