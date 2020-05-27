#!/usr/bin/python3
"""Locked Class doesn't allow more
   Attributes
"""


class LockedClass:
    """empty locked class
        LockedClass:
            First_name
    """
    __slots__ = "first_name"
