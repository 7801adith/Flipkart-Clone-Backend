from pymongo import MongoClient
from scripts.logging.application_logging import logger
from scripts.config.app_configurations import MONGO_HOST, MONGO_PORT, MONGO_DB


class MongoUtility:
    @staticmethod
    def connect_cursor():
        try:
            logger.info(f"Connecting MongoDB with {MONGO_HOST}, {MONGO_PORT}, {MONGO_DB}")
            client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}")
            return client
        except Exception as ex:
            logger.eror(f"Error establishing connection to Mongo {ex}")
            raise Exception(f"Unable to connect Mongo {ex}")

    def insert_record(self, collection_name, record):
        client = self.connect_cursor()
        try:
            logger.info("Inside Mongo insert_record function")
            status = client[collection_name].insert_one(record)
            return status
        except Exception as ex:
            logger.eror(f"Error inserting record to Mongo {ex}")
            raise Exception(f"Unable to insert record {ex}")
        finally:
            logger.info("Closing Mongo Connection")
            client.close()
