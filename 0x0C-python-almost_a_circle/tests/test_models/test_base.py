#!/usr/bin/python3
"""
    models.base unittest module.
    Subclasses:
      TestBaseClass: unittest Class
"""
import unittest
Base = __import__('models.base').Base


class TestBase(unittest.TestCase):
    """verify multiple conditions
       for checking max_integer results
       function:
        valid_max(self)
        raise_error(self)
    """

    def test_valid_max(self):
        """test_arguments.
           Args:
             Self: Subclass argument
        """
        pass
