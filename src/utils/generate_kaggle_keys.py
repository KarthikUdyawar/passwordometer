"""Generates kaggle.json file"""
import json
from dotenv import dotenv_values

# Load secrets from .env file
secrets = dotenv_values(".env")

# Generate kaggle.json
kaggle_credentials = {
    "username": secrets["KAGGLE_USERNAME"],
    "key": secrets["KAGGLE_KEY"],
}

# Save the credentials as kaggle.json
with open("kaggle.json", "w") as file:
    json.dump(kaggle_credentials, file)
