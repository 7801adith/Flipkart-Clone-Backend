import re
import bcrypt
import uuid

from scripts.logging.application_logging import logger
from scripts.config.app_constants import Regex


class Validator:
    @staticmethod
    def email_validator(email):
        try:
            logger.info(f"Inside email_validator with {email}")
            pattern = re.compile(Regex.email_regex)
            return bool(pattern.match(email)), "Email Address"
        except Exception as ex:
            logger.error(f"Error in email_validator function {ex}")
            return False, "Invalid Email Address"

    @staticmethod
    def phone_validator(phone):
        try:
            logger.info(f"Inside phone_validator with {phone}")
            pattern = re.compile(Regex.phone_regex)
            return bool(pattern.match(phone)), "Phone number"
        except Exception as ex:
            logger.error(f"Error in phone_validator function {ex}")
            return False, "Invalid Phone number"

    def validate_contact_info(self, email, phone):
        try:
            logger.info("Inside validate_contact_info function")
            phone_result, phone_type = self.phone_validator(phone)
            email_result, email_type = self.email_validator(email)
            if not phone_result:
                return False, f"Invalid {phone_type}"
            if not email_result:
                return False, f"Invalid {email_type}"
            return True, "Valid Contact info"
        except Exception as ex:
            logger.error(f"Error in validate_contact_info function {ex}")
            return False, "Invalid Contact details"

    def classify_contact_info(self, key):
        try:
            logger.info("Inside classify_contact_info function")
            logger.info("Differentiating the given input to identify key")
            phone_result, phone_type = self.phone_validator(key)
            if phone_result:
                logger.info("Given Input is Phone number")
                return "phoneNo"
            email_result, email_type = self.email_validator(key)
            if email_result:
                logger.info("Given Input is Email Id")
                return "emailId"
            logger.error("Given Input is invalid, returning 'None' ")
            return None
        except Exception as ex:
            logger.error(f"Error in classify_contact_info function {ex}")



class PasswordHashing:
    @staticmethod
    def hash_password(password):
        try:
            logger.info("Hashing input password for safety")
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(password.encode(), salt)
        except Exception as ex:
            logger.error(f"Error in Hashing Password {ex}")
            raise Exception(f"Unable to Hash Password {ex}")

    @staticmethod
    def verify_password(hashed_password, password):
        try:
            logger.info("Verifying Hashed Password and input password")
            return bcrypt.checkpw(password.encode(), hashed_password)
        except Exception as ex:
            logger.error(f"Error in Verifying Password {ex}")
            raise Exception(f"Unable to Verify Password {ex}")


class GenerateID:

    @staticmethod
    def generate_unique_id(prefix):
        try:
            unique_id = str(uuid.uuid4().hex)[:10]
            return f"{prefix}{unique_id}"
        except Exception as ex:
            logger.error(f"Error in Generating Unique ID {ex}")
            raise Exception(f"Unable to Generate Unique ID {ex}")
