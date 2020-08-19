#!/usr/bin/python3
""" Find_peak module
    Find the peak in a list
"""


def find_peak(list_int):
    """ find_peak function
        Args:
            list_int: random list for getting peak
        Return:
            the peak
    """

    if len(list_int) == 0:
        return None
    peak = 0
    check_2 = None
    cut_1 = list_int[(len(list_int) // 2):]
    cut_2 = list_int[:(len(list_int) // 2)]
    if sum(cut_1) // len(cut_1) > sum(cut_2) // len(cut_2):
        check_1 = cut_1
    elif sum(cut_1) // len(cut_1) == sum(cut_2) // len(cut_2):
        check_1 = cut_1
        check_2 = cut_2
    else:
        check_1 = cut_2
    for num in check_1:
        if num > peak:
            peak = num
    if check_2 is not None:
        for num_1 in check_2:
            if num_1 > peak:
                peak = num_1
    return peak
