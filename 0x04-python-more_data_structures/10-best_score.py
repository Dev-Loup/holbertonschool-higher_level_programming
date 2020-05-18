#!/usr/bin/python3
def best_score(a_dictionary):
    topper = None
    score = 0
    if a_dictionary is not None:
        for key in a_dictionary.keys():
            value = a_dictionary[key]
            if value > score:
                score = value
                topper = key
    return topper
