#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    n2 = int(argv[3])
    math = [['+', add], ['-', sub], ['*', mul], ['/', div]]
    for op in math:
        if op[0] == argv[2]:
            print("{} {} {} = {}".format(n1, argv[2], n2, op[1](n1, n2)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
