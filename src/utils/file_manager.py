import os
import sys

import joblib

from src.middleware.exception import CustomException
from src.middleware.logger import logger


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        joblib.dump(obj, file_path)

    except Exception as e:
        raise CustomException(e, sys) from e


def load_object(file_path):
    try:
        return joblib.load(file_path)

    except Exception as e:
        raise CustomException(e, sys) from e
