#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    units = number % 10
else:
    units = number % -10
print("Last digit of {:d} is {:d} ".format(number, units), end="")
if units == 0:
    print("and is 0")
elif units > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
