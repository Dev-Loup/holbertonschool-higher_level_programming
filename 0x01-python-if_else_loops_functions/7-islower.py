#!/usr/bin/python3
def islower(c):
    chrcode = ord(c)
    if chrcode >= 97 and chrcode <= 122:
        return True
    else:
        return False
