"""This module defines a FastAPI endpoint for predicting the strength of a given
password using a trained machine learning model and a data pipeline."""

import sys

from fastapi import HTTPException

from src.api.schema import (
    PredictionRequest,
    PredictionResponse,
    GenerateRequest,
    GenerateResponse,
)
from src.api.utils import (
    generate_password,
    calc_class_strength,
    calc_entropy,
    calc_strength,
    display_time,
    entropy_to_crack_time,
)

from src.middleware.exception import CustomException
from src.middleware.logger import logger

from src.utils.data_validation import is_valid_password


def password_strength_component(
    request: PredictionRequest,
) -> PredictionResponse:
    """
    Predict the strength of a given password.

    Args:
        request (PredictionRequest): The request containing the password.

    Returns:
        PredictionResponse: The response containing the password ,
        strength prediction and its strength class.

    Raises:
        HTTPException: If the password is invalid or any other custom exception
        occurs.
    """
    try:
        logger.info("Called predict function")

        password = request.password

        if is_valid_password(password) == 0:
            if len(password) < 4:
                logger.error("400 Bad Request: Invalid too short password")
                raise HTTPException(
                    status_code=400,
                    detail="Invalid too short password:"
                    " Length of the password should be greater then 3",
                )
            if len(password) > 64:
                logger.error("400 Bad Request: Invalid password length")
                raise HTTPException(
                    status_code=400,
                    detail="Invalid password length:"
                    " Length of the password should be lesser then 64",
                )
            logger.error("400 Bad Request: Invalid password characters")
            raise HTTPException(
                status_code=400,
                detail="Invalid password characters: "
                "Valid values for passwords include numerals, capital letters"
                ", !, @, #, $, %, ^, &, or *. No other special characters are"
                "allowed.",
            )

        strength = calc_strength(password)
        class_strength = calc_class_strength(strength)
        entropy = calc_entropy(password)
        crack_time = entropy_to_crack_time(entropy)

        logger.info("200 OK: Done predict function")

        return PredictionResponse(
            password=password,
            length=len(password),
            strength=strength,
            class_strength=class_strength,
            entropy=round(entropy, 3),
            crack_time_sec=round(crack_time, 3),
            crack_time=display_time(crack_time),
        )
    except CustomException as error:
        logger.error(error, sys)
        raise HTTPException(status_code=500, detail=error) from error


def generate_strong_password(
    request: GenerateRequest,
) -> GenerateResponse:
    """Generate a strong password using numerals, letters, and specific
    special characters.

    Args:
        request (GenerateRequest): The request containing the length of the
        generated password.

    Returns:
        GenerateResponse: The response containing the generated password.
    """
    try:
        logger.info("Called generate function")

        length = request.length

        if length <= 12:
            logger.error("400 Bad Request: Invalid too short password")
            raise HTTPException(
                status_code=400,
                detail="Invalid too short password:"
                " Length of the password should be greater then 12",
            )
        if length > 64:
            logger.error("400 Bad Request: Invalid password length")
            raise HTTPException(
                status_code=400,
                detail="Invalid password length:"
                " Length of the password should be lesser then 64",
            )

        while True:
            password = generate_password(length)
            strength = calc_strength(password)

            if strength > 0.6:
                class_strength = calc_class_strength(strength)
                entropy = calc_entropy(password)
                crack_time = entropy_to_crack_time(entropy)

                logger.info("200 OK: Done generate function")

                return GenerateResponse(
                    password=password,
                    length=length,
                    strength=strength,
                    class_strength=class_strength,
                    entropy=round(entropy, 3),
                    crack_time_sec=round(crack_time, 3),
                    crack_time=display_time(crack_time),
                )
    except CustomException as error:
        logger.error(error, sys)
        raise HTTPException(status_code=500, detail=error) from error
