import uvicorn
from fastapi import FastAPI

from scripts.logging.application_logging import logger
from scripts.config.app_configurations import APP_HOST, APP_PORT
from scripts.core.services.user_management_service import user_route


app = FastAPI(title="Flipkart")

app.include_router(user_route)

@app.get("/")
def read_root():
    return "Welcome to the application"


if __name__ == "__main__":
    logger.info("Starting Flipkart Backend")
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
