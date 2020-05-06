#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for even in my_list:
        if even % 2 == 0:
            a.append(True)
        else:
            a.append(False)
    return a
