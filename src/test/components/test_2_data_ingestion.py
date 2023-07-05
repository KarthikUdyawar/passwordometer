"""
This module contains test cases for the DataIngestion class.
"""
# import os
# from dataclasses import dataclass

# import pandas as pd
import pytest

# from src.build.interface.config import FilePathConfig
# from src.components.data_ingestion import DataIngestion
# from src.components.data_pusher import DataPusher
# from src.interface.config import MongoDBConfig
# from src.test.components.test_1_data_pusher import (
#     data_pusher_fixture,
#     test_initiate_data_push,
# )


# # Mock the necessary dependencies
# @dataclass
# class MockMongoDBConfig(MongoDBConfig):
#     """Mock configuration class for MongoDB."""

#     mongodb_connection_string: str = "mongodb://localhost:27017/"
#     database_name: str = "passwordometer"
#     collection_name: str = "sample"


# @dataclass
# class MockFilePathConfig(FilePathConfig):
#     """Mock configuration class for file paths."""

#     raw_data_path: str = os.path.join("src/test/data", "sample.txt")


# @pytest.fixture(scope="session", name="data_pusher")  # type: ignore
# def data_pusher_fixture() -> DataPusher:
#     """Fixture for creating a DataPusher instance with mock configurations.

#     Returns:
#         DataPusher: The DataPusher instance.
#     """
#     data_pusher = DataPusher()
#     data_pusher.mongodb_config = MockMongoDBConfig()
#     data_pusher.filepath_config = MockFilePathConfig()

#     return data_pusher


# @pytest.fixture(scope="session", name="data_ingestion")  # type: ignore
# def data_ingestion_fixture() -> DataIngestion:
#     """
#     Fixture to create a DataIngestion object before each test.

#     Returns:
#         DataIngestion: An instance of the DataIngestion class.
#     """
#     # data_pusher = data_pusher_fixture()
#     data_ingestion = DataIngestion()
#     return data_ingestion


# def test_initiate_data_ingestion(data_ingestion: DataIngestion) -> None:
#     """
#     Test the initiate_data_ingestion method of DataIngestion.

#     Args:
#         data_ingestion (DataIngestion): An instance of the DataIngestion class.
#     """
#     train_path, test_path = data_ingestion.initiate_data_ingestion()
#     assert os.path.exists(train_path)
#     assert os.path.exists(test_path)


# def test_data_report(data_ingestion: DataIngestion) -> None:
#     """
#     Test the data_report method of DataIngestion.

#     Args:
#         data_ingestion (DataIngestion): An instance of the DataIngestion class.
#     """
#     data_ingestion.initiate_data_ingestion()
#     data_ingestion.data_report()


# def test_train_test_split_ratio(data_ingestion: DataIngestion) -> None:
#     """
#     Test the train-test split ratio.

#     Args:
#         data_ingestion (DataIngestion): An instance of the DataIngestion class.
#     """
#     data_ingestion.initiate_data_ingestion()
#     train_df = pd.read_csv(data_ingestion.filepath_config.train_data_path)
#     test_df = pd.read_csv(data_ingestion.filepath_config.test_data_path)
#     total_samples = len(train_df) + len(test_df)
#     expected_train_ratio = len(train_df) / total_samples
#     expected_test_ratio = len(test_df) / total_samples
#     assert pytest.approx(expected_train_ratio, abs=0.01) == 0.8
#     assert pytest.approx(expected_test_ratio, abs=0.01) == 0.2


# def test_missing_values(data_ingestion: DataIngestion) -> None:
#     """
#     Test for the absence of missing values in the train and test data.

#     Args:
#         data_ingestion (DataIngestion): An instance of the DataIngestion class.
#     """
#     data_ingestion.initiate_data_ingestion()
#     train_df = pd.read_csv(data_ingestion.filepath_config.train_data_path)
#     test_df = pd.read_csv(data_ingestion.filepath_config.test_data_path)
#     assert not train_df.isnull().values.any()
#     assert not test_df.isnull().values.any()


if __name__ == "__main__":
    pytest.main()