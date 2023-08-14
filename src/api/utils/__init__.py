"""Utility module for password strength calculation and related calculations."""
import math
import secrets
from src.interface.config import CustomData
from src.pipe.pipeline import Pipeline

CHARS_SET = (
    "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*"
)
CRACK_PASSWORD_PER_SECOND = 1000000000
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_MONTH = 30 * 24 * 60 * 60
SECONDS_IN_YEAR = 365 * 24 * 60 * 60
SECONDS_IN_CENTURY = 100 * 365 * 24 * 60 * 60


def generate_password(length: int) -> str:
    """Generate a random password of a given length.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password.
    """
    return "".join(secrets.choice(CHARS_SET) for _ in range(length))


def calc_strength(password: str) -> float:
    """Calculate the strength of a given password.

    Args:
        password (str): The password to calculate the strength for.

    Returns:
        float: The calculated strength of the password.
    """
    custom_data = CustomData()
    pipeline = Pipeline()
    password_df = custom_data.data2df(password)
    strength = pipeline.predict(password_df)
    return custom_data.array2data(strength)


def calc_class_strength(value: float) -> str:
    """Calculate the class strength based on a strength value.

    Args:
        value (float): The strength value.

    Returns:
        str: The class strength category.
    """
    return (
        "Very week"
        if value <= 0.2
        else "Week"
        if value <= 0.4
        else "Average"
        if value <= 0.6
        else "Strong"
        if value <= 0.8
        else "Very strong"
    )


def calc_entropy(password: str) -> float:
    """Calculate the entropy of a given password.

    Args:
        password (str): The password to calculate entropy for.

    Returns:
        float: The calculated entropy.
    """
    cardinality = calc_cardinality(password)
    length = len(password)
    sample_space = (cardinality) ** (length)
    return math.log(sample_space, 2)


def calc_cardinality(password: str) -> int:
    """Calculate the cardinality of a password.

    Args:
        password (str): The password to calculate cardinality for.

    Returns:
        int: The calculated cardinality.
    """
    lower, upper, digits, symbols = 0, 0, 0, 0
    for char in password:
        if char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isupper():
            upper += 1
        else:
            symbols += 1
    return lower + digits + upper + symbols


def entropy_to_crack_time(entropy: float) -> float:
    """Convert entropy to estimated crack time.

    Args:
        entropy (float): The entropy value.

    Returns:
        float: The estimated crack time in seconds.
    """
    return (0.5 * math.pow(2, entropy)) / CRACK_PASSWORD_PER_SECOND


def display_time(seconds: float) -> str:
    """ "Convert seconds to a human-readable time representation.

    Args:
        seconds (float): The time in seconds.

    Returns:
        str: The human-readable time representation.
    """
    time_string = "instant"
    if seconds >= 1 and seconds < SECONDS_IN_MINUTE:
        time_string = f"{seconds} seconds"
    if seconds < SECONDS_IN_HOUR:
        time_string = (
            f"{str(1 + math.ceil(seconds / SECONDS_IN_MINUTE))} minutes"
        )
    if seconds < SECONDS_IN_DAY:
        time_string = f"{str(1 + math.ceil(seconds / SECONDS_IN_HOUR))} hours"
    if seconds < SECONDS_IN_MONTH:
        time_string = f"{str(1 + math.ceil(seconds / SECONDS_IN_DAY))} days"
    if seconds < SECONDS_IN_YEAR:
        time_string = (
            f"{str(1 + math.ceil(seconds / SECONDS_IN_MONTH))} months"
        )
    if seconds < SECONDS_IN_CENTURY:
        time_string = f"{str(1 + math.ceil(seconds / SECONDS_IN_YEAR))} years"
    else:
        time_string = (
            f"{str(1 + math.ceil(seconds / SECONDS_IN_CENTURY))} centuries"
        )
    return time_string
