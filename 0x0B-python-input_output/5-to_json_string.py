#!/usr/bin/python3
""" Json conversion module
    functions:
        to_json_string: converts string to json
"""

import json


def to_json_string(my_obj):
    """ Converts to json
        return: object dumped to json
    """

    return json.dumps(my_obj)
