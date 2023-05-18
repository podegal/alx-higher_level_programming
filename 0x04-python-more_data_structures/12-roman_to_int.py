#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    
    num = 0

    roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    for i in range(len(roman_string)):
        if roman_num.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_dict[roman_string[i]] < roman_num[roman_string[i + 1]]):
                num += roman_num[roman_string[i]] * -1

        else:
            num += roman_num[roman_string[i]]
    return num
