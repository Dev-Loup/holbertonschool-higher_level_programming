#!/usr/bin/python3
""" Class check module
    Functions:
        is_kind_of_class: checks if obj is inherit
        from determined class
"""


def is_kind_of_class(obj, a_class):
    """ checks class inheritance
        Args:
            obj: object to evaluate
            a_class: suspect father
    """

    return isinstance(obj, a_class)
