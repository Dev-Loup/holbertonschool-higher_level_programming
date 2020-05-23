#!/usr/bin/python3
"""
  4-print_square module.
  Print squares
  Functions:
    print_square(size)
"""


def print_square(size):
    """
        print a compose '#' square.
        Args:
          size: size of the square
        Raises:
          TypeError: size must be an integer
          ValueError:size must be >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for Y in range(size):
        print("#" * size)
