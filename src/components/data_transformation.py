"""This module provides a class for data transformation and preprocessing."""

import sys
from typing import Any, List

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer

from src.interface.config import FilePathConfig
from src.middleware.exception import CustomException
from src.middleware.logger import logger
from src.utils.feature_extraction import (
    AlphaLCTransform,
    AlphaUCTransform,
    ConsecAlphaLCTransform,
    ConsecAlphaUCTransform,
    ConsecNumberTransform,
    ConsecSymbolTransform,
    LenTransform,
    MidCharTransform,
    NumberTransform,
    RepCharTransform,
    SeqAlphaTransform,
    SeqKeyboardTransform,
    SeqNumberTransform,
    SymbolTransform,
    UniqueCharTransform,
)
from src.utils.file_manager import save_object


class DataTransformation:
    """A class for data transformation and preprocessing."""

    def __init__(self) -> None:
        """Initialize the DataTransformation object."""
        self.filepath_config = FilePathConfig()

    def get_data_transformer_object(
        self, features: List[str]
    ) -> ColumnTransformer:
        """Get a ColumnTransformer object for data transformation.

        Args:
            features (List[str]): List of feature names.

        Raises:
            CustomException: If there is an error during the transformation.

        Returns:
            ColumnTransformer: The ColumnTransformer object for data transformation.
        """
        try:
            logger.info("Initialize preprocess")

            preprocessor = ColumnTransformer(
                [
                    ("len", LenTransform(), features),
                    ("alpha_uc", AlphaUCTransform(), features),
                    ("alpha_lc", AlphaLCTransform(), features),
                    ("number", NumberTransform(), features),
                    ("symbol", SymbolTransform(), features),
                    ("mid_char", MidCharTransform(), features),
                    ("rep_char", RepCharTransform(), features),
                    ("unique_char", UniqueCharTransform(), features),
                    ("consec_alpha_uc", ConsecAlphaUCTransform(), features),
                    ("consec_alpha_lc", ConsecAlphaLCTransform(), features),
                    ("consec_number", ConsecNumberTransform(), features),
                    ("consec_symbol", ConsecSymbolTransform(), features),
                    ("seq_alpha", SeqAlphaTransform(), features),
                    ("seq_number", SeqNumberTransform(), features),
                    ("seq_keyboard", SeqKeyboardTransform(), features),
                ]
            )
            logger.info("Complete preprocess")
            return preprocessor
        except Exception as error:
            raise CustomException(error, sys) from error

    def initiate_data_transformation(
        self, features: List[str], target: str
    ) -> tuple[Any, Any, str]:
        """Initiate the data transformation process.

        Args:
            features (List[str]): List of feature names.
            target (str): The target variable name.

        Raises:
            CustomException: If there is an error during the data transformation.

        Returns:
            tuple[Any, Any, str]: A tuple containing the transformed training
            and testing data arrays, the path to the saved preprocessing object.
        """
        try:
            logger.info("Fetching train and test data")
            train_df = pd.read_csv(self.filepath_config.train_data_path)
            test_df = pd.read_csv(self.filepath_config.test_data_path)

            logger.info("Read train and test data completed")

            logger.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object(features)

            X_train = train_df.drop(columns=[target], axis=1)
            y_train = train_df[target]

            X_test = test_df.drop(columns=[target], axis=1)
            y_test = test_df[target]

            logger.info(
                "Applying preprocessing object on training dataframe and testing dataframe."
            )

            X_train_arr = preprocessing_obj.fit_transform(X_train)
            X_test_arr = preprocessing_obj.transform(X_test)

            train_arr = np.c_[X_train_arr, np.array(y_train)]
            test_arr = np.c_[X_test_arr, np.array(y_test)]

            logger.info("Saved preprocessing object.")

            save_object(
                file_path=self.filepath_config.preprocessor_path,
                obj=preprocessing_obj,
            )

            return (
                train_arr,
                test_arr,
                self.filepath_config.preprocessor_path,
            )
        except Exception as error:
            raise CustomException(error, sys) from error


if __name__ == "__main__":
    t = DataTransformation()
    t.initiate_data_transformation(["password"], "strength")
