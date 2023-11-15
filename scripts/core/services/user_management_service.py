from fastapi import APIRouter
from scripts.config.app_constants import Routes, UserEndpoints
from scripts.logging.application_logging import logger
from scripts.core.models.user_management_model import Signup, Login
from scripts.core.handlers.user_management_handler import UserManagement

user_route = APIRouter(prefix=Routes.user_route)


@user_route.post(UserEndpoints.signup)
def user_signup(req_json: Signup):
    """
    Function to register user details
    :param req_json: First Name, Last Name, Email ID, Phone No, Password
    :return: A JSON structure with proper message and status
    """
    try:
        logger.info(f"Inside {UserEndpoints.signup} Endpoint")
        response = UserManagement().user_signup(req_json)
        return response
    except Exception as ex:
        logger.error(f"Error in {UserEndpoints.signup} Endpoint {ex}")


@user_route.post(UserEndpoints.login)
def user_login(req_json: Login):
    """
    Function to log in a user
    :param req_json: user_id, password
    :return: A JSON structure with proper message and status, also user_id if login is success
    """
    try:
        logger.info(f"Inside {UserEndpoints.login} Endpoint")
        response = UserManagement().user_login(req_json)
        return response
    except Exception as ex:
        logger.error(f"Error in {UserEndpoints.login} Endpoint {ex}")


@user_route.post(UserEndpoints.forgot_password)
def forgot_password(req_json: Login):
    try:
        logger.info(f"Inside {UserEndpoints.forgot_password} Endpoint")
        response = UserManagement().forgot_password(req_json)
        return response
    except Exception as ex:
        logger.error(f"Error in {UserEndpoints.forgot_password} Endpoint {ex}")



