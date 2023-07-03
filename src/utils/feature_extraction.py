"""
Module for password strength calculation.

This module provides a function for calculating the strength of a password
based on certain criteria.
"""
from password_strength import PasswordStats


def calculate_strength(text: str) -> float:
    """
    Calculate the strength of a password.

    Args:
        text (str): The password for which the strength will be calculated.

    Returns:
        float: The strength value of the password.
    """
    return float(PasswordStats(text).strength())
