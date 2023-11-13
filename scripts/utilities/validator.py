import re

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
