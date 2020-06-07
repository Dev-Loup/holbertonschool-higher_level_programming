#!/usr/bin/python3
""" SuperClass module
    Creates the geometric base
    Classes:
        Base: set Base geometry parameters
"""


class Base():
    """ Set geometry Base parameters
        Priv Class Attributes:
            __nb_objects: number of objects
        Pub instance attributes:
            id: instance identification
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def set_id(self):
        return self.id

    @set_id.setter
    def set_id(self, id):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
