#!/usr/bin/python3
"""
  3-say_my_name module.
  Print the name given in arguments
  Functions:
    say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name prints arguments as
        person introduction.
        Args:
          first_name: the main name
          last_name: optional last name
        Raises:
          TypeError: first_name must be a string
          TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", end="")
    if first_name:
        print(" " + first_name + " ", end="")
    if last_name:
        if first_name == "":
            print(" ", end="")
        print(last_name, end="")
    print()
