#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    check = len(tuple_a)
    check2 = len(tuple_b)
    for index in range(2):
        if check > index:
            a[index] += tuple_a[index]
        if check2 > index:
            a[index] += tuple_b[index]
    tup_add = tuple(a)
    return tup_add
