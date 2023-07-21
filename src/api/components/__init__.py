"""This module defines a FastAPI endpoint for predicting the strength of a given
password using a trained machine learning model and a data pipeline."""

import sys

from fastapi import HTTPException

from src.api.schema import PredictionRequest, PredictionResponse
from src.interface.config import CustomData
from src.middleware.exception import CustomException
from src.middleware.logger import logger
from src.pipe.pipeline import Pipeline
from src.utils.data_validation import is_valid_password


def password_strength_component(
    request: PredictionRequest,
) -> PredictionResponse:
    """
    Predict the strength of a given password.

    Args:
        request (PredictionRequest): The request containing the password.

    Returns:
        PredictionResponse: The response containing the password and its 
        strength prediction.

    Raises:
        HTTPException: If the password is invalid or any other custom exception 
        occurs.
    """
    try:
        logger.info("Called predict function")
        custom_data = CustomData()
        pipeline = Pipeline()
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

        password_df = custom_data.data2df(password)
        strength = pipeline.predict(password_df)
        value = custom_data.array2data(strength)

        class_strength = (
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

        logger.info("200 OK: Done predict function")
        return PredictionResponse(
            password=password, strength=value, class_strength=class_strength
        )
    except CustomException as error:
        logger.error(error, sys)
        raise HTTPException(status_code=500, detail=error) from error
