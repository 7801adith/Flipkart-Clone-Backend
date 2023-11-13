from fastapi import APIRouter
from scripts.config.app_constants import Routes, UserEndpoints
from scripts.logging.application_logging import logger
from scripts.core.models.user_management_model import Signup

user_route = APIRouter(prefix=Routes.user_route)


@user_route.post(UserEndpoints.signup)
def user_signup(req_json: Signup):
    try:
        logger.info(f"Inside {UserEndpoints.signup} Endpoint")

    except Exception as ex:
        logger.error(f"Error in {UserEndpoints.signup} Endpoint {ex}")
