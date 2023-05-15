#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples2 = []
    for i in range(len(my_list)):
        if multiples2[i] % 2 == 0:
            multiples2.append(True)
        else:
            multiples2.append(False)
    return multiples2
