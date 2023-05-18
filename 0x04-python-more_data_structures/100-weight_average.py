#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    total = 0 
    val = 0

    for i in my_list:
        total += i[0] * i[1]
        val += i[1]
    return total / val
