#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    counter = 0
    copy_list = my_list.copy()

    for int in copy_list:
        if counter > idx:
            return copy_list
        if counter == idx:
            copy_list[idx] = element
            return copy_list
        counter += 1
    return copy_list
