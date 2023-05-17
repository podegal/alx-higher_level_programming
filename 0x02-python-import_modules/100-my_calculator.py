#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    num_args = len(argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>"
        exit(1)

    operator = argv[2]
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if operator == '+':
        print("{} + {} = {:d}".format(argv[1], argv[3], add(a, b)))
    elif operator == '-':
        print("{} - {} = {:d}".format(argv[1], argv[3], sub((a), (b))))
    elif operator == '*':
        print("{} * {} = {:d}".format(argv[1], argv[3], mul((a), (b))))
    else:
        print("{} / {} = {:d}".format(argv[1], argv[3], div((a), (b))))
