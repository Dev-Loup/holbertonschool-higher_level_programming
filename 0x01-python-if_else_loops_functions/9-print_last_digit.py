#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        units = number % 10
    else:
        units = (number * -1) % 10
    print("{:d}".format(units), end="")
    return units
