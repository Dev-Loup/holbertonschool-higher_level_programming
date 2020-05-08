#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        topper = None
        score = 0
        for key in a_dictionary.keys():
            value = a_dictionary[key]
            if value > score:
                score = value
                topper = key
        return topper
