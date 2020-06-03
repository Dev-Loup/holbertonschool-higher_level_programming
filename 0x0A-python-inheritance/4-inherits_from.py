#!/usr/bin/python3
""" class Check module
    Functions:
        inherits_from: checks inheritance
"""


def inherits_from(obj, a_class):
    """ Returns booleanType response
        for class inheritance test
        Args:
            obj: object to evaluate
            a_class: class value for testing
    """

    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    else:
        return False
