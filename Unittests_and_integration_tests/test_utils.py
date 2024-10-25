#!/usr/bin/env python3
"""
Unit tests for access_nested_map function.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function."""

    @parameterized.expand([
        ({}, ("a",)),  # Case: Key 'a' not found in an empty dict.
        ({"a": 1}, ("a", "b")),  # Case: Path 'a' exists, but 'b' does not.
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Assert the exception message matches the missing key.
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
