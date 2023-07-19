"""This module defines a FastAPI application with a root endpoint and includes a router for password strength prediction."""

from fastapi import FastAPI
from src.api.routers import router
from src.middleware.logger import logger


app = FastAPI()

app.include_router(router)


@app.get("/", summary="Root endpoint", description="Returns a success message.")
def read_root() -> dict[str, str]:
    """
    Get the root endpoint.

    Returns:
        dict: A dictionary containing a success message.
    """
    logger.info("Server running successfully")
    return {"message": "Server running successfully"}
