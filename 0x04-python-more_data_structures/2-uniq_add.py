#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_of_uniqueintegers = 0
    for i in set(my_list):
        sum_of_uniqueintegers += i
    return sum_of_uniqueintegers
