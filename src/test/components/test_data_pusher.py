"""
Test module for the DataPusher component.
"""
import os
from dataclasses import dataclass

import pandas as pd
import pytest
from src.components.data_pusher import DataPusher
from src.interface.config import FilePathConfig
from src.interface.config import MongoDBConfig


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

    raw_data_path: str = os.path.join("raw_dataset", "sample.txt")


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


def test_initiate_data_push(data_pusher: DataPusher) -> None:
    """Test case for initiating the data push.

    Args:
        data_pusher (DataPusher): The DataPusher instance.
    """
    data_pusher.initiate_data_push()


def test_get_data_from_mongodb(data_pusher: DataPusher) -> None:
    """Test case for getting data from MongoDB.

    Args:
        data_pusher (DataPusher): The DataPusher instance.
    """
    dataframe = data_pusher.get_data_from_mongodb()
    assert isinstance(dataframe, pd.DataFrame)
    assert dataframe.shape[0] > 0


def test_push_to_mongodb(data_pusher: DataPusher) -> None:
    """Test case for pushing data to MongoDB.

    Args:
        data_pusher (DataPusher): The DataPusher instance.
    """
    data_frame = pd.DataFrame(
        {
            "password": ["123456", "password"],
            "strength": [0.17233083320907958, 0.24954265948891105],
        },
    )
    data_pusher.push_to_mongodb(data_frame)


if __name__ == "__main__":
    pytest.main()
