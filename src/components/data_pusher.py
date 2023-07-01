import sys

import pandas as pd
from pymongo import MongoClient

from src.interface.config import FilePathConfig, MongoDBConfig
from src.middleware.exception import CustomException
from src.middleware.logger import logger
from src.utils.data_validation import isValidPassword
from src.utils.feature_extraction import cal_strength


class DataPusher:
    def __init__(self):
        self.mongodb_config = MongoDBConfig()
        self.filepath_config = FilePathConfig()

    def initiate_data_push(self):
        try:
            logger.info("Started data push method")

            logger.info("Started fetching data")
            df = pd.read_csv(
                self.filepath_config.raw_data_path,
                header=None,
                names=["password"],
                sep="\t",
                encoding="ISO-8859-1",
            )
            logger.info("Done fetching data")

            logger.info("Started removing duplicates")
            df = df.dropna()
            logger.info("Done removing duplicates")

            logger.info("Started cleaning data")
            df["IsValid"] = df["password"].apply(lambda x: isValidPassword(x))
            clean_df = df[df["IsValid"] == 1]
            clean_df = clean_df.drop(["IsValid"], axis=1)
            logger.info("Done cleaning data")

            logger.info("Started creating target data")
            clean_df["strength"] = clean_df["password"].apply(lambda x: cal_strength(x))
            logger.info("Done creating target data")

            logger.info("Started data pushed to MongoDB")
            self.push_to_mongodb(clean_df)
            logger.info("Done data pushed to MongoDB")

            logger.info("Data push completed")

        except Exception as e:
            raise CustomException(e, sys) from e

    def push_to_mongodb(self, df, chunk_size=10_00_000):
        try:
            logger.info("Started connected to MongoDB")
            client = MongoClient(self.mongodb_config.mongodb_connection_string)
            db = client[self.mongodb_config.database_name]
            collection = db[self.mongodb_config.collection_name]
            logger.info("Done connected to MongoDB")

            total_rows = df.shape[0]
            num_chunks = (total_rows // chunk_size) + 1

            logger.info("Started insert data into MongoDB")
            for chunk in range(num_chunks):
                start = chunk * chunk_size
                end = min(start + chunk_size, total_rows)
                chunk_data = df.iloc[start:end].to_dict(orient="records")
                collection.insert_many(chunk_data)

                logger.info(f"Chunk {chunk+1}/{num_chunks} inserted into MongoDB")

            self._close_db("Done insert data into MongoDB", client)
        except Exception as e:
            raise CustomException(e, sys) from e

    def get_data_from_mongodb(self, chunk_size=10_00_000):
        try:
            logger.info("Started connected to MongoDB")
            client = MongoClient(self.mongodb_config.mongodb_connection_string)
            db = client[self.mongodb_config.database_name]
            collection = db[self.mongodb_config.collection_name]
            logger.info("Done connected to MongoDB")

            total_documents = collection.count_documents({})
            num_chunks = (total_documents // chunk_size) + 1

            df = pd.DataFrame()

            logger.info("Started fetch data from MongoDB")
            for chunk in range(num_chunks):
                skip_documents = chunk * chunk_size
                chunk_data = list(
                    collection.find(
                        {},
                        {"_id": 0},  # Exclude the _id field
                        skip=skip_documents,
                        limit=chunk_size,
                    )
                )
                chunk_df = pd.DataFrame(chunk_data)
                df = pd.concat([df, chunk_df], ignore_index=True)

                logger.debug(f"Fetched Chunk {chunk+1}/{num_chunks} from MongoDB")

            self._close_db("Done fetch data from MongoDB", client)
            logger.info("Data retrieved from MongoDB")

            return df

        except Exception as e:
            raise CustomException(e, sys) from e

    def _close_db(self, arg0, client):
        logger.info(arg0)
        logger.info("Started close MongoDB")
        client.close()
        logger.info("Done close MongoDB")


if __name__ == "__main__":
    df = DataPusher().get_data_from_mongodb()
    logger.debug(df.info())
