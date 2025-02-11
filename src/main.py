from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FastAPI CRUD with SOLID Principles")

app.include_router(router)
