#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function from the utils module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map with various nested dictionaries and paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        # Assert the exception message matches the missing key.
        self.assertEqual(str(context.exception), f"'{path[-1]}'")
