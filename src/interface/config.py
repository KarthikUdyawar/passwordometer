"""
Module for configuration classes related to file paths and MongoDB settings.
"""
import os
import sys
from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd
from dotenv import dotenv_values

from src.middleware.exception import CustomException

config = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}


class CustomData:
    """A class for handling custom data."""

    def data2df(self, password: str) -> pd.DataFrame:
        """Convert the given password into a pandas DataFrame.

        Args:
            password (str): The password to be converted.

        Raises:
            CustomException: If there is an error during the conversion.

        Returns:
            pd.DataFrame: The password converted into a pandas DataFrame.
        """
        try:
            input_data = {
                "password": [password],
            }

            return pd.DataFrame(input_data)

        except Exception as error:
            raise CustomException(error, sys) from error

    def array2data(self, arr: np.ndarray[np.float64, Any]) -> Any:
        """Convert the given NumPy array to a single value.

        Args:
            arr (np.ndarray): The NumPy array to be converted.

        Returns:
            float: The converted value.
        """
        try:
            return arr.item()

        except Exception as error:
            raise CustomException(error, sys) from error


@dataclass
class FilePathConfig:
    """Configuration class for file paths."""

    database_url: str = "https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt"
    raw_data_path: str = os.path.join(
        "common-password-list-rockyoutxt", "rockyou.txt"
    )
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    preprocessor_path: str = os.path.join("artifacts", "preprocessor.pkl")
    model_path: str = os.path.join("artifacts", "model.pkl")


@dataclass
class MongoDBConfig:
    """Configuration class for MongoDB."""

    mongodb_connection_string: str = config["MONGODB_CONN_STRING"]
    database_name: str = "passwordometer"
    collection_name: str = "password_dataset"
