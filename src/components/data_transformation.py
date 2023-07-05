import sys

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer

from src.interface.config import FilePathConfig
from src.middleware.exception import CustomException
from src.middleware.logger import logger
from src.utils.feature_extraction import (AlphaLCTransform, AlphaUCTransform,
                                          ConsecAlphaLCTransform,
                                          ConsecAlphaUCTransform,
                                          ConsecNumberTransform,
                                          ConsecSymbolTransform, LenTransform,
                                          MidCharTransform, NumberTransform,
                                          RepCharTransform, SeqAlphaTransform,
                                          SeqKeyboardTransform,
                                          SeqNumberTransform, SymbolTransform,
                                          UniqueCharTransform)
from src.utils.file_manager import save_object


class DataTransformation:
    def __init__(self):
        self.filepath_config = FilePathConfig()

    def get_data_transformer_object(self, features):
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
        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_transformation(self, train_path, test_path, features, target):
        try:
            logger.info("Fetching train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

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
        except Exception as e:
            raise CustomException(e, sys) from e
