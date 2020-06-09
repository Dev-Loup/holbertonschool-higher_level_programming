#!/usr/bin/python3
""" Square module
    Creates Squares from Squares
    Classes:
        Square: set Square parameters
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ Square instantiation
            super init Rectangle:
                (width, height, x, y, id)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print default definition
            Return: predefined string
        """

        return "[Square]"\
               "({}) {}/{} - {}".format(self.id,
                                        self.set_x,
                                        self.set_y,
                                        self.set_width)

    @property
    def size(self):
        """ Get size attribute
        """

        return self.set_width

    @size.setter
    def size(self, size):
        """ set the size attribute
        """

        self.set_width = size
        self.set_height = size

    def update(self, *args, **kwargs):
        setter = ['id',
                  'size',
                  'set_x',
                  'set_y']
        if args:
            for counter, arg in enumerate(args):
                setattr(self, setter[counter], arg)
        else:
            for key, value in kwargs.items():
                if key != 'id' and key != 'size':
                    attr_key = "set_" + key
                else:
                    attr_key = key
                setattr(self, attr_key, value)

    def to_dictionary(self):
        """ Returns a dictionary of
            the class
        """

        return {'id': self.id,
                'size': self.size,
                'x': self.set_x,
                'y': self.set_y}
