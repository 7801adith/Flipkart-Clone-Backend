from scripts.logging.application_logging import logger


class UserManagement:

    def user_signup(self, req_json):
        try:
            logger.info("Inside user_signup function")


        except Exception as ex:
            logger.error(f"Error in user_signup function, Failed to insert user {ex}")
