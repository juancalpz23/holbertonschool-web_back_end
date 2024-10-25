#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function from the utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """
    Test get_json function with mock HTTP calls.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns expected result and that requests.get
        was called with the correct URL.
        """
        # Create a Mock response object with a .json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test URL
        result = get_json(test_url)

        # Assert that requests.get was called once with the test URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result from get_json matches the expected payload
        self.assertEqual(result, test_payload)


class TestClass:
    """Class with a memoized property for testing purposes."""

    def a_method(self):
        """Method that returns a fixed value."""
        return 42

    @memoize
    def a_property(self):
        """Memoized property that calls a_method."""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test the memoization functionality of
    the memoize decorator."""

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """Test that a_method is called only once,
        even with multiple accesses."""
        test_obj = TestClass()

        # Access the memoized property twice
        first_call = test_obj.a_property
        second_call = test_obj.a_property

        # Assert that the result is correct
        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)

        # Assert that a_method was only called once
        mock_a_method.assert_called_once()
