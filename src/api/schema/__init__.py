"""This module defines classes for password strength prediction requests and responses using Pydantic models."""

from pydantic import BaseModel, Field


class PasswordPredictionRequest(BaseModel):
    """A request model for password strength prediction.

    Args:
        BaseModel (type): The Pydantic BaseModel class.
    """
    password: str = Field(
        ..., description="The password to predict its strength"
    )


class PasswordPredictionResponse(BaseModel):
    """A response model for password strength prediction.

    Args:
        BaseModel (type): The Pydantic BaseModel class.
    """
    password: str = Field(..., description="The input password")
    strength: float = Field(
        ..., description="The strength prediction of the password"
    )
