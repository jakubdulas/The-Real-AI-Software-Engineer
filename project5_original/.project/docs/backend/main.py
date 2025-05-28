"""
main.py
-------
This is the main entry point for the FastAPI backend of the TODO application.
It defines the FastAPI application instance and the root endpoint.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint for the API.

    Returns a welcome message to verify the API is running.
    """
    return {"message": "Welcome to the TODO API"}
