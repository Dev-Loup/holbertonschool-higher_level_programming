#!/usr/bin/python3
""" load json to object module
    Functions:
        load_from_json: open and return a read json
"""

import json


def load_from_json_file(filename):
    """ Returns a read json
        Args:
            filename: json file
    """

    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
