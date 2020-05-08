#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key:
        concept = {key: value}
        a_dictionary.update(concept)
    return a_dictionary
