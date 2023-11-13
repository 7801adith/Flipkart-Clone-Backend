from scripts.logging.application_logging import logger
from scripts.utilities.validator import Validator, GenerateID, PasswordHashing
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
            user_id = GenerateID().generate_unique_id("user_")
            hashed_pwd = PasswordHashing.hash_password(req_json.password)
            record = {'userId': user_id, 'firstName': req_json.first_name,
                      'lastName': req_json.last_name, 'password': hashed_pwd, 'emailId': req_json.email_id,
                      'phoneNo': req_json.phone_no}
            MongoUtility().insert_record(MongoCollections.user_collection, record)
            return {'status': 0, 'message': "User Added Successfully"}
        except Exception as ex:
            logger.error(f"Error in user_signup function, Failed to insert user {ex}")
            raise Exception(f"Unable to add new user {ex}")
