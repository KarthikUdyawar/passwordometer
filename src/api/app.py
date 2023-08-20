"""This module defines a FastAPI application with a root endpoint
and includes a router for password strength prediction."""

from fastapi import FastAPI

from src.api.routers import router
from src.middleware.logger import logger

APP_DESC = """
The Passwordometer API is a powerful tool designed to enhance password security and empower users with the ability to assess password strength and generate secure passwords. Whether you're a developer integrating password strength prediction into your application or an end user looking for a reliable password generation service, the Passwordometer API has you covered.

## Features

- **Password Strength Prediction:** Get an accurate assessment of the strength of a password, helping you make informed decisions about your password choices.

- **Secure Password Generation:** Generate strong and secure passwords based on customizable criteria, ensuring you have robust passwords that meet your needs.

- **API Integration:** Seamlessly integrate the Passwordometer API into your applications, providing your users with an additional layer of security and peace of mind.

## How It Works

The Passwordometer API utilizes state-of-the-art machine learning techniques to predict password strength based on a variety of features and characteristics. It combines data analysis, feature engineering, and model selection to provide reliable and accurate predictions.

## Getting Started

To get started with the Passwordometer API, follow the instructions provided in the project's [GitHub repository](https://github.com/KarthikUdyawar/Passwordometer). You can set up the API locally or access it remotely.

## API Documentation

Explore the comprehensive API documentation and interactive Swagger interface to understand the available endpoints, request and response structures, and usage examples. You can access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) after starting the local server.

## Docker Image

For easy deployment and scalability, a Docker image of the Passwordometer API is available on Docker Hub. By pulling and running the image, you can quickly set up the API in a containerized environment.

## Contribution and Contact

Contributions to the Passwordometer API are welcome! Whether you're interested in fixing a bug, enhancing existing features, or adding new functionality, your contributions are valuable. Feel free to reach out to the project author, [Karthik Udyawar](mailto:karthikajitudy@gmail.com), for any questions or feedback.

## License

The Passwordometer API is distributed under the [MIT License](https://github.com/KarthikUdyawar/Passwordometer/blob/main/LICENSE). This license allows you to use, modify, and distribute the software, subject to the terms and conditions outlined in the license.
"""

app = FastAPI(
    title="Passwordometer API",
    description=APP_DESC,
    summary="Predict and Generate Password Strength",
    version="1.1.0",
    contact={
        "name": "Karthik Udyawar",
        "url": "https://github.com/KarthikUdyawar",
        "email": "karthikajitudy@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/KarthikUdyawar/Passwordometer/blob/main/LICENSE",
    },
)

app.include_router(router)


@app.get(
    "/", summary="Root endpoint", description="Returns a success message."
)  # type: ignore
def read_root() -> dict[str, str]:
    """
    Get the root endpoint.

    Returns:
        dict: A dictionary containing a success message.
    """
    logger.info("Server running successfully")
    return {"message": "Server running successfully"}
