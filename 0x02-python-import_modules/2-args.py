#!/usr/bin/python3
if __name__ == "__main__":
    import sys import argv
    num_of_arg = len(argv)-1
    if num_of_arg == 0:
        print("0 arguments")
    elif num_of_arg == 1:
        print("1 argument")
    else:
        print("{} arguments:".format(num_of_arg))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
