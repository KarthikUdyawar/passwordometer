"""This module defines a FastAPI router for predicting password strength based 
on a given password."""

from fastapi import APIRouter

from src.api.components import password_strength_component
from src.api.schema import PredictionRequest, PredictionResponse

router = APIRouter()


@router.post(
    "/predict",
    summary="Predict password strength",
    description="Predict the strength of a given password.",
)  # type: ignore
async def password_strength(
    request: PredictionRequest,
) -> PredictionResponse:
    """
    Predict the strength of a given password.

    Args:
        request (PasswordPredictionRequest): The request containing the password.

    Returns:
        PasswordPredictionResponse: The response containing the password and 
        its strength prediction.
    """
    return password_strength_component(request)
