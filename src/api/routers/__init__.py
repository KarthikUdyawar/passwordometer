"""This module defines a FastAPI router for predicting password strength based
on a given password."""

from fastapi import APIRouter

from src.api.components import (
    password_strength_component,
    generate_strong_password,
)
from src.api.schema import (
    PredictionRequest,
    PredictionResponse,
    GenerateRequest,
    GenerateResponse,
)

router = APIRouter()


@router.post(
    "/predict",
    summary="Predict password strength",
    description="Predict the strength of a given password.",
    tags=["API"],
    response_model=PredictionResponse,
)  # type: ignore
async def password_strength(
    request: PredictionRequest,
) -> PredictionResponse:
    """
    Predict the strength of a given password.

    Args:
        request (PredictionRequest): The request containing the password.

    Returns:
        PredictionResponse: The response containing the password and
        its strength prediction and other parameters.
    """
    return password_strength_component(request)


@router.post(
    "/generate",
    summary="Generate password",
    description="Generate strong password of a given length.",
    tags=["API"],
    response_model=GenerateResponse,
)  # type: ignore
async def generate_password(
    request: GenerateRequest,
) -> GenerateResponse:
    """
    Generate strong password of a given length.

    Args:
        request (GenerateRequest): The request containing the length.

    Returns:
        GenerateResponse: The response containing the password and
        its strength prediction and other parameters.
    """
    return generate_strong_password(request)
