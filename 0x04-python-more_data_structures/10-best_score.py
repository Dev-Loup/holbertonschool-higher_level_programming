#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        if value > score:
            score = value
    return key
