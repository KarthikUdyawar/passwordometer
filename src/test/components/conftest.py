"""
This module contains test fixtures for the unit tests of the data ingestion
and data pusher components.
"""
import pytest

from src.components.data_ingestion import DataIngestion
from src.components.data_pusher import DataPusher
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# from src.test.components.config import MockFilePathConfig, MockMongoDBConfig


@pytest.fixture(scope="session", name="data_pusher")  # type: ignore
def data_pusher_fixture() -> DataPusher:
    """Fixture for creating a DataPusher instance with mock configurations.

    Returns:
        DataPusher: The DataPusher instance.
    """
    data_pusher = DataPusher()
    data_pusher.sample_size = 500
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


@pytest.fixture(scope="session", name="data_transformation")  # type: ignore
def data_transformation_fixture() -> DataTransformation:
    """Fixture to create a DataTransformation object before each test.

    Returns:
        DataTransformation: An instance of the DataTransformation class.
    """
    return DataTransformation()


@pytest.fixture(scope="session", name="model_trainer")  # type: ignore
def model_trainer_fixture() -> ModelTrainer:
    """Fixture to create a ModelTrainer object before each test.

    Returns:
        ModelTrainer: An instance of the ModelTrainer class.
    """
    return ModelTrainer()
