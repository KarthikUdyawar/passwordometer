import os
import pandas as pd
from src.components.data_ingestion import DataIngestion
import pytest


@pytest.fixture
def data_ingestion():
    return DataIngestion()


def test_initiate_data_ingestion(data_ingestion):
    train_path, test_path = data_ingestion.initiate_data_ingestion()
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)


def test_data_report(data_ingestion):
    data_ingestion.initiate_data_ingestion()
    data_ingestion.data_report()


def test_train_test_split_ratio(data_ingestion):
    data_ingestion.initiate_data_ingestion()
    train_df = pd.read_csv(data_ingestion.filepath_config.train_data_path)
    test_df = pd.read_csv(data_ingestion.filepath_config.test_data_path)
    total_samples = len(train_df) + len(test_df)
    expected_train_ratio = len(train_df) / total_samples
    expected_test_ratio = len(test_df) / total_samples
    assert pytest.approx(expected_train_ratio, abs=0.01) == 0.8
    assert pytest.approx(expected_test_ratio, abs=0.01) == 0.2


def test_missing_values(data_ingestion):
    data_ingestion.initiate_data_ingestion()
    train_df = pd.read_csv(data_ingestion.filepath_config.train_data_path)
    test_df = pd.read_csv(data_ingestion.filepath_config.test_data_path)
    assert not train_df.isnull().values.any()
    assert not test_df.isnull().values.any()
