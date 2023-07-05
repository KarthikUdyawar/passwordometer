import os
from dataclasses import dataclass

# import pandas as pd
# import pytest

# from src.components.data_ingestion import DataIngestion
# from src.components.data_pusher import DataPusher
from src.interface.config import FilePathConfig, MongoDBConfig

# Mock the necessary dependencies
@dataclass
class MockMongoDBConfig(MongoDBConfig):
    """Mock configuration class for MongoDB."""

    mongodb_connection_string: str = "mongodb://localhost:27017/"
    database_name: str = "passwordometer"
    collection_name: str = "sample"


@dataclass
class MockFilePathConfig(FilePathConfig):
    """Mock configuration class for file paths."""

    raw_data_path: str = os.path.join("src/test/data", "sample.txt")
    train_data_path: str = os.path.join("src/test/data", "train.csv")