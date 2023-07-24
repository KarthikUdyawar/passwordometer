"""
Module for password data validation.
"""
import sys

from src.middleware.exception import CustomException


def is_valid_password(text: str) -> int:
    """The is_valid_password function checks whether a given password meets
    certain criteria and returns an integer value indicating its validity.

    Args:
    ---
        text (str): The password to be validated.

    Returns:
    ---
        int: An integer value representing the validity of the password.
        It returns 1 if the password is valid, and 0 if it is not.
    """
    try:
        if len(text) < 4 or len(text) > 64:
            return 0

        text_set = set(text.lower())
        valid_set = set("qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*")

        return 0 if text_set.difference(valid_set) else 1
    except Exception as error:
        raise CustomException(error, sys) from error
