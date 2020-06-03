#!/usr/bin/python3
""" Class declaration module
    classes:
        BaseGeometry: geometry class
"""


class BaseGeometry():
    """ Class Base Geometry
        Methods:
            area(): not implement, raise Error
            integer_validator
    """

    def area(self):
        """ function not implemented
            Raises:
                Exception: area() is not implemented

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Check if value is absolute
            Args:
                name: int name
                value: int to evaluate
            Raises:
                TypeError: <name> must be an integer
                ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
