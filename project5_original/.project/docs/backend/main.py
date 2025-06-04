"""
main.py
---------
Entry point for the FastAPI TODO backend.

This script initializes the FastAPI application and includes the API routes for managing TODO tasks.

How it works:
- Imports and creates a FastAPI application (`app`).
- Imports the task API router from `api/tasks.py` and includes it in the app, mounting all task endpoints (`/tasks`).
"""

from fastapi import FastAPI
from api.tasks import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)
