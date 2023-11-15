import time

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
                                                 {"emailId": req_json.email_id, "phoneNo": req_json.phone_no},
                                                 {"userId": 1}):
                logger.info("User already exists with given details")
                return {"status": 1, "message": "User already exists. Please try login"}
            validate, message = Validator().validate_contact_info(req_json.email_id, req_json.phone_no)
            if not validate:
                logger.info(message)
                return {"status": 1, "message": message}
            user_id = GenerateID().generate_unique_id("user_")
            hashed_pwd = PasswordHashing.hash_password(req_json.password)
            time_stamp = int(time.time())
            record = {'userId': user_id, 'firstName': req_json.first_name,
                      'lastName': req_json.last_name, 'password': hashed_pwd, 'emailId': req_json.email_id,
                      'phoneNo': req_json.phone_no, 'delete': 0, 'createdAt': str(time_stamp), 'modifiedAt':
                          str(time_stamp)}
            MongoUtility().insert_record(MongoCollections.user_collection, record)
            return {'status': 0, 'message': "User Added Successfully"}
        except Exception as ex:
            logger.error(f"Error in user_signup function, Failed to insert user {ex}")
            raise Exception(f"Unable to add new user {ex}")

    @staticmethod
    def user_login(req_json):
        try:
            logger.info("Inside user_login Function")
            key = Validator().classify_contact_info(req_json.user_id)
            if not key:
                logger.error("Invalid Input: Not Phone number or Email")
                return {'status': 1, "message": "Please Enter Valid Email id or Phone"}
            record = MongoUtility().fetch_mongo_record(MongoCollections.user_collection,
                                                       {key: req_json.user_id},
                                                       {"password": 1, "userId": 1})
            if not record:
                logger.error("User details not found")
                return {'status': 1, "message": "Account not found, Please signup"}
            match = PasswordHashing().verify_password(record.get("password", ""), req_json.password)
            if match:
                logger.info("Password Match, Signing in user")
                return {'status': 0, 'message': "Logged in Successfully", "user_id": record.get("userId", "")}
            logger.error("Entered password is wrong")
            return {'status': 1, "message": "Wrong Password"}
        except Exception as ex:
            logger.error(f"Error in user_login function, Failed to login user {ex}")
            raise Exception(f"Unable to login user {ex}")

    @staticmethod
    def forgot_password(req_json):
        try:
            logger.info("Inside forgot_password function")
            key = Validator().classify_contact_info(req_json.user_id)
            if not key:
                logger.error("Invalid Input: Not Phone number or Email")
                return {'status': 1, "message": "Please Enter Valid Email id or Phone"}
            record = MongoUtility().fetch_mongo_record(MongoCollections.user_collection,
                                                       {key: req_json.user_id},
                                                       {"userId": 1})
            if not record:
                logger.error("User details not found")
                return {'status': 1, "message": "Account not found, Please signup"}
            hashed_pwd = PasswordHashing.hash_password(req_json.password)
            time_stamp = int(time.time())
            update = {"$set": {"password": hashed_pwd, "modifiedAt": str(time_stamp)}}
            MongoUtility().update_mongo_record(MongoCollections.user_collection,
                                               {"userId": record.get("userId")}, update)
            return {'status': 0, 'message': "Password Updated Successfully"}
        except Exception as ex:
            logger.error(f"Error in forgot_password function, Failed to change password {ex}")
            raise Exception(f"Unable to change password {ex}")
