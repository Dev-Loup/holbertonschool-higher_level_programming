#!/usr/bin/python3
""" Printing files module
    Functions:
        number_of_lines: get the number of lines and
        return it
"""


def number_of_lines(filename=""):
    """ Write the file in a list of lines and return the len
        filename: string containing the name or "" if
        not given.
        Return:
            lines of the file
    """

    with open(filename, encoding="utf-8") as fl_opened:
        fl_list_lines = fl_opened.readlines()
        count = len(fl_list_lines)
        return count
