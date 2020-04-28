#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    units = number % 10
else:
    units = number % -10
if units == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, units))
elif units > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, units))
else:
    print("Last digit of {:d} is {} and is less than 6 and not 0".format(number, units))
