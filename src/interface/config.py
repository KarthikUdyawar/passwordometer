import os
import sys
from dataclasses import dataclass

import pandas as pd

from src.middleware.exception import CustomException


@dataclass
class FilePathConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("raw_dataset", "rockyou.txt")
    preprocessor_path: str = os.path.join("artifacts", "preprocessor.pkl")
    model_path: str = os.path.join("artifacts", "model.pkl")


@dataclass
class MongoDBConfig:
    mongodb_connection_string: str = "mongodb://localhost:27017/"
    database_name: str = "passwordometer"
    collection_name: str = "password_dataset"
