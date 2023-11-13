import uvicorn
from fastapi import FastAPI

from scripts.logging.application_logging import logger


app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the application"


if __name__ == "__main__":
    logger.info("Starting Flipkart Backend")
    uvicorn.run(app, host="localhost", port=5858)