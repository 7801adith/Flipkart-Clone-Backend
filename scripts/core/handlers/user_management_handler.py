from scripts.logging.application_logging import logger
from scripts.utilities.validator import Validator
from scripts.utilities.mongo_utility import MongoUtility
from scripts.config.app_constants import MongoCollections


class UserManagement:

    @staticmethod
    def user_signup(req_json):
        try:
            logger.info("Inside user_signup function")
            logger.info("Checking for user duplication using phone number and email")
            if MongoUtility().fetch_mongo_record(MongoCollections.user_collection,
                                                 {"email": req_json.email_id, "phone": req_json.phone_no},
                                                 {"user_id": 1}):
                logger.info("User already exists with given details")
                return {"status": 0, "message": "User already exists. Please try login"}
            validate, message = Validator().validate_contact_info(req_json.email_id, req_json.phone_no)
            if not validate:
                logger.info(message)
                return {"status": 0, "message": message}




        except Exception as ex:
            logger.error(f"Error in user_signup function, Failed to insert user {ex}")
