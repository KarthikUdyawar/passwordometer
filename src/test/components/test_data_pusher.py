import os
import pandas as pd
import pytest
from src.interface.config import FilePathConfig, MongoDBConfig
from src.components.data_pusher import DataPusher
from dataclasses import dataclass


# Mock the necessary dependencies
@dataclass
class MockMongoDBConfig(FilePathConfig):
    mongodb_connection_string: str = "mongodb://localhost:27017/"
    database_name: str = "passwordometer"
    collection_name: str = "sample"


@dataclass
class MockFilePathConfig(MongoDBConfig):
    raw_data_path: str = os.path.join("raw_dataset", "sample.txt")


@pytest.fixture
def data_pusher_instance():
    data_pusher = DataPusher()
    data_pusher.filepath_config = MockFilePathConfig()
    data_pusher.mongodb_config = MockMongoDBConfig()
    return data_pusher


def test_initiate_data_push(data_pusher_instance):
    data_pusher_instance.initiate_data_push()


def test_get_data_from_mongodb(data_pusher_instance):
    df = data_pusher_instance.get_data_from_mongodb()
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0


def test_push_to_mongodb(data_pusher_instance):
    data_frame = pd.DataFrame(
        {
            "password": ["123456", "password"],
            "strength": [0.17233083320907958, 0.24954265948891105],
        },
    )
    data_pusher_instance.push_to_mongodb(data_frame)


if __name__ == "__main__":
    pytest.main()
