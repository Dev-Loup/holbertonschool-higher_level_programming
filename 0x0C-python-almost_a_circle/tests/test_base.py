#!/usr/bin/python3
"""
    models/base.py unittest module.
    Subclasses:
      TestBaseClass: unittest Class
"""
import unittest
max_integer = __import__('models/base.py').Base


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

        self.assertEqual(max_integer([1, 5, 7]), 7)
