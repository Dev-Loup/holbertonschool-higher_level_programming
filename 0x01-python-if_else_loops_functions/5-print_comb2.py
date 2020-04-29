#!/usr/bin/python3
for num in range(0, 100):
    print("{:0>2d}".format(num),end="")
    if num != 99:
        print(", ",end="")
