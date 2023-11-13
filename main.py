import uvicorn
from fastapi import FastAPI

from scripts.logging.application_logging import logger
from scripts.config.app_configurations import APP_HOST, APP_PORT


app = FastAPI(title="Flipkart")


@app.get("/")
def read_root():
    return "Welcome to the application"


if __name__ == "__main__":
    logger.info("Starting Flipkart Backend")
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
