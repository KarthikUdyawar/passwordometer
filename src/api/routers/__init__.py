"""This module defines a FastAPI router for predicting password strength based on a given password."""

from fastapi import APIRouter
from src.api.components import predict_component
from src.api.schema import PasswordPredictionRequest, PasswordPredictionResponse

router = APIRouter()


@router.post(
    "/predict",
    summary="Predict password strength",
    description="Predict the strength of a given password.",
)
async def predict(request: PasswordPredictionRequest) -> PasswordPredictionResponse:
    """
    Predict the strength of a given password.

    Args:
        request (PasswordPredictionRequest): The request containing the password.

    Returns:
        PasswordPredictionResponse: The response containing the password and its strength prediction.
    """
    return predict_component(request)
