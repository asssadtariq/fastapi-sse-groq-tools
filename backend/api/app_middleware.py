"""
This module is responsible for adding middleware to the FastAPI application instance.
The function register_middleware() takes a FastAPI instance as an argument and adds
middleware to it.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.constants.origins import ORIGINS


def register_middleware(app: FastAPI) -> None:
    """
    Registers API middleware with the provided FastAPI application instance.
    Args:
        app (FastAPI): The FastAPI application instance to which the middleware will be added.
    Returns:
        None
    """

    # Add CORS middleware to allow requests from the frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # you can add any other middleware here
    # app.add_middleware(MyCustomMiddleware)
