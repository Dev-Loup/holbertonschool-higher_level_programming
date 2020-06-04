#!/usr/bin/python3
""" Saves to json module
    Functions:
        save_to_json: store a json into a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ converts and saves the json
        Args:
            my_obj: the string to dump
            filename: where to save
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
