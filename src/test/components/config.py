"""
This module contains mock configuration classes for file paths
and MongoDB settings, used for testing purposes.
"""
from dataclasses import dataclass

from src.interface.config import MongoDBConfig


# Mock the necessary dependencies
@dataclass
class MockMongoDBConfig(MongoDBConfig):
    """Mock configuration class for MongoDB."""

    mongodb_connection_string: str = "mongodb://localhost:27017/"
    database_name: str = "passwordometer"
    collection_name: str = "sample"
