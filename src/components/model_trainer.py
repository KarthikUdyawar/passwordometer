"""This module provides a class for model training and evaluation."""

import sys
from typing import Any, Tuple

import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from src.interface.config import FilePathConfig
from src.middleware.exception import CustomException
from src.middleware.logger import logger
from src.utils.file_manager import save_object


class ModelTrainer:
    """A class for model training and evaluation."""

    def __init__(self) -> None:
        """Initialize the ModelTrainer object."""
        self.filepath_config = FilePathConfig()
        self.models = {
            "Decision Tree": DecisionTreeRegressor(),
        }
        self.params = {
            "Decision Tree": {
                "criterion": [
                    "squared_error",
                    "friedman_mse",
                    "absolute_error",
                    "poisson",
                ],
                "splitter": ["best", "random"],
                "max_features": ["sqrt", "log2"],
            },
        }

    def evaluate_models(
        self,
        train_array: np.ndarray[np.float64, Any],
        test_array: np.ndarray[np.float64, Any],
    ) -> dict[str, Any]:
        """Evaluate multiple models using GridSearchCV.

        Args:
            train_array (np.ndarray): Training data array.
            test_array (np.ndarray): Testing data array.

        Raises:
            CustomException: If there is an error during model evaluation.

        Returns:
            dict: A dictionary containing the model names as keys and
            their evaluation scores as values.
        """
        try:
            logger.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )
            logger.info("Done split training and test input data")

            logger.info("Started evaluate models")
            test_report = {}

            for i in range(len(list(self.models))):
                model = list(self.models.values())[i]
                para = self.params[list(self.models.keys())[i]]
                logger.debug("%s Model: %s, parameter: %s", i, model, para)

                logger.info("Started training")
                gs = GridSearchCV(model, para, cv=3, n_jobs=-1, verbose=1)
                gs.fit(X_train, y_train)
                logger.info("Done training")

                logger.info("Started training best params")
                model.set_params(**gs.best_params_)
                model.fit(X_train, y_train)
                logger.info("Done training best params")

                logger.info("Started predicting model")
                y_test_pred = model.predict(X_test)
                logger.info("Done predicting model")

                logger.info("Started score model")
                test_model_score = r2_score(y_test, y_test_pred)
                logger.info("Done score model")

                logger.info("Started storing report")
                test_report[list(self.models.keys())[i]] = test_model_score
                logger.info("Done storing report")

            logger.info("Done evaluate models")
            return test_report

        except Exception as e:
            raise CustomException(e, sys) from e

    def select_best_model(
        self,
        test_report: dict[str, Any],
        test_array: np.ndarray[np.float64, Any],
    ) -> Tuple[str, float | Any]:
        """Select the best model based on the evaluation scores.

        Args:
            test_report (dict): A dictionary containing the model names as
            keys and their evaluation scores as values.
            test_array (np.ndarray): Testing data array.

        Raises:
            CustomException: If there is an error during model selection.

        Returns:
            Tuple[str, float | Any]: A tuple containing the name of the best
            model and its evaluation score.
        """
        try:
            logger.info("Started selecting best models")

            # To get best model score from dict
            best_model_score = max(sorted(test_report.values()))

            # To get best model name from dict
            best_model_name = list(test_report.keys())[
                list(test_report.values()).index(best_model_score)
            ]
            best_model = self.models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found", sys)

            logger.info(
                "Best found model on both training and testing dataset"
            )

            logger.info("Started saving best models")
            save_object(
                file_path=self.filepath_config.model_path,
                obj=best_model,
            )
            logger.info("Done saving best models")

            predicted = best_model.predict(test_array[:, :-1])

            return best_model_name, r2_score(test_array[:, -1], predicted)

        except Exception as e:
            raise CustomException(e, sys) from e


if __name__ == "__main__":
    from src.components.data_transformation import DataTransformation

    data_transformation = DataTransformation()
    transformer_obj = data_transformation.get_data_transformer_object(
        features=["password"]
    )
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        target="strength", transformer=transformer_obj
    )
    model_trainer = ModelTrainer()
    report = model_trainer.evaluate_models(train_arr, test_arr)
    name_model, score = model_trainer.select_best_model(report, test_arr)
    logger.info("Best model: %s Score: %s", name_model, score)
