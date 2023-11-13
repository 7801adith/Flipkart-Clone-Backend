from pymongo import MongoClient
from scripts.logging.application_logging import logger
from scripts.config.app_configurations import MONGO_HOST, MONGO_PORT, MONGO_DB


class MongoUtility:
    @staticmethod
    def connect_cursor():
        try:
            logger.info(f"Connecting MongoDB with {MONGO_HOST}, {MONGO_PORT}, {MONGO_DB}")
            client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
            database = client[MONGO_DB]
            return database, client
        except Exception as ex:
            logger.eror(f"Error establishing connection to Mongo {ex}")
            raise Exception(f"Unable to connect Mongo {ex}")

    def insert_record(self, collection_name, record):
        database, client = self.connect_cursor()
        try:
            logger.info("Inside Mongo insert_record function")
            status = database[collection_name].insert_one(record)
            return status
        except Exception as ex:
            logger.eror(f"Error inserting record to Mongo {ex}")
            raise Exception(f"Unable to insert record {ex}")
        finally:
            logger.info("Closing Mongo Connection")
            client.close()

    def fetch_mongo_record(self, collection_name, query, projection={}):
        database, client = self.connect_cursor()
        try:
            logger.info("Inside fetch_mongo_record function")
            projection.update({"_id": 0})
            query.update({"delete": 0})
            record = database[collection_name].find_one(query, projection)
            return record
        except Exception as ex:
            logger.error(f"Error in fetching record {ex}")
            raise Exception(f"Unable to fetch record {ex}")
        finally:
            logger.info("Closing Mongo Connection")
            client.close()
