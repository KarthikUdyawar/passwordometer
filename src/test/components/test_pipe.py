"""This module contains test cases for the Pipeline class."""
import pytest
import numpy as np

from src.pipe.pipeline import Pipeline
from src.interface.config import CustomData


def test_push_data(pipeline: Pipeline) -> None:
    """Test case for the `push_data` method.

    Args:
        pipeline (Pipeline): The Pipeline instance.
    """
    assert pipeline.push_data() is None

def test_train(pipeline: Pipeline) -> None:
    """Test case for the `train` method.

    Args:
        pipeline (Pipeline): The Pipeline instance.
    """
    assert pipeline.train() is None

def test_predict(pipeline: Pipeline, custom_data:CustomData) -> None:
    """Test case for the `predict` method.

    Args:
        pipeline (Pipeline): The Pipeline instance.
        custom_data (CustomData): The CustomData instance.
    """
    input_data = "test_password123"
    password = custom_data.data2df(input_data)
    result = pipeline.predict(password)
    value = custom_data.array2data(result)
    assert isinstance(result, np.ndarray)
    assert isinstance(value, float)

if __name__ == "__main__":
    pytest.main()
    