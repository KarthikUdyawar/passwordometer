"""Generates kaggle.json file"""
import json
import os

from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

# Generate kaggle.json
kaggle_credentials = {
    "username": config["KAGGLE_USERNAME"],
    "key": config["KAGGLE_KEY"],
}

# Save the credentials as kaggle.json
with open("kaggle.json", "w", encoding="utf-8") as file:
    json.dump(kaggle_credentials, file)
