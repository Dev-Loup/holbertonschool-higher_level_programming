#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        first_lenchar = (len(sentence), sentence[0])
    else:
        first_lenchar = (0, None)
    return first_lenchar
