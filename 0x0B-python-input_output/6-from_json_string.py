#!/usr/bin/python3
""" Json conversion module
    functions:
        from_json_string: converts json to string
"""

import json


def from_json_string(my_str):
    """ Converts to string
        return: json loaded to object
    """

    return json.loads(my_str)
