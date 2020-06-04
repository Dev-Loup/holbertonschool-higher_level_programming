#!/usr/bin/python3
""" Add item to file module
    Convert arguments to list then put into json file
"""

from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

arg_list = []
if path.isfile(filename):
    arg_list = load_from_json_file(filename)

for argument in argv[1:]:
    arg_list.append(argument)

save_to_json_file(arg_list, "add_item.json")
