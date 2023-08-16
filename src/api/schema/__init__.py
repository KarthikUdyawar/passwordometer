"""This module defines classes for password strength prediction and generation
requests and responses using Pydantic models."""
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):  # type: ignore
    """A request model for password strength prediction.

    Args:
        BaseModel (type): The Pydantic BaseModel class.
    """

    password: str = Field(
        ..., description="The password to predict its strength"
    )


class PredictionResponse(BaseModel):  # type: ignore
    """A response model for password strength prediction.

    Args:
        BaseModel (type): The Pydantic BaseModel class.
    """

    password: str = Field(..., description="The input password")
    length: int = Field(..., description="The length of password")
    strength: float = Field(
        ..., description="The strength prediction of the password"
    )
    class_strength: str = Field(
        ..., description="The class strength prediction of the password"
    )
    entropy: float = Field(
        ..., description="The measurement of how unpredictable is the password"
    )
    crack_time_sec: float = Field(
        ..., description="The time taken to crack the password in sec"
    )
    crack_time: str = Field(
        ..., description="The time taken to crack the password"
    )


class GenerateRequest(BaseModel):  # type: ignore
    """A request model for password generation.

    Args:
        BaseModel (type): The Pydantic BaseModel class.
    """

    length: int = Field(..., description="The length of password")


class GenerateResponse(BaseModel):  # type: ignore
    """A response model for password generation.

    Args:
        BaseModel (type): The Pydantic BaseModel class.
    """

    password: str = Field(..., description="The generated password")
    length: int = Field(..., description="The length of password")
    strength: float = Field(
        ..., description="The strength prediction of the password"
    )
    class_strength: str = Field(
        ..., description="The class strength prediction of the password"
    )
    entropy: float = Field(
        ..., description="The measurement of how unpredictable is the password"
    )
    crack_time_sec: float = Field(
        ..., description="The time taken to crack the password in sec"
    )
    crack_time: str = Field(
        ..., description="The time taken to crack the password"
    )
