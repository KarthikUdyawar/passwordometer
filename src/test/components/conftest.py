"""
Module: test_fixtures

This module contains test fixtures for the unit tests of the data ingestion
and data pusher components.

Fixtures:
- data_pusher_fixture: Fixture for creating a DataPusher instance with
mock configurations.
- data_ingestion_fixture: Fixture to create a DataIngestion object
before each test.

"""
import pytest

from src.components.data_ingestion import DataIngestion
from src.components.data_pusher import DataPusher
from src.test.components.config import MockFilePathConfig, MockMongoDBConfig


@pytest.fixture(scope="session", name="data_pusher")  # type: ignore
def data_pusher_fixture() -> DataPusher:
    """Fixture for creating a DataPusher instance with mock configurations.

    Returns:
        DataPusher: The DataPusher instance.
    """
    data_pusher = DataPusher()
    data_pusher.mongodb_config = MockMongoDBConfig()
    data_pusher.filepath_config = MockFilePathConfig()

    return data_pusher


@pytest.fixture(scope="session", name="data_ingestion")  # type: ignore
def data_ingestion_fixture(data_pusher: DataPusher) -> DataIngestion:
    """
    Fixture to create a DataIngestion object before each test.

    Returns:
        DataIngestion: An instance of the DataIngestion class.
    """
    data_ingestion = DataIngestion()
    data_ingestion.dataframe = data_pusher.get_data_from_mongodb()
    return data_ingestion
