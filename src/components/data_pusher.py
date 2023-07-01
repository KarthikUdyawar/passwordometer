

class DataPusher:
    def __init__(self):
        self.mongodb_config = MongoDBConfig()
        self.filepath_config = FilePathConfig()

    def initiate_data_push(self):
        try:
            logger.info("Started data push method")

