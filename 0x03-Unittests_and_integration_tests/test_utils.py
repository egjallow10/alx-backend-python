#!/usr/bin/env python3
""" This function allows you to access nested dictionaries
(a data structure where one dictionary is inside another dictionary)
by passing a path of keys that lead to the value you want to retrieve"""


import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


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

    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ['a', 'b'])
    ])
    def test_access_nested_map_exception(self, nested_map, expected_result):
        """Exptional Error"""
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """mock an api reques"""

    @parameterized.expand([
        ("http://example.com", {"payload": True})
        ("http://holberton.io", {"payload": False})
    ])
    # @mock.patch("request.get")
    def test_get_json(self, test_url, test_payload):
        """"""
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
