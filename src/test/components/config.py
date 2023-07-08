"""
Module: config

This module contains mock configuration classes for file paths
and MongoDB settings, used for testing purposes.

Classes:
- MockMongoDBConfig: Mock configuration class for MongoDB.
- MockFilePathConfig: Mock configuration class for file paths.

"""
import os
from dataclasses import dataclass

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
    test_data_path: str = os.path.join("src/test/data", "test.csv")
    preprocessor_path: str = os.path.join("src/test/data", "preprocessor.pkl")
