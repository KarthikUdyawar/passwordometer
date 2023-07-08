import numpy as np
import pytest
from sklearn.compose import ColumnTransformer

from src.components.data_transformation import DataTransformation


def test_get_data_transformer_object(data_transformation: DataTransformation):
    features = ["password"]
    transformer = data_transformation.get_data_transformer_object(features)
    assert isinstance(transformer, ColumnTransformer)


def test_initiate_data_transformation(data_transformation: DataTransformation):
    features = ["password"]
    target = "strength"
    transformer = data_transformation.get_data_transformer_object(features)
    result = data_transformation.initiate_data_transformation(target, transformer)
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], np.ndarray)
    assert isinstance(result[1], np.ndarray)
    assert isinstance(result[2], str)


if __name__ == "__main__":
    pytest.main()
