"""
This module is responsible for adding routes to the FastAPI application instance.
The function register_routes() takes a FastAPI instance as an argument and adds
routes to it.
"""

from fastapi import FastAPI

from api.routes.query import router as query_router


def register_routes(app: FastAPI) -> None:
    """
    Registers API routes with the provided FastAPI application instance.
    Args:
        app (FastAPI): The FastAPI application instance to which the routes will be added.
    Returns:
        None
    """

    app.include_router(query_router)
