#!/usr/bin/python3
"""
    6-max_integer_test unittest module.
    Subclasses:
      TestMaxInteger: unittest verification
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """verify multiple conditions
       for checking max_integer results
       function:
        valid_max(self)
        raise_error(self)
    """

    def valid_max(self):
        """test_arguments.
           Args:
             Self: Subclass argument
        """

        self.assertEqual(max_integer([1, 5, 7]), 7)
        self.assertEqual(max_integer([1, 7]), 7)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([1, 7, 5, 7]), 7)
        self.assertEqual(max_integer([1, 5, -7]), 5)
        self.assertEqual(max_integer([-1, -5, -7]), -1)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([0, 0.1]), 0.1)
        self.assertEqual(max_integer([0, -0.1]), 0)
        self.assertEqual(max_integer([]), None)

    def raise_error(self):
        """check error being raised.
           Args:
             Self: subclass argument
        """

        self.assertRaises(TypeError, max_integer, [1, 2, 'tres'])
        self.assertRaises(TypeError, max_integer, [1, 2, []])
        self.assertRaises(TypeError, max_integer, [1, 2, {}])
        self.assertRaises(TypeError, max_integer, [1, 2, set()])
        self.assertRaises(TypeError, max_integer, [1, 2, ()])
        self.assertRaises(TypeError, max_integer, 12)
        self.assertRaises(TypeError, max_integer, 'hello')
        self.assertRaises(TypeError, max_integer, ())
        self.assertRaises(TypeError, max_integer, {})
        self.assertRaises(TypeError, max_integer, set())
        self.assertRaises(TypeError, max_integer, [1, [1, 2]])
