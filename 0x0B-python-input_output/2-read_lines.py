#!/usr/bin/python3
""" Printing files module
    Functions:
        read_lines: Read n lines of a file and
        print it
"""


def read_lines(filename="", nb_lines=0):
    """ Write the file in a list of lines and print
        the nb_lines lines
        filename: string containing the name or "" if
        not given.
        nb_lines:
            number of lines to print
    """

    with open(filename, encoding="utf-8") as fl_opened:
        fl_list_lines = fl_opened.readlines()
        if nb_lines <= 0 or nb_lines >= len(fl_list_lines):
            nb_lines = len(fl_list_lines)
        for idx in range(nb_lines):
            if fl_list_lines[idx]:
                print("{}".format(fl_list_lines[idx]))
            else:
                break
