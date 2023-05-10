#!/usr/bin/python3
def uppercase(str):
    for charc in str:
        if (ord(charc) >= 97) and (ord(charc) <= 122):
            charc = chr(ord(charc) - 32)
        print("{}".format(charc), end="")
    print()
