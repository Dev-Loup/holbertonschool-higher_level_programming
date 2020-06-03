#!/usr/bin/python3
""" Class Inheritance module
    Class:
        MyList: List's child (inherits from list)
"""


class MyList(list):
    """ My list class.
        inherits methods and attributes from list
        Public instance methods:
        print_sorted: prints the mylist object content
    """
    def print_sorted(self):
        """ method for printing mylists
        """
        print(sorted(self))
