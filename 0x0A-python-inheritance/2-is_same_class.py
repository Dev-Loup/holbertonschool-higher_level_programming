#!/usr/bin/python3
""" Class check module
    Functions:
        is_same_class: checks if object is from some class.
"""


def is_same_class(obj, a_class):
    """ checks an object class and returns if it belongs to
        Args:
            obj: object to evaluate
            a_class: class name
        Return:
            booleanType value
    """

    return type(obj) == a_class
