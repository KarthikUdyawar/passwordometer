"""
A pipeline for data ingestion, transformation, model training, 
and prediction.
"""

import sys
from typing import Any

import numpy as np
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_pusher import DataPusher
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.interface.config import CustomData, FilePathConfig
from src.middleware.exception import CustomException
from src.middleware.logger import logger
from src.utils.file_manager import load_object


class Pipeline:
    """A pipeline for data ingestion, transformation, model training,
    and prediction."""

    def __init__(self) -> None:
        """Initialize the Pipeline object."""

        self.data_pusher = DataPusher()
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()
        self.filepath_config = FilePathConfig()

    def push_data(self) -> None:
        """Push data to MongoDB, perform data ingestion, and generate
        data report.

        Raises:
            CustomException: If there is an error during the data push,
            data ingestion, or data report generation.
        """
        try:
            df = self.data_pusher.initiate_data_push()
            self.data_pusher.push_to_mongodb(df)
            self.data_ingestion.initiate_data_ingestion()
            self.data_ingestion.data_report()

        except Exception as error:
            raise CustomException(error, sys) from error

    def train(self) -> None:
        """Perform data transformation, model training, and select the
        best model.

        Raises:
            CustomException: If there is an error during the data
            transformation or model training.
        """
        try:
            transformer_obj = (
                self.data_transformation.get_data_transformer_object(
                    features=["password"]
                )
            )
            (
                train_arr,
                test_arr,
                _,
            ) = self.data_transformation.initiate_data_transformation(
                target="strength", transformer=transformer_obj
            )
            report = self.model_trainer.evaluate_models(train_arr, test_arr)
            name_model, score = self.model_trainer.select_best_model(
                report, test_arr
            )
            logger.info("Best model: %s Score: %s", name_model, score)

        except Exception as error:
            raise CustomException(error, sys) from error

    def predict(self, features: pd.DataFrame) -> np.ndarray[np.float64, Any]:
        """Perform prediction on the given features.

        Args:
            features (pd.DataFrame): The features to be predicted.

        Raises:
            CustomException: If there is an error during the prediction.

        Returns:
            np.ndarray[np.float64, Any]: The predicted values.
        """
        try:
            logger.info("Initiated load files")
            model = load_object(file_path=self.filepath_config.model_path)
            preprocessor = load_object(
                file_path=self.filepath_config.preprocessor_path
            )
            logger.info("Done load files")

            logger.info("Initiated data transformation")
            data_scaled = preprocessor.transform(features)
            logger.info("Done data transformation")

            logger.info("Initiated prediction")
            result = model.predict(data_scaled)
            logger.info("Done prediction")

            return result

        except Exception as error:
            raise CustomException(error, sys) from error


if __name__ == "__main__":

    def predict_usage():
        custom_data = CustomData()
        input_data = str(input("Enter the password: "))
        password = custom_data.data2df(input_data)
        strength = Pipeline().predict(password)
        value = custom_data.array2data(strength)
        logger.info(f"\nPassword: {input_data} Strength: {value}")

    def train_usage():
        Pipeline().train()

    def push_data_usage():
        Pipeline().push_data()

    print("Main menu")
    print("1. Push data")
    print("2. Train pipeline")
    print("3. Predict pipeline")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        push_data_usage()
    elif choice == 2:
        train_usage()
    elif choice == 3:
        predict_usage()
    else:
        raise CustomException("Invalid input", sys)
