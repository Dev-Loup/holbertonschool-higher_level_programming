#!/usr/bin/python3
""" Square module
    Creates Squares from Squares
    Classes:
        Square: set Square parameters
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square
        Priv instance attributes:
            super init attributes from Rectangle
        Public methods:
            size: set the super class width and height
            update: updates a class with given args or kwargs
            to_dictionary: returns a kwargs dictionary
    """
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
                                        self.x,
                                        self.y,
                                        self.width)

    @property
    def size(self):
        """ Get size attribute
        """

        return self.width

    @size.setter
    def size(self, size):
        """ set the size attribute
        """

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update a class square with
            args o kwargs
            Args:
                *args: no keyworded args
                **kwargs: keyworded args
        """

        setter = ['id',
                  'size',
                  'x',
                  'y']
        if args:
            for counter, arg in enumerate(args):
                setattr(self, setter[counter], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary of
            the class
            Return:
                kwargs dictionary
        """

        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
