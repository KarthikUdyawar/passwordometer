"""
Module for configuration classes related to file paths and MongoDB settings.
"""
import os
from dataclasses import dataclass


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

    mongodb_connection_string: str = "mongodb://localhost:27017/"
    database_name: str = "passwordometer"
    collection_name: str = "password_dataset"
