import os
import sys

from sklearn.model_selection import train_test_split

from src.components.data_pusher import DataPusher
from src.interface.config import FilePathConfig
from src.middleware.exception import CustomException
from src.middleware.logger import logger


class DataIngestion:
    def __init__(self):
        self.filepath_config = FilePathConfig()

    def initiate_data_ingestion(self):
        try:
            logger.info("Started data ingestion method")

            logger.info("Fetching data from MongoDB")
            df = DataPusher().get_data_from_mongodb()
            os.makedirs(
                os.path.dirname(self.filepath_config.raw_data_path),
                exist_ok=True,
            )
            logger.info("Done fetching data from MongoDB")

            logger.info("Train test split initiated")
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42
            )
            logger.info("Done Train test split")

            logger.info("Saving Train test split")
            train_set.to_csv(
                self.filepath_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.filepath_config.test_data_path, index=False, header=True
            )
            logger.info("Finish saving Train test split")
            logger.info("Data ingestion completed")

            return (
                self.filepath_config.train_data_path,
                self.filepath_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys) from e


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
