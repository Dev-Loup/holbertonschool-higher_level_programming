#!/usr/bin/python3
from sys import argv
num = 0
for arg in argv[1:]:
    if arg != 0:
        num += int(arg)
print("{:d}".format(num))
