#!/usr/bin/python3
"""
  0-add_integer module
  Contains add integer function.
  Functions:
    add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
      Adds two integers or floats,
      with one number it adds 98 to number.

      Args:
        a: float or integer
        b: float or integer, 98 if argument is not given
      Raises:
        TypeError: foo must be an integer
      Return:
        Addition type int
    """

    if type(a) not in {int, float} or a != a:
        raise TypeError("a must be an integer")
    if type(b) not in {int, float} or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
