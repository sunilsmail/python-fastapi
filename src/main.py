import logging
from fastapi import FastAPI
from .routes import router

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("app.log"),  # Save logs to file
        logging.StreamHandler()  # Show logs in console
    ]
)

app = FastAPI(title="FastAPI CRUD with SOLID Principles")
# logging.info("Root endpoint accessed")
app.include_router(router)
