#!/usr/bin/python3
""" Module for MyInt class inheritage from int
    Classes:
        MyInt: Int child
"""


class MyInt(int):
    """ Class MyInt rebellous
        Inverts boolean response for equal
        or different
        Return:
            inverse result
    """

    def __init__(self, value):
        """method instantiation
        """

        self.value = value

    def __eq__(self, randomvalue):
        """ Inverse equal values
        """

        return self.value != randomvalue

    def __ne__(self, randomvalue):
        """ Inverse different values
        """
        return self.value == randomvalue
