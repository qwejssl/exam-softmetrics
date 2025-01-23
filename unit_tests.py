"""
Unit tests for the `absolute` function from the `absolute` module.
It covers all input checks and edge cases.
"""

import math
import unittest

from absolute import absolute


class TestAbsoluteFunction(unittest.TestCase):
    """
    Thorough test suite for the 'absolute' function from 'absolute.py'.
    """

    def test_positive_value(self):
        """Test standard positive integers."""
        self.assertEqual(absolute(10), 10)

    def test_negative_value(self):
        """Test negative inputs yield their positive equivalent."""
        self.assertEqual(absolute(-10), 10)

    def test_zero_value(self):
        """Test zero input results in 0.0."""
        self.assertEqual(absolute(0), 0.0)

    def test_float_value(self):
        """Test floating-point inputs."""
        self.assertAlmostEqual(absolute(-10.5), 10.5)

    def test_none_input(self):
        """Test that None input raises ValueError."""
        with self.assertRaises(ValueError):
            absolute(None)

    def test_nan_input(self):
        """Test that NaN input raises ValueError."""
        with self.assertRaises(ValueError):
            absolute(math.nan)

    def test_infinite_input(self):
        """Test that infinite input raises ValueError."""
        with self.assertRaises(ValueError):
            absolute(math.inf)
        with self.assertRaises(ValueError):
            absolute(-math.inf)

    def test_non_numeric_input(self):
        """Test that non-numeric values raise TypeError."""
        with self.assertRaises(TypeError):
            absolute("ten")
        with self.assertRaises(TypeError):
            absolute([10])
        with self.assertRaises(TypeError):
            absolute({"value": 10})


if __name__ == '__main__':  # pragma: no cover
    unittest.main()          # pragma: no cover