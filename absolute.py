"""
This module provides a function to calculate the absolute value using math.fabs.
It includes input checks for None, non-numeric, NaN, and infinite values.
"""

import math


def absolute(value):
    """
    Calculate the absolute value of a number using math.fabs, with
    thorough validation of the input.

    :param value: The number for which the absolute value is to be calculated.
    :type value: int or float
    :raises ValueError: If the value is None, NaN, or infinite.
    :raises TypeError: If the value is not an int or float.
    :return: The absolute value as a float.
    :rtype: float
    """

    # Check for None
    if value is None:
        raise ValueError("Argument 'value' cannot be None.")

    # Check type
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"Argument 'value' must be int or float, got {type(value).__name__}."
        )

    # Check NaN
    if math.isnan(value):
        raise ValueError("Argument 'value' cannot be NaN.")

    # Check infinite
    if not math.isfinite(value):
        raise ValueError("Argument 'value' cannot be infinite.")

    return math.fabs(value)