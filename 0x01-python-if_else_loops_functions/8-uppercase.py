#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if str[c] >= "a" and str[c] <= "z":
            uppercaser = ord(str[c])
            uppercaser -= 32
            letter = chr(uppercaser)
        else:
            letter = str[c]
        print("{}".format(letter), end="")
    print()
