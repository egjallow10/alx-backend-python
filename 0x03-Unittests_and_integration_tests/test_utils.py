#!/usr/bin/env python3
""" This function allows you to access nested dictionaries
(a data structure where one dictionary is inside another dictionary)
by passing a path of keys that lead to the value you want to retrieve"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ A class test  that inherit"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """to this function, and it will return the value"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
